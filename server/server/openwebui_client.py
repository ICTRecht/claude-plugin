"""Thin adapter naar OpenWebUI. De OpenWebUI-API-key zit ALLEEN hier en verlaat de server nooit.

Gebruikt de gedocumenteerde RAG-route van OpenWebUI: een chat-completion die een
kennis-collectie als `files`-referentie meekrijgt, zodat OpenWebUI's retrieval-pipeline
relevante passages ophaalt en een gegrond antwoord teruggeeft.

LET OP: bevestig het exacte pad/payload tegen JOUW OpenWebUI-versie (Swagger op /docs bij ENV=dev).
"""
import httpx

import config

_HEADERS = {
    "Authorization": f"Bearer {config.OPENWEBUI_API_KEY}",
    "Content-Type": "application/json",
}


async def search_knowledge(query: str) -> str:
    payload = {
        "model": config.OPENWEBUI_MODEL,
        "messages": [{"role": "user", "content": query}],
        "files": [{"type": "collection", "id": config.OPENWEBUI_KNOWLEDGE_ID}],
        "stream": False,
    }
    url = f"{config.OPENWEBUI_BASE_URL}/api/chat/completions"
    async with httpx.AsyncClient(timeout=config.UPSTREAM_TIMEOUT) as client:
        resp = await client.post(url, headers=_HEADERS, json=payload)
        resp.raise_for_status()
        data = resp.json()
    # Gangbare OpenAI-compatibele vorm:
    return data["choices"][0]["message"]["content"]
