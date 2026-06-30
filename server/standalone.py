"""
ICTRecht Knowledge MCP Server
- Haalt documentchunks op uit OpenWebUI (geen dubbele inferentie)
- Streamable HTTP transport (werkt met OpenWebUI, M365 Copilot, Claude Desktop)
- Beheerscherm voor multi-tenant token-management
- Copilot Studio auth via Microsoft tenant-ID header

Start: uvicorn main:app --port 8001 --host 0.0.0.0
"""

import os
import json
import hmac
import hashlib
import secrets
import sqlite3
import asyncio
import anyio
from collections import defaultdict
from datetime import datetime, timedelta

import httpx
from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse
from mcp.server import Server
from mcp.server.streamable_http import StreamableHTTPServerTransport
from mcp import types

# ── Configuratie ──────────────────────────────────────────────────────────────

ADMIN_PASSWORD   = os.getenv("ADMIN_PASSWORD", "changeme")
SESSION_SECRET   = os.getenv("SESSION_SECRET", secrets.token_hex(32))
SESSION_TTL      = timedelta(hours=8)
DB_PATH          = os.getenv("DB_PATH", "ictrecht_mcp.db")
SECURE_COOKIES   = os.getenv("SECURE_COOKIES", "true").lower() == "true"
CHUNKS_PER_QUERY = int(os.getenv("CHUNKS_PER_QUERY", "6"))
MAX_QUERIES_DAY  = int(os.getenv("MAX_QUERIES_PER_DAY", "500"))
MAX_QUERY_LEN    = int(os.getenv("MAX_QUERY_LENGTH", "2000"))
ENV              = os.getenv("ENV", "development")

# Publieke URL van de server (voor verbindingsinformatie in admin)
PUBLIC_URL           = os.getenv("PUBLIC_URL", "https://mcp.example.com")

# Copilot Studio — stel MS_TENANT_ID in om Microsoft-header auth te activeren
MS_TENANT_ID         = os.getenv("MS_TENANT_ID", "")
COPILOT_OWUI_URL     = os.getenv("COPILOT_OPENWEBUI_URL", os.getenv("OPENWEBUI_URL", ""))
COPILOT_OWUI_API_KEY = os.getenv("COPILOT_OPENWEBUI_API_KEY", os.getenv("OPENWEBUI_API_KEY", ""))

# ── Productie-guard ───────────────────────────────────────────────────────────

if ENV == "production" and ADMIN_PASSWORD == "changeme":
    raise RuntimeError("Stel ADMIN_PASSWORD in via omgevingsvariabele vóór productie gebruik.")

# ── Brute-force bescherming (in-memory) ──────────────────────────────────────

_failed_logins:  dict[str, list[datetime]] = defaultdict(list)
LOCKOUT_ATTEMPTS = int(os.getenv("LOCKOUT_ATTEMPTS", "5"))
LOCKOUT_WINDOW   = timedelta(minutes=15)

# ── Kennisbanken ──────────────────────────────────────────────────────────────
# UUID → leesbare naam. De AI ziet alleen namen; de server mapt naar UUID.

ALL_COLLECTIONS: dict[str, str] = {
    "b1c44172-86ba-4504-8b1a-6c58c8ea9120": "Privacy Guide v2",
    "eb430eef-341c-463b-8ab2-9a1712bafb32": "WOO",
    "21982d73-9d75-434d-8c5b-24fcb5d6606d": "Ondernemingsrecht",
    "de0e5e93-0acb-433c-a13a-7f3682c9f16a": "Onderwijsassistent",
    "3d8809ff-c0c1-4d78-947e-a084f425ef2d": "Risico Assistent",
    "e344e0f3-d32a-4151-8238-00e1d5e2bf3a": "VSO Checker",
    "2254dc37-fa85-474b-9345-f5138bbd62cc": "WPG",
    "af813a9e-7d21-4e98-bb4a-0e46695a746a": "Zorgrecht Guide",
    "3538820f-87e6-45fb-bf27-65428a818200": "Arbeidsovereenkomsten Checker",
    "0ba17aec-794c-4149-9dd6-379712dc25a7": "Ontslag Assistent",
    "387ece26-3cb4-4efd-b809-691645bb86bb": "Wet DBA Guide",
    "2f3b3297-a449-4848-b38b-44cf61d58c2a": "Gegevensverwerking Assistent",
}

