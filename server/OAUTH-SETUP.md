# OAuth-pad — setup-runbook (Keycloak + Entra, klant kiest)

Resultaat: klanten klikken in Claude/ChatGPT/Copilot Studio op **Connect**, loggen in via
**Keycloak** óf **Microsoft Entra**, en bereiken jouw kennis via de gateway. De eigen
MCP-server en de OpenWebUI-API-key zijn afgeschermd.

```
Claude.ai / ChatGPT / Copilot Studio
        │  OAuth 2.1 (Connect → browser-login)
        ▼
  [nginx TLS]  mcp.jouwbedrijf.nl ─▶ ContextForge-gateway ──servicetoken (intern)──▶ eigen MCP-server ──API-key──▶ OpenWebUI
               idp.jouwbedrijf.nl ─▶ Keycloak                         (niet publiek)
        ▲
   login-keuze: [Keycloak] of [Microsoft Entra]
```

## 0. Voorbereiding
- DNS: `mcp.jouwbedrijf.nl` en `idp.jouwbedrijf.nl` → je host.
- TLS-cert in `nginx/certs/` (wildcard `*.jouwbedrijf.nl` is handig). Zie `nginx/README.md`.
- `cp .env.example .env`; genereer secrets:
  ```bash
  openssl rand -hex 32   # JWT_SECRET_KEY
  openssl rand -hex 32   # AUTH_ENCRYPTION_SECRET
  ```
- Pas in `.env` en `nginx/nginx.conf` `jouwbedrijf.nl` aan; vul `OPENWEBUI_*` in.

## 1. Servicetoken (gateway → eigen MCP-server)
De gateway praat intern met je MCP-server via één servicetoken:
```bash
docker compose build mcpserver
docker compose run --rm mcpserver python manage_tokens.py issue --label "ContextForge-gateway"
```
Zet de uitvoer in `.env` als `MCP_BACKEND_TOKEN=...`.

## 2. Stack starten
```bash
docker compose up -d
docker compose ps        # alles healthy?
```

## 3. Keycloak — niets in te richten (auto-import) ✅
De realm `mcp` met client `mcp-gateway`, rol/groep en korte token-TTL wordt **automatisch
geïmporteerd** bij de eerste start (`keycloak/realm-mcp.json`). Je hoeft dit dus niet handmatig
te bouwen. Twee dingen vooraf (zie [keycloak/README.md](keycloak/README.md)):
- Vervang in `realm-mcp.json` het domein `mcp.jouwbedrijf.nl` door je eigen MCP-domein.
- Zet hetzelfde client-secret in `realm-mcp.json` (`"secret"`) én in `.env`
  (`SSO_KEYCLOAK_CLIENT_SECRET`): `openssl rand -hex 24`.

Klanten toevoegen en toegang intrekken doe je daarna in de adminconsole —
zie **[CUSTOMER-ADMIN.md](CUSTOMER-ADMIN.md)**.

## 4. Microsoft Entra inrichten
In het Entra-portaal → **App registrations → New registration**:
1. Redirect URI (Web): `https://mcp.jouwbedrijf.nl/auth/sso/callback/entra`
2. Noteer **Application (client) ID** → `SSO_ENTRA_CLIENT_ID`, **Directory (tenant) ID** → `SSO_ENTRA_TENANT_ID`.
3. **Certificates & secrets → New client secret** → waarde → `SSO_ENTRA_CLIENT_SECRET`.
4. **API permissions**: `openid`, `profile`, `email` (Microsoft Graph, delegated).

> Beide providers uit? Zet `SSO_KEYCLOAK_ENABLED` of `SSO_ENTRA_ENABLED` op `false`.
> Na het wijzigen van `.env`: `docker compose up -d` om te herladen.

## 5. Eigen MCP-server registreren in de gateway
Admin-UI op `https://mcp.jouwbedrijf.nl` (eerste keer: lokale admin uit `.env`):
1. **Gateways/Servers → Add**: URL `http://mcpserver:8000/mcp`, transport **Streamable HTTP**.
2. Auth: **Bearer**, waarde = `MCP_BACKEND_TOKEN`.
3. Maak een **Virtual Server** die de tool `search_knowledge` aanbiedt en koppel toegang aan de gewenste rol/gebruikers (RBAC).

## 6. Clients koppelen (per klant, eenmalig)
De MCP-URL voor klanten is de **virtual-server-URL** uit de gateway, bv.
`https://mcp.jouwbedrijf.nl/servers/<id>/mcp`.
- **Claude.ai / ChatGPT (web)**: Settings → Connectors → *Add custom connector* → plak de URL → **Connect** → kies Keycloak/Entra → inloggen. Klaar; geen token plakken.
- **Copilot Studio**: voeg de MCP-server toe; OAuth 2.0 wordt door de connector afgehandeld.

## 7. Beheer & intrekken
- **Toegang per klant intrekken**: in de IdP (Keycloak: user disable; Entra: account/he toewijzing) of in de gateway-RBAC.
- **Servicetoken roteren**: nieuw token uitgeven (stap 1), `.env` bijwerken, server-registratie aanpassen, oud token `revoke`-en.

## 8. Vóór productie
Loop [`SECURITY-CHECKLIST.md`](SECURITY-CHECKLIST.md) af. Extra aandachtspunten OAuth-pad:
- Korte access-token-TTL; `REQUIRE_JTI=true`, `REQUIRE_TOKEN_EXPIRATION=true` (staan aan).
- `SSO_TRUSTED_DOMAINS` strikt; `SSO_AUTO_CREATE_USERS` bewust kiezen.
- Backups van `pgdata` én `kcdata` (Keycloak-realm/users) + geteste restore.
- Verifieer de upstream OpenWebUI-call in `server/openwebui_client.py` tegen jouw versie.
