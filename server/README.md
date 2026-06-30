# MCP-server — veilig, zelf-hostbaar, token-geauthenticeerd

**Doel.** Klanten benaderen jullie OpenWebUI-kennis via een MCP-server, aanroepbaar vanuit
externe AI-tools (Claude, ChatGPT, Copilot Studio). Eisen: **validatie per aanroep**, de
**OpenWebUI-API-key blijft beschermd** (server-side), de server is **op geen enkele manier
benaderbaar voor derden**, en er gaat **gevoelige informatie** doorheen.

## Twee paden in deze map

| | **OAuth-pad** ⭐ gebruiksvriendelijk + superveilig | **Simpel pad** (minimale infra) |
|---|---|---|
| Map/compose | [`docker-compose.yml`](docker-compose.yml) (ContextForge + Keycloak) | [`server/`](server/) + [`docker-compose.simple.yml`](docker-compose.simple.yml) |
| Auth | OAuth 2.1: klant klikt **Connect** → login via **Keycloak óf Entra** (kiest zelf) | Beheerbaar **bearer-token** per klant |
| Werkt met | **Alles**: Claude.ai/ChatGPT **web** ✅ + Copilot Studio ✅ + desktop ✅ | Copilot Studio ✅, desktop ✅ — **web-connectors niet** |
| Veiligheid | Kortlevende tokens, PKCE, per-gebruiker, centrale revocatie | Langlevend statisch geheim (hashed, TLS, vervaldatum) |
| Infra | Gateway + Postgres + Redis + Keycloak | Alleen server + TLS-proxy |
| Setup | [OAUTH-SETUP.md](OAUTH-SETUP.md) | [server/README.md](server/README.md) |

> **Aanbevolen: het OAuth-pad.** Het is voor de klant juist makkelijker (browser-login, geen
> token plakken) én veiliger (korte tokens, geen rondslingerend statisch geheim). De eigen
> MCP-server (hieronder) blijft ongewijzigd en staat **network-isolated** achter de gateway.
> Het simpele pad blijft beschikbaar als je alleen Copilot Studio/desktop bedient en minimale
> infra wilt. In beide gevallen blijft de OpenWebUI-API-key server-side.

## Het simpele pad in het kort
- [`server/server.py`](server/server.py) — MCP-server (streamable HTTP) met bearer-auth-gate (default-deny, 401 zonder geldig token), audit-log zonder PII.
- [`server/tokens.py`](server/tokens.py) + [`server/manage_tokens.py`](server/manage_tokens.py) — beheerbare tokens (uitgeven/opsommen/intrekken, vervaldatum); alleen de **hash** wordt opgeslagen.
- [`server/openwebui_client.py`](server/openwebui_client.py) — adapter die de **OpenWebUI-API-key server-side houdt**.
- TLS + security headers via [`nginx/nginx.simple.conf`](nginx/nginx.simple.conf).

```bash
cd MCP-server && cp .env.example .env        # vul OPENWEBUI_* + zet TLS-cert (nginx/README.md)
docker compose -f docker-compose.simple.yml build
docker compose -f docker-compose.simple.yml run --rm mcpserver \
  python manage_tokens.py issue --label "Klant X" --ttl-days 90   # token -> aan klant geven
docker compose -f docker-compose.simple.yml up -d
```

---

## Achtergrond: de gateway-/RBAC-optie

De onderstaande opzet plaatst je MCP-server áchter een gehardende gateway die authenticatie,
autorisatie (RBAC), rate limiting, auditing en OAuth centraliseert. Relevant zodra je
web-connectors of fijnmazige RBAC nodig hebt.

## Aanbevolen bouwsteen (open source)

