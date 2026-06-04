"""
ICTRecht Knowledge MCP Server — Horizon/FastMCP versie

Per-klant toegang wordt beheerd via Horizon RBAC (welke tools een klant mag aanroepen).
Configuratie via omgevingsvariabelen:
  OPENWEBUI_URL       — URL van de OpenWebUI instance
  OPENWEBUI_API_KEY   — API-sleutel voor OpenWebUI
  CHUNKS_PER_QUERY    — aantal fragmenten per zoekopdracht (standaard: 6)
"""

import os
import httpx
from fastmcp import FastMCP

mcp = FastMCP(
    name="ictrecht-knowledge",
    instructions=(
        "Je hebt toegang tot ICTRecht kennisbanken. Gebruik de zoektools om relevante "
        "juridische informatie op te halen. Verwerk de fragmenten zelf in je antwoord."
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
async def search_privacy_guide(query: str) -> str:
    """Zoek in de Privacy Guide v2 kennisbank (AVG, privacyrecht, verwerkersovereenkomsten)."""
    return await _search("b1c44172-86ba-4504-8b1a-6c58c8ea9120", "Privacy Guide v2", query)

@mcp.tool()
async def search_woo(query: str) -> str:
    """Zoek in de WOO kennisbank (Wet open overheid, openbaarheid van bestuur)."""
    return await _search("eb430eef-341c-463b-8ab2-9a1712bafb32", "WOO", query)

@mcp.tool()
async def search_ondernemingsrecht(query: str) -> str:
    """Zoek in de Ondernemingsrecht kennisbank."""
    return await _search("21982d73-9d75-434d-8c5b-24fcb5d6606d", "Ondernemingsrecht", query)

@mcp.tool()
async def search_onderwijsassistent(query: str) -> str:
    """Zoek in de Onderwijsassistent kennisbank (onderwijs en privacy)."""
    return await _search("de0e5e93-0acb-433c-a13a-7f3682c9f16a", "Onderwijsassistent", query)

@mcp.tool()
async def search_risico_assistent(query: str) -> str:
    """Zoek in de Risico Assistent kennisbank (DPIA, risicoanalyse)."""
    return await _search("3d8809ff-c0c1-4d78-947e-a084f425ef2d", "Risico Assistent", query)

@mcp.tool()
async def search_vso_checker(query: str) -> str:
    """Zoek in de VSO Checker kennisbank (vaststellingsovereenkomsten)."""
    return await _search("e344e0f3-d32a-4151-8238-00e1d5e2bf3a", "VSO Checker", query)

@mcp.tool()
async def search_wpg(query: str) -> str:
    """Zoek in de WPG kennisbank (Wet politiegegevens)."""
    return await _search("2254dc37-fa85-474b-9345-f5138bbd62cc", "WPG", query)

@mcp.tool()
async def search_zorgrecht(query: str) -> str:
    """Zoek in de Zorgrecht Guide kennisbank."""
    return await _search("af813a9e-7d21-4e98-bb4a-0e46695a746a", "Zorgrecht Guide", query)

@mcp.tool()
async def search_arbeidsovereenkomsten(query: str) -> str:
    """Zoek in de Arbeidsovereenkomsten Checker kennisbank."""
    return await _search("3538820f-87e6-45fb-bf27-65428a818200", "Arbeidsovereenkomsten Checker", query)

@mcp.tool()
async def search_ontslag(query: str) -> str:
    """Zoek in de Ontslag Assistent kennisbank."""
    return await _search("0ba17aec-794c-4149-9dd6-379712dc25a7", "Ontslag Assistent", query)

@mcp.tool()
async def search_wet_dba(query: str) -> str:
    """Zoek in de Wet DBA Guide kennisbank (zelfstandigen, zzp)."""
    return await _search("387ece26-3cb4-4efd-b809-691645bb86bb", "Wet DBA Guide", query)

@mcp.tool()
async def search_gegevensverwerking(query: str) -> str:
    """Zoek in de Gegevensverwerking Assistent kennisbank."""
    return await _search("2f3b3297-a449-4848-b38b-44cf61d58c2a", "Gegevensverwerking Assistent", query)
