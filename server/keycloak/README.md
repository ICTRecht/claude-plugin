# Keycloak realm — kant-en-klaar (auto-import)

`realm-mcp.json` wordt **automatisch geïmporteerd** bij de eerste start van de
Keycloak-container (zie `command: ["start", "--import-realm"]` in `docker-compose.yml`).
Daarna staat alles klaar; je hoeft alleen nog klanten toe te voegen.

## Wat er vooraf is ingericht
| Onderdeel | Waarde | Doel |
|---|---|---|
| Realm | `mcp` | Aparte omgeving voor klanttoegang |
| Client | `mcp-gateway` (confidential, PKCE S256) | OAuth-client voor de gateway |
| Rol | `mcp-access` | "Mag de kennisbank gebruiken" |
| Groep | `mcp-klanten` (krijgt `mcp-access`) | Lidmaatschap = toegang |
| Default groep | `mcp-klanten` | Nieuwe gebruiker krijgt direct toegang |
| Access-token-TTL | 5 min | Intrekken werkt vrijwel direct |
| Wachtwoordbeleid | min. 12 tekens, hoofdletter+cijfer | Basishygiëne |
| Brute-force-bescherming | aan | Tegen wachtwoord-gokken |

## Twee dingen aanpassen vóór de eerste start
1. **Domein:** vervang in `realm-mcp.json` alle `mcp.jouwbedrijf.nl` door je eigen MCP-domein.
2. **Client-secret:** genereer één geheim en zet het op **twee** plekken (moet gelijk zijn):
   ```bash
   openssl rand -hex 24
   ```
   - in `realm-mcp.json` → veld `"secret"`
   - in `.env` → `SSO_KEYCLOAK_CLIENT_SECRET`

> Realm al eens geïmporteerd en je wijzigt het JSON-bestand? Een herstart importeert niet
> opnieuw over een bestaande realm heen. Verwijder dan eerst de realm in de console, of leeg
> het `kcdata`-volume (`docker compose down -v` wist álle data — voorzichtig).

Beheer van klanten (toevoegen / intrekken): zie [../CUSTOMER-ADMIN.md](../CUSTOMER-ADMIN.md).