_NAME_TO_ID: dict[str, str] = {v: k for k, v in ALL_COLLECTIONS.items()}

# ── Session store ─────────────────────────────────────────────────────────────

_sessions: dict[str, datetime] = {}


def _create_session() -> str:
    token = secrets.token_urlsafe(32)
    _sessions[token] = datetime.now()
    return token


def _is_valid_session(token: str) -> bool:
    ts = _sessions.get(token)
    if not ts:
        return False
    if datetime.now() - ts > SESSION_TTL:
        _sessions.pop(token, None)
        return False
    return True


def _csrf_token(session_token: str) -> str:
    return hmac.new(
        SESSION_SECRET.encode(), session_token.encode(), hashlib.sha256
    ).hexdigest()[:32]


def _verify_csrf(session_token: str, submitted: str) -> bool:
    return hmac.compare_digest(_csrf_token(session_token), submitted)


# ── Database ──────────────────────────────────────────────────────────────────

def _get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = _get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id                      INTEGER PRIMARY KEY AUTOINCREMENT,
            name                    TEXT    NOT NULL,
            email                   TEXT,
            token                   TEXT    UNIQUE NOT NULL,
            openwebui_api_key       TEXT    NOT NULL,
            openwebui_url           TEXT    NOT NULL,
            allowed_collections     TEXT    NOT NULL DEFAULT '[]',
            is_active               INTEGER NOT NULL DEFAULT 1,
            created_at              TEXT    NOT NULL,
            last_used_at            TEXT,
            query_count             INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS query_log (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id       INTEGER,
            collection_id   TEXT,
            query           TEXT,
            chunks_returned INTEGER,
            created_at      TEXT
        )
    """)
    conn.commit()
    conn.close()


def _get_client_by_token(token: str):
    conn = _get_db()
    client = conn.execute(
        "SELECT * FROM clients WHERE token = ? AND is_active = 1", (token,)
    ).fetchone()
    conn.close()
    return client


def _get_daily_query_count(client_id: int) -> int:
    conn = _get_db()
    row = conn.execute(
        "SELECT COUNT(*) FROM query_log WHERE client_id = ? AND created_at > datetime('now', '-1 day')",
        (client_id,),
    ).fetchone()
    conn.close()
    return row[0] if row else 0


def _record_query(client_id: int, collection_id: str, query: str, chunks: int) -> None:
    conn = _get_db()
    now = datetime.now().isoformat()
    conn.execute(
        "INSERT INTO query_log (client_id, collection_id, query, chunks_returned, created_at)"
        " VALUES (?, ?, ?, ?, ?)",
        (client_id, collection_id, query[:500], chunks, now),
    )
    conn.execute(
        "UPDATE clients SET last_used_at = ?, query_count = query_count + 1 WHERE id = ?",
        (now, client_id),
    )
    conn.commit()
    conn.close()


# ── Authenticatie ─────────────────────────────────────────────────────────────

async def _authenticate(request) -> tuple[dict | None, str | None]:
    """
    Twee auth-methoden:

    1. Bearer token  →  opzoeken in clients-tabel (Claude Desktop, OpenWebUI, enz.)
    2. Microsoft Copilot Studio headers  →  x-ms-client-tenant-id valideren

    Geeft (client_data, error_message) terug.
    """
    auth = request.headers.get("Authorization", "")

    # Methode 1: Bearer token
    if auth.startswith("Bearer "):
        token = auth.removeprefix("Bearer ").strip()
        client = await asyncio.to_thread(_get_client_by_token, token)
        if not client:
            return None, "Ongeldig of inactief token"
        return dict(client), None

    # Methode 2: Microsoft Copilot Studio (x-ms-client-tenant-id)
    if MS_TENANT_ID:
        ms_tenant = request.headers.get("x-ms-client-tenant-id", "")
        if ms_tenant and hmac.compare_digest(ms_tenant, MS_TENANT_ID):
            # Virtuele Copilot-client — id=-1 zodat query-logging wordt overgeslagen
            return {
                "id":                  -1,
                "name":                "Copilot Studio",
                "openwebui_api_key":   COPILOT_OWUI_API_KEY,
                "openwebui_url":       COPILOT_OWUI_URL,
                "allowed_collections": json.dumps(list(ALL_COLLECTIONS.keys())),
                "is_active":           1,
            }, None

    return None, "Geen geldig authenticatiemiddel"


# ── OpenWebUI retrieval (geen LLM) ────────────────────────────────────────────

async def retrieve_chunks(
    api_key: str,
    openwebui_url: str,
    collection_id: str,
    query: str,
    k: int = CHUNKS_PER_QUERY,
) -> list[dict]:
    """
    Haalt ruwe documentfragmenten op via OpenWebUI's knowledge-query endpoint.
    Er wordt GEEN LLM aangeroepen — alleen vector search.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{openwebui_url}/api/v1/knowledge/{collection_id}/query",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={"query": query, "k": k},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

    chunks: list[dict] = []
    for result in data.get("results", []):
        documents  = result.get("documents",  [])
        metadatas  = result.get("metadatas",  [])
        distances  = result.get("distances",  [])

        for i, text in enumerate(documents):
            meta     = metadatas[i] if i < len(metadatas) else {}
            distance = distances[i] if i < len(distances) else None
            chunks.append({
                "text":   text,
                "source": meta.get("name") or meta.get("source", "onbekend"),
                "page":   meta.get("page_label") or meta.get("page"),
                "score":  round(1 - float(distance), 3) if distance is not None else None,
            })

    return chunks