**[IBM ContextForge MCP Gateway](https://github.com/IBM/mcp-context-forge)** als beheer-/
gatewaylaag. Waarom dit de beste keuze is voor jouw situatie:

| Eis | ContextForge |
|---|---|
| Open source, zelf-hostbaar | ✅ Apache-2.0, Docker/Compose/Helm |
| RBAC-beheer (rollen, teams, scopes) | ✅ Ingebouwd: RBAC-API, admin-UI, Cedar-plugin, per-server API-keys |
| Past op jouw stack | ✅ Python/FastAPI (net als je bestaande `main.py`/RAG) |
| Veiligheid by default | ✅ SSRF strict, token scoping default-deny, OAuth-secret-encryptie, JTI-revocatie, sessie-ownership (40+ controls) |
| Betrouwbaarheid | ✅ Federatie, HA-replicas, Postgres+Redis, health checks |
| Mapt op het testplan | ✅ Dekt AUTH-, INJ-, SUP-, LOG-, DOS-categorieën aan de gatewayrand |

Het mapt direct op de bijlage (`Testplan_MCP_RAG_beveiliging.md`).

### Alternatieven (en wanneer)
- **[agentgateway](https://github.com/agentgateway/agentgateway)** (Linux Foundation/Solo.io) — Rust data-plane, Cedar-RBAC, JWT/OAuth, OTel. Kies dit als je een infra-grade proxy wilt i.p.v. een beheer-UI/registry.
- **[Obot](https://obot.ai)** — kant-en-klare MCP-governance met catalogus + RBAC + audit.
- **[Lasso open-source MCP gateway](https://github.com/lasso-security)** — sterk in *content-inspectie* (prompt-injection-detectie, secret-patronen). **Aanbevolen als aanvullende laag** (zie PLAN.md, defense-in-depth).
- **[Docker MCP Gateway](https://github.com/docker)** — container-isolatie per MCP-server.

## ⚠️ Kerninzicht: RBAC is twee lagen

De gateway-RBAC bepaalt **wié welke tools mag aanroepen** (grofkorrelig). Dat is **niet
genoeg** voor RAG. De meest voorkomende RAG-faalfout (zie bijlage §2.4) is *over-retrieval*:
een gebruiker mag de zoektool aanroepen, maar krijgt chunks te zien die hij niet mag zien.

Daarom **twee lagen**:
1. **Gateway-RBAC** (ContextForge) — authN + welke tools/servers per principal.
2. **Data-autorisatie in de RAG-backend** — welke documenten/chunks per gebruiker, afgedwongen op de backend (pgvector RLS / server-side metadatafilters), met **identiteit doorgegeven vanuit de gateway**. Filters nooit uit gebruikersinvoer.

Zie [PLAN.md](PLAN.md) §3 voor het volledige model.

## Bestanden
- [PLAN.md](PLAN.md) — het volledige betrouwbaarheids- en veiligheidsplan + roadmap.
- [SECURITY-CHECKLIST.md](SECURITY-CHECKLIST.md) — gehardende config gemapt op de testplan-ID's.
- [docker-compose.yml](docker-compose.yml) — hostbare stack (gateway + Postgres + Redis + TLS-reverse-proxy).
- [.env.example](.env.example) — gehardende omgevingsvariabelen (kopieer naar `.env`).
- [nginx/](nginx/) — TLS-terminatie + security headers.

## Snelstart (lokaal, voor evaluatie)
```bash
cd "MCP-server"
cp .env.example .env
# 1) Genereer secrets en vul ze in .env:
openssl rand -hex 32   # -> JWT_SECRET_KEY
openssl rand -hex 32   # -> AUTH_ENCRYPTION_SECRET
# 2) Zet een sterk PLATFORM_ADMIN_PASSWORD in .env
docker compose up -d
# Admin-UI: https://localhost (via nginx) — log in met PLATFORM_ADMIN_EMAIL
```
> ⚠️ De compose-file is een **hardened startpunt**, geen kant-en-klare productie. Werk
> [SECURITY-CHECKLIST.md](SECURITY-CHECKLIST.md) en de roadmap in [PLAN.md](PLAN.md) af
> vóór productie. Pin het image op de actueel laatste **stable** release.
