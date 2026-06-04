"""
ICTRecht Knowledge MCP Server — Horizon/FastMCP versie

Per-klant toegang wordt beheerd via Horizon RBAC (welke tools een klant mag aanroepen).
Configuratie via omgevingsvariabelen:
  OPENWEBUI_URL       — URL van de OpenWebUI instance (bijv. https://ai.ictrecht.nl)
  OPENWEBUI_API_KEY   — API-sleutel voor OpenWebUI
  CHUNKS_PER_QUERY    — aantal fragmenten per zoekopdracht (standaard: 6)
"""

import os
import httpx
from fastmcp import FastMCP

mcp = FastMCP(
    name="ictrecht-knowledge",
    instructions=(
        "Je hebt toegang tot ICTRecht privacy- en gegevensbeschermingskennisbanken. "
        "Gebruik de zoektools om relevante juridische informatie op te halen en "
        "verwerk de fragmenten zelf in je antwoord."
    ),
)

OPENWEBUI_URL     = os.getenv("OPENWEBUI_URL", "").rstrip("/")
OPENWEBUI_API_KEY = os.getenv("OPENWEBUI_API_KEY", "")
CHUNKS            = int(os.getenv("CHUNKS_PER_QUERY", "6"))


async def _search(collection_id: str, collection_name: str, query: str) -> str:
    """Haalt documentfragmenten op uit OpenWebUI via vector search (geen LLM)."""
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            f"{OPENWEBUI_URL}/api/v1/knowledge/{collection_id}/query",
            headers={"Authorization": f"Bearer {OPENWEBUI_API_KEY}"},
            json={"query": query, "k": CHUNKS},
        )
        r.raise_for_status()
        data = r.json()

    lines = [f"## Kennisbank: {collection_name}\n"]
    for result in data.get("results", []):
        docs  = result.get("documents", [])
        metas = result.get("metadatas", [])
        dists = result.get("distances", [])
        for i, text in enumerate(docs):
            meta = metas[i] if i < len(metas) else {}
            dist = dists[i] if i < len(dists) else None
            ref  = meta.get("name") or meta.get("source", "onbekend")
            if meta.get("page_label") or meta.get("page"):
                ref += f", p. {meta.get('page_label') or meta.get('page')}"
            if dist is not None:
                ref += f" (relevantie: {round(1 - float(dist), 3)})"
            lines += [f"**{ref}**", text.strip(), ""]

    return "\n".join(lines) if len(lines) > 1 else f"*{collection_name}* — geen relevante fragmenten gevonden."


# ── Tools — één per kennisbank ────────────────────────────────────────────────
# Horizon RBAC bepaalt welke tools een klant mag aanroepen.

@mcp.tool()
async def search_avg_rechten(query: str) -> str:
    """Zoek in de AVG-Rechten Assistent kennisbank (rechten van betrokkenen, inzage, bezwaar)."""
    return await _search("376ab8c4-d17a-40c4-9031-45668128d27a", "AVG-Rechten Assistent", query)

@mcp.tool()
async def search_privacy_guide(query: str) -> str:
    """Zoek in de Privacy Guide V2 kennisbank (AVG, privacyrecht, verwerkersovereenkomsten)."""
    return await _search("b1c44172-86ba-4504-8b1a-6c58c8ea9120", "Privacy Guide V2", query)

@mcp.tool()
async def search_datalekken(query: str) -> str:
    """Zoek in de Beoordelingsassistent Datalekken kennisbank (meldplicht, beoordeling datalekken)."""
    return await _search("e89f6432-124c-421f-ac93-6b83c3ce37b4", "Beoordelingsassistent Datalekken", query)

@mcp.tool()
async def search_data_act(query: str) -> str:
    """Zoek in de Data Act Guide kennisbank (EU Data Act, dataverordening)."""
    return await _search("41f69cc8-8f94-436c-95f1-e8939e7dfcb5", "Data Act Guide", query)

@mcp.tool()
async def search_wpg(query: str) -> str:
    """Zoek in de WPG kennisbank (Wet politiegegevens)."""
    return await _search("2254dc37-fa85-474b-9345-f5138bbd62cc", "WPG", query)

@mcp.tool()
async def search_gegevensverwerking(query: str) -> str:
    """Zoek in de Gegevensverwerking Assistent kennisbank (grondslagen, verwerkingsregister)."""
    return await _search("2f3b3297-a449-4848-b38b-44cf61d58c2a", "Gegevensverwerking Assistent", query)

@mcp.tool()
async def search_dpia(query: str) -> str:
    """Zoek in de DPIA Assistent kennisbank (gegevensbeschermingseffectbeoordeling)."""
    return await _search("6ea95c7b-0e2c-4efd-ac84-bd7a96fc9356", "DPIA Assistent", query)

@mcp.tool()
async def search_doorgifte(query: str) -> str:
    """Zoek in de Doorgifte Assistent AVG kennisbank (internationale doorgifte, SCCs, adequaatheid)."""
    return await _search("a7280324-a663-4c80-b056-ae42fc223abc", "Doorgifte Assistent AVG", query)