def _format_chunks(collection_name: str, chunks: list[dict]) -> str:
    if not chunks:
        return f"*{collection_name}* — geen relevante fragmenten gevonden."

    lines = [f"## Kennisbank: {collection_name}\n"]
    for i, chunk in enumerate(chunks, 1):
        ref = chunk["source"]
        if chunk["page"]:
            ref += f", p. {chunk['page']}"
        if chunk["score"] is not None:
            ref += f" (relevantie: {chunk['score']})"
        lines.append(f"**[{i}] {ref}**")
        lines.append(chunk["text"].strip())
        lines.append("")

    return "\n".join(lines)


# ── MCP server builder ────────────────────────────────────────────────────────

def build_mcp_server(client_data: dict) -> Server:
    allowed_ids: list[str] = json.loads(client_data["allowed_collections"])
    allowed_names = [
        ALL_COLLECTIONS[cid] for cid in allowed_ids if cid in ALL_COLLECTIONS
    ]

    mcp = Server("ictrecht-knowledge")

    @mcp.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="search_knowledge",
                description=(
                    "Zoekt in een ICTRecht kennisbank en geeft relevante documentfragmenten "
                    "terug als context. Claude verwerkt de fragmenten zelf — er wordt geen "
                    "tweede AI aangeroepen."
                ),
                inputSchema={
                    "type": "object",
                    "properties": {
                        "collection": {
                            "type": "string",
                            "enum": allowed_names,
                            "description": "Naam van de kennisbank",
                        },
                        "query": {
                            "type": "string",
                            "description": "Zoekvraag in gewone taal",
                        },
                    },
                    "required": ["collection", "query"],
                },
            )
        ]

    @mcp.call_tool()
    async def call_tool(tool_name: str, arguments: dict) -> list[types.TextContent]:
        if tool_name != "search_knowledge":
            return [types.TextContent(type="text", text=f"Onbekende tool: {tool_name}")]

        collection_name = arguments.get("collection", "")
        query           = str(arguments.get("query", ""))[:MAX_QUERY_LEN]

        collection_id = _NAME_TO_ID.get(collection_name)
        if not collection_id or collection_id not in allowed_ids:
            return [types.TextContent(type="text", text="Geen toegang tot deze kennisbank.")]

        try:
            chunks = await retrieve_chunks(
                api_key       = client_data["openwebui_api_key"],
                openwebui_url = client_data["openwebui_url"],
                collection_id = collection_id,
                query         = query,
            )
            # Alleen loggen voor echte clients (Copilot heeft id=-1)
            if client_data["id"] >= 0:
                await asyncio.to_thread(
                    _record_query, client_data["id"], collection_id, query, len(chunks)
                )
            return [types.TextContent(type="text", text=_format_chunks(collection_name, chunks))]

        except httpx.HTTPStatusError as e:
            return [types.TextContent(
                type="text",
                text=f"OpenWebUI API-fout {e.response.status_code}: {e.response.text[:200]}",
            )]
        except Exception as e:
            return [types.TextContent(type="text", text=f"Fout: {e}")]

    return mcp


