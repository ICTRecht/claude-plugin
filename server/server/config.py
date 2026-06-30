"""Centrale configuratie via omgevingsvariabelen. Geen secrets in code."""
import os


def _required(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        raise RuntimeError(f"Verplichte omgevingsvariabele ontbreekt: {name}")
    return val


# --- Upstream: OpenWebUI (de API-key blijft HIER, server-side, en lekt nooit naar clients) ---
OPENWEBUI_BASE_URL = _required("OPENWEBUI_BASE_URL").rstrip("/")
OPENWEBUI_API_KEY = _required("OPENWEBUI_API_KEY")
# ID van de kennis-collectie in OpenWebUI waarop gezocht wordt:
OPENWEBUI_KNOWLEDGE_ID = _required("OPENWEBUI_KNOWLEDGE_ID")
# Model dat OpenWebUI gebruikt om het gegronde antwoord te genereren:
OPENWEBUI_MODEL = _required("OPENWEBUI_MODEL")
UPSTREAM_TIMEOUT = float(os.environ.get("UPSTREAM_TIMEOUT", "30"))

# --- MCP-server ---
MCP_HOST = os.environ.get("MCP_HOST", "0.0.0.0")
MCP_PORT = int(os.environ.get("MCP_PORT", "8000"))

# --- Tokenopslag (volume-gemount voor persistentie) ---
TOKEN_DB_PATH = os.environ.get("TOKEN_DB_PATH", "/data/tokens.db")
