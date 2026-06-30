"""Token-geauthenticeerde MCP-server (streamable HTTP) die OpenWebUI-kennis ontsluit.

Beveiliging:
- Elk verzoek vereist `Authorization: Bearer <token>`; ongeldig/ontbrekend -> 401 (default-deny).
- Geen enkele endpoint lekt info zonder geldig token (behalve /health, dat geeft alleen "ok").
- De OpenWebUI-API-key zit server-side (openwebui_client) en gaat nooit naar de client.
- Audit-log per aanroep: token-id + pad + status + duur. GEEN query-/antwoordinhoud (PII) in logs.
- TLS wordt door de reverse proxy ervoor afgedwongen (zie nginx.simple.conf).
"""
from __future__ import annotations

import logging
import time

import uvicorn
from mcp.server.fastmcp import FastMCP

import config
import tokens
import openwebui_client

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("knowledge-mcp")

mcp = FastMCP("knowledge-mcp", host=config.MCP_HOST, port=config.MCP_PORT)


@mcp.tool()
async def search_knowledge(query: str) -> str:
    """Doorzoek de kennisbank en geef een gegrond antwoord op basis van de opgeslagen kennis.

    Gebruik dit om vragen te beantwoorden over onderwerpen in de kennisbank.
    """
    return await openwebui_client.search_knowledge(query)


class BearerAuthMiddleware:
    """Pure-ASGI middleware: valideert het bearer-token vóór elke MCP-aanroep.

    Pure ASGI (geen BaseHTTPMiddleware) zodat streaming/SSE van MCP intact blijft.
    """

    PUBLIC_PATHS = {"/health", "/healthz"}

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            # lifespan / websocket ongemoeid doorlaten
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")
        if path in self.PUBLIC_PATHS:
            await self._send_status(send, 200, b'{"status":"ok"}')
            return

        principal = tokens.validate(self._bearer(scope))
        if principal is None:
            log.warning("auth_denied path=%s", path)
            await self._send_status(
                send, 401, b'{"error":"unauthorized"}',
                extra_headers=[(b"www-authenticate", b"Bearer")],
            )
            return

        start = time.monotonic()
        status_holder = {"status": 0}

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                status_holder["status"] = message["status"]
            await send(message)

        await self.app(scope, receive, send_wrapper)
        log.info(
            "call token=%s path=%s status=%s dur_ms=%d",
            principal["id"], path, status_holder["status"],
            int((time.monotonic() - start) * 1000),
        )

    @staticmethod
    def _bearer(scope) -> str | None:
        for name, value in scope.get("headers", []):
            if name == b"authorization":
                v = value.decode("latin-1")
                if v.lower().startswith("bearer "):
                    return v[7:].strip()
        return None

    @staticmethod
    async def _send_status(send, status, body, extra_headers=None):
        headers = [(b"content-type", b"application/json")] + (extra_headers or [])
        await send({"type": "http.response.start", "status": status, "headers": headers})
        await send({"type": "http.response.body", "body": body})


def main() -> None:
    tokens.init_db()
    app = BearerAuthMiddleware(mcp.streamable_http_app())
    log.info("Knowledge MCP-server start op %s:%d (MCP-pad: /mcp)", config.MCP_HOST, config.MCP_PORT)
    uvicorn.run(app, host=config.MCP_HOST, port=config.MCP_PORT)


if __name__ == "__main__":
    main()