# ── MCP ASGI handler ──────────────────────────────────────────────────────────

class MCPHandler:
    """ASGI handler voor /mcp — Streamable HTTP MCP requests."""

    async def __call__(self, scope, receive, send) -> None:
        if scope["type"] != "http":
            return

        from starlette.requests import Request as _Req
        request = _Req(scope, receive)

        client_data, error = await _authenticate(request)
        if not client_data:
            await JSONResponse({"detail": error}, status_code=401)(scope, receive, send)
            return

        # Daglimiet — alleen voor echte clients (Copilot heeft id=-1)
        if client_data["id"] >= 0:
            daily_count = await asyncio.to_thread(_get_daily_query_count, client_data["id"])
            if daily_count >= MAX_QUERIES_DAY:
                await JSONResponse(
                    {"detail": f"Daglimiet van {MAX_QUERIES_DAY} queries bereikt"},
                    status_code=429,
                )(scope, receive, send)
                return

        mcp_server = build_mcp_server(client_data)
        transport  = StreamableHTTPServerTransport(
            mcp_session_id=None,
            is_json_response_enabled=False,
        )

        async with anyio.create_task_group() as tg:
            async def run_server(*, task_status=anyio.TASK_STATUS_IGNORED):
                async with transport.connect() as streams:
                    read_stream, write_stream = streams
                    task_status.started()
                    await mcp_server.run(
                        read_stream,
                        write_stream,
                        mcp_server.create_initialization_options(),
                        stateless=True,
                    )

            await tg.start(run_server)
            await transport.handle_request(scope, receive, send)
            tg.cancel_scope.cancel()


# ── RootApp wrapper ───────────────────────────────────────────────────────────
# FastAPI redirectt /mcp → /mcp/ wat de MCP-integratie breekt.
# RootApp onderschept /mcp vóór FastAPI dat doet.

class RootApp:
    def __init__(self, fastapi_app, mcp_handler):
        self._fastapi = fastapi_app
        self._mcp     = mcp_handler

    async def __call__(self, scope, receive, send) -> None:
        path = scope.get("path", "")
        if scope["type"] == "http" and path.rstrip("/") == "/mcp":
            await self._mcp(scope, receive, send)
        else:
            await self._fastapi(scope, receive, send)


# ── FastAPI app ───────────────────────────────────────────────────────────────

_fastapi  = FastAPI()
templates = Jinja2Templates(directory="templates")
templates.env.filters["from_json"] = json.loads

# Database initialiseren bij module-import
init_db()


# ── Admin authenticatie ───────────────────────────────────────────────────────

def get_admin_session(request: Request) -> str:
    token = request.cookies.get("admin_session", "")
    if not _is_valid_session(token):
        raise HTTPException(status_code=303, headers={"Location": "/admin/login"})
    return token


# ── Admin routes ──────────────────────────────────────────────────────────────

@_fastapi.get("/admin/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@_fastapi.post("/admin/login")
async def login(request: Request, password: str = Form(...)):
    ip  = request.client.host if request.client else "unknown"
    now = datetime.now()

    _failed_logins[ip] = [t for t in _failed_logins[ip] if now - t < LOCKOUT_WINDOW]

    if len(_failed_logins[ip]) >= LOCKOUT_ATTEMPTS:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Te veel mislukte pogingen — wacht 15 minuten.",
        })

    if secrets.compare_digest(password, ADMIN_PASSWORD):
        _failed_logins.pop(ip, None)
        session_token = _create_session()
        response = RedirectResponse("/admin", status_code=303)
        response.set_cookie(
            "admin_session", session_token,
            httponly=True, samesite="strict", secure=SECURE_COOKIES,
        )
        return response

    _failed_logins[ip].append(now)
    remaining = LOCKOUT_ATTEMPTS - len(_failed_logins[ip])
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": f"Verkeerd wachtwoord ({remaining} poging{'en' if remaining != 1 else ''} resterend).",
    })


