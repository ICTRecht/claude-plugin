# Knowledge MCP-server — token-geauthenticeerd, OpenWebUI-kennis ontsloten

Een dunne, veilige MCP-server die jouw OpenWebUI-kennis ontsluit voor externe AI-tools
(Copilot Studio, Claude, ChatGPT). De **OpenWebUI-API-key blijft server-side** en gaat
nooit naar de client. Toegang vereist een **beheerbaar bearer-token** per klant.

## Hoe de beveiliging is geborgd (jouw doelen)

| Doel | Hoe |
|---|---|
| Validatie van elke aanroep | Bearer-token verplicht; ongeldig/ontbrekend → `401`, geen tooluitvoer (`server.py`) |
| API-key beschermd | Zit alleen in `openwebui_client.py` via env; nooit in responses, tools of logs |
| Niet benaderbaar voor derden | TLS-only (proxy) + default-deny token-auth + server niet direct gepubliceerd (alleen via proxy) |
| Gevoelige info onderweg | TLS afgedwongen; logs bevatten **geen** query-/antwoordinhoud, alleen token-id + status |
| Beheerbaar | `manage_tokens.py`: uitgeven / opsommen / intrekken; per token een vervaldatum |

## Tokens beheren

```bash
# Uitgeven (eenmalig zichtbaar — bewaar veilig en geef door aan de klant):
docker compose -f docker-compose.simple.yml run --rm mcpserver \
  python manage_tokens.py issue --label "Klant Acme" --ttl-days 90

# Opsommen (zonder geheime waarde):
docker compose -f docker-compose.simple.yml run --rm mcpserver \
  python manage_tokens.py list

# Intrekken:
docker compose -f docker-compose.simple.yml run --rm mcpserver \
  python manage_tokens.py revoke --id <token-id>
```

## Clients koppelen

De MCP-endpoint is `https://<jouw-domein>/mcp`.

### ✅ Microsoft Copilot Studio  (bearer-token werkt direct)
Voeg de MCP-server toe en kies **API key**-authenticatie, type **Header**:
`Authorization: Bearer <token>`.

### ✅ Claude Desktop / Claude Code  (bearer via headers)
```json
{
  "mcpServers": {
    "kennisbank": {
      "type": "http",
      "url": "https://<jouw-domein>/mcp",
      "headers": { "Authorization": "Bearer <token>" }
    }
  }
}
```

### ✅ ChatGPT desktop  (bearer via headers, vergelijkbaar)

### ⚠️ Claude.ai web-connector & ChatGPT web-connector  (vereisen OAuth 2.1)
De **web**-UI's van Claude.ai en ChatGPT accepteren géén statisch bearer-token; ze vereisen
de OAuth 2.1-flow uit de MCP-spec. Twee opties:
1. **Front met ContextForge** (`docker-compose.yml` in de bovenliggende map): die levert de
   OAuth-laag + tokenbeheer-UI; je MCP-server blijft hierachter ongewijzigd. *(Aanrader als je
   deze web-connectors per se nodig hebt.)*
2. **OAuth in de server bouwen** (authorization code + PKCE + protected-resource-metadata).
   Meer werk en eigen onderhoud.

> Bron-controle: bevestig per client de actuele auth-opties; deze veranderen snel.

## Belangrijk om te verifiëren vóór productie
- **Upstream-call** in `openwebui_client.py`: het exacte pad/payload kan per OpenWebUI-versie
  verschillen. Controleer tegen Swagger (`/docs` bij `ENV=dev`) en pas zo nodig aan.
- Loop [`../SECURITY-CHECKLIST.md`](../SECURITY-CHECKLIST.md) af (AUTH, INJ, DOS, LOG, PRIV).
