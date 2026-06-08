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
from starlette.requests import Request
from starlette.responses import JSONResponse

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

ALL_COLLECTIONS = {
    "AVG-Rechten Assistent":          "376ab8c4-d17a-40c4-9031-45668128d27a",
    "Privacy Guide V2":               "b1c44172-86ba-4504-8b1a-6c58c8ea9120",
    "Beoordelingsassistent Datalekken": "e89f6432-124c-421f-ac93-6b83c3ce37b4",
    "Data Act Guide":                 "41f69cc8-8f94-436c-95f1-e8939e7dfcb5",
    "WPG":                            "2254dc37-fa85-474b-9345-f5138bbd62cc",
    "Gegevensverwerking Assistent":   "2f3b3297-a449-4848-b38b-44cf61d58c2a",
    "DPIA Assistent":                 "6ea95c7b-0e2c-4efd-ac84-bd7a96fc9356",
    "Doorgifte Assistent AVG":        "a7280324-a663-4c80-b056-ae42fc223abc",
}


async def _search(collection_id: str, collection_name: str, query: str) -> str:
    """Haalt documentfragmenten op uit OpenWebUI via vector search (geen LLM)."""
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            f"{OPENWEBUI_URL}/api/v1/retrieval/query/doc",
            headers={"Authorization": f"Bearer {OPENWEBUI_API_KEY}"},
            json={"collection_name": collection_id, "query": query, "k": CHUNKS},
        )
        r.raise_for_status()
        data = r.json()

    docs  = data.get("documents",  [[]])[0]
    metas = data.get("metadatas",  [[]])[0]
    dists = data.get("distances",  [[]])[0]

    if not docs:
        return f"*{collection_name}* — geen relevante fragmenten gevonden."

    lines = [f"## Kennisbank: {collection_name}\n"]
    for i, text in enumerate(docs):
        meta = metas[i] if i < len(metas) else {}
        dist = dists[i] if i < len(dists) else None
        source = meta.get("name") or meta.get("source", "onbekend")
        source = source.removesuffix(".json")
        if dist is not None:
            source += f" (relevantie: {round(1 - float(dist), 3)})"
        lines += [f"**{source}**", text.strip(), ""]

    return "\n".join(lines)


# ── REST endpoint voor Custom GPT / externe integraties ───────────────────────
# Geen API-sleutel nodig — OpenWebUI credentials blijven server-side.

@mcp.custom_route("/api/search", methods=["POST"])
async def api_search(request: Request) -> JSONResponse:
    """
    REST endpoint voor ChatGPT Custom GPT Actions en andere REST-clients.
    Body: { "collection": "<naam>", "query": "<vraag>", "k": 6 }
    """
    try:
        data = await request.json()
    except Exception:
        return JSONResponse({"error": "Ongeldige JSON"}, status_code=400)

    collection_name = data.get("collection", "")
    query           = str(data.get("query", ""))[:2000]
    k               = int(data.get("k", CHUNKS))

    if not collection_name or not query:
        return JSONResponse(
            {"error": "Vereiste velden ontbreken: 'collection' en 'query'",
             "beschikbare_kennisbanken": list(ALL_COLLECTIONS.keys())},
            status_code=400,
        )

    collection_id = ALL_COLLECTIONS.get(collection_name)
    if not collection_id:
        return JSONResponse(
            {"error": f"Onbekende kennisbank: '{collection_name}'",
             "beschikbare_kennisbanken": list(ALL_COLLECTIONS.keys())},
            status_code=404,
        )

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                f"{OPENWEBUI_URL}/api/v1/retrieval/query/doc",
                headers={"Authorization": f"Bearer {OPENWEBUI_API_KEY}"},
                json={"collection_name": collection_id, "query": query, "k": k},
            )
            r.raise_for_status()
            data = r.json()

        docs  = data.get("documents",  [[]])[0]
        metas = data.get("metadatas",  [[]])[0]
        dists = data.get("distances",  [[]])[0]

        results = []
        for i, text in enumerate(docs):
            meta = metas[i] if i < len(metas) else {}
            dist = dists[i] if i < len(dists) else None
            source = (meta.get("name") or meta.get("source", "onbekend")).removesuffix(".json")
            results.append({
                "tekst":     text.strip(),
                "bron":      source,
                "relevantie": round(1 - float(dist), 3) if dist is not None else None,
            })

        return JSONResponse({"kennisbank": collection_name, "fragmenten": results})

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# ── MCP Tools — één per kennisbank ───────────────────────────────────────────

@mcp.tool()
async def search_avg_rechten(query: str) -> str:
    """Zoek in de AVG-Rechten Assistent kennisbank (rechten van betrokkenen, inzage, bezwaar)."""
    return await _search(ALL_COLLECTIONS["AVG-Rechten Assistent"], "AVG-Rechten Assistent", query)

@mcp.tool()
async def search_privacy_guide(query: str) -> str:
    """Zoek in de Privacy Guide V2 kennisbank (AVG, privacyrecht, verwerkersovereenkomsten)."""
    return await _search(ALL_COLLECTIONS["Privacy Guide V2"], "Privacy Guide V2", query)

@mcp.tool()
async def search_datalekken(query: str) -> str:
    """Zoek in de Beoordelingsassistent Datalekken kennisbank (meldplicht, beoordeling datalekken)."""
    return await _search(ALL_COLLECTIONS["Beoordelingsassistent Datalekken"], "Beoordelingsassistent Datalekken", query)

@mcp.tool()
async def search_data_act(query: str) -> str:
    """Zoek in de Data Act Guide kennisbank (EU Data Act, dataverordening)."""
    return await _search(ALL_COLLECTIONS["Data Act Guide"], "Data Act Guide", query)

@mcp.tool()
async def search_wpg(query: str) -> str:
    """Zoek in de WPG kennisbank (Wet politiegegevens)."""
    return await _search(ALL_COLLECTIONS["WPG"], "WPG", query)

@mcp.tool()
async def search_gegevensverwerking(query: str) -> str:
    """Zoek in de Gegevensverwerking Assistent kennisbank (grondslagen, verwerkingsregister)."""
    return await _search(ALL_COLLECTIONS["Gegevensverwerking Assistent"], "Gegevensverwerking Assistent", query)

@mcp.tool()
async def search_dpia(query: str) -> str:
    """Zoek in de DPIA Assistent kennisbank (gegevensbeschermingseffectbeoordeling)."""
    return await _search(ALL_COLLECTIONS["DPIA Assistent"], "DPIA Assistent", query)

@mcp.tool()
async def search_doorgifte(query: str) -> str:
    """Zoek in de Doorgifte Assistent AVG kennisbank (internationale doorgifte, SCCs, adequaatheid)."""
    return await _search(ALL_COLLECTIONS["Doorgifte Assistent AVG"], "Doorgifte Assistent AVG", query)