@_fastapi.get("/admin/logout")
async def logout(request: Request):
    token = request.cookies.get("admin_session", "")
    _sessions.pop(token, None)
    response = RedirectResponse("/admin/login", status_code=303)
    response.delete_cookie("admin_session")
    return response


@_fastapi.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request, session: str = Depends(get_admin_session)):
    conn = _get_db()
    clients = conn.execute("SELECT * FROM clients ORDER BY created_at DESC").fetchall()
    conn.close()
    return templates.TemplateResponse("dashboard.html", {
        "request":         request,
        "clients":         clients,
        "all_collections": ALL_COLLECTIONS,
        "csrf_token":      _csrf_token(session),
        "public_url":      PUBLIC_URL,
    })


@_fastapi.get("/admin/client/new", response_class=HTMLResponse)
async def new_client_page(request: Request, session: str = Depends(get_admin_session)):
    return templates.TemplateResponse("client_form.html", {
        "request":         request,
        "all_collections": ALL_COLLECTIONS,
        "client":          None,
        "csrf_token":      _csrf_token(session),
    })


@_fastapi.post("/admin/client/new")
async def create_client(
    request:           Request,
    name:              str       = Form(...),
    email:             str       = Form(""),
    openwebui_api_key: str       = Form(...),
    openwebui_url:     str       = Form(...),
    collections:       list[str] = Form(default=[]),
    csrf_token:        str       = Form(...),
    session:           str       = Depends(get_admin_session),
):
    if not _verify_csrf(session, csrf_token):
        raise HTTPException(status_code=403, detail="Ongeldig CSRF-token")
    token = secrets.token_urlsafe(32)
    conn  = _get_db()
    conn.execute(
        "INSERT INTO clients"
        " (name, email, token, openwebui_api_key, openwebui_url, allowed_collections, created_at)"
        " VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name, email, token, openwebui_api_key, openwebui_url,
         json.dumps(collections), datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()
    return RedirectResponse("/admin", status_code=303)


@_fastapi.post("/admin/client/{client_id}/toggle")
async def toggle_client(
    client_id:  int,
    csrf_token: str = Form(...),
    session:    str = Depends(get_admin_session),
):
    if not _verify_csrf(session, csrf_token):
        raise HTTPException(status_code=403, detail="Ongeldig CSRF-token")
    conn = _get_db()
    conn.execute(
        "UPDATE clients SET is_active = CASE WHEN is_active = 1 THEN 0 ELSE 1 END WHERE id = ?",
        (client_id,),
    )
    conn.commit()
    conn.close()
    return RedirectResponse("/admin", status_code=303)


@_fastapi.post("/admin/client/{client_id}/delete")
async def delete_client(
    client_id:  int,
    csrf_token: str = Form(...),
    session:    str = Depends(get_admin_session),
):
    if not _verify_csrf(session, csrf_token):
        raise HTTPException(status_code=403, detail="Ongeldig CSRF-token")
    conn = _get_db()
    conn.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    conn.commit()
    conn.close()
    return RedirectResponse("/admin", status_code=303)


@_fastapi.post("/admin/client/{client_id}/rotate-token")
async def rotate_token(
    client_id:  int,
    csrf_token: str = Form(...),
    session:    str = Depends(get_admin_session),
):
    if not _verify_csrf(session, csrf_token):
        raise HTTPException(status_code=403, detail="Ongeldig CSRF-token")
    new_token = secrets.token_urlsafe(32)
    conn = _get_db()
    conn.execute("UPDATE clients SET token = ? WHERE id = ?", (new_token, client_id))
    conn.commit()
    conn.close()
    return RedirectResponse("/admin", status_code=303)


# ── Health check ──────────────────────────────────────────────────────────────

@_fastapi.get("/health")
async def health():
    return {"status": "ok", "service": "ICTRecht Knowledge MCP"}


# ── ASGI entry point ──────────────────────────────────────────────────────────
# RootApp onderschept /mcp vóór FastAPI's redirect-middleware.

app = RootApp(_fastapi, MCPHandler())
