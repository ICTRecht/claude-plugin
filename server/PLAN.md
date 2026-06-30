# Plan — betrouwbare, veilige, zelf-gehoste MCP-gateway met RBAC

Dit plan maakt de keten uit de bijlage (`Testplan_MCP_RAG_beveiliging.md`) concreet
inrichtbaar. Het is bewust geordend van architectuur → autorisatie → hardening →
betrouwbaarheid → privacy → testen, zodat elke laag aantoonbaar geborgd wordt.

---

## 1. Doelarchitectuur

```
                          ┌──────────────────────────────────────────┐
  Eindgebruiker / Agent   │            Vertrouwde zone (jij host)      │
        │ HTTPS + OAuth/JWT│                                          │
        ▼                  │   ┌────────────────────────────────┐     │
   [nginx/Caddy TLS] ──────┼──▶│  ContextForge MCP-Gateway       │     │
   (terminatie,            │   │  • AuthN (OAuth/OIDC, JWT)      │     │
    security headers,      │   │  • RBAC (rollen/teams/scopes)   │     │
    rate limit L7)         │   │  • Rate limit / quota           │     │
                           │   │  • SSRF-allowlist, input-limits │     │
                           │   │  • Audit-log + OTel             │     │
                           │   └──────┬─────────────────┬────────┘     │
                           │          │ identiteit       │ (mTLS/intern)│
                           │          ▼ doorgegeven       ▼              │
                           │   ┌─────────────────┐  ┌──────────────┐    │
                           │   │ RAG-MCP-server  │  │ andere MCP-   │    │
                           │   │ (jouw tools)    │  │ servers       │    │
                           │   └───┬────────┬────┘  └──────────────┘    │
                           │       │        │                           │
                           │       ▼        ▼                           │
                           │  Embedding   Vectorstore (pgvector +       │
                           │   -API        RLS / metadatafilters)       │
                           └──────────────────────────────────────────┘
                                          │ (egress-allowlist)
                                          ▼
                                   LLM-provider (extern/lokaal)
```

**Componenten en verantwoordelijkheid**
- **Reverse proxy (nginx/Caddy):** TLS, HSTS/security headers, L7-rate-limit, geen klare tekst (testplan AUTH-04).
- **ContextForge-gateway:** authN, **RBAC**, rate limiting, auditing, SSRF-defaults, token-revocatie. Eén governance-punt voor álle MCP-tools.
- **RAG-MCP-server (jouw code):** biedt de retrieval-/zoektools aan; dwingt **data-autorisatie** af op basis van de doorgegeven identiteit.
- **Vectorstore + embedding:** isoleren in privénetwerk; nooit publiek bereikbaar (EXFIL-03).
- **Secret-store:** Vault/SOPS/Docker-secrets — nooit in code, prompts of tooldescripties.

---

## 2. Aanbevolen software (open source) — verantwoording

**Primair: IBM ContextForge MCP Gateway** (`ghcr.io/ibm/mcp-context-forge`).
- Ingebouwde **RBAC** (rol-management-API + admin-UI + Cedar-policy-plugin), teams, per-virtual-server API-keys, default-deny token-scoping.
- Productiehardening: SSRF strict defaults, OIDC `id_token`-verificatie, OAuth-secret at-rest-encryptie, JTI-revocatie, sessie-ownership, content-size-limieten.
- Federatie + HA-replicas + Postgres/Redis → betrouwbaarheid.
- Python/FastAPI → sluit aan op je bestaande stack.

**Aanvullend (defense-in-depth):**
- **Lasso open-source MCP gateway** of een eigen guardrail-plugin als **prompt-injection-/content-inspectielaag** vóór de modelcontext (testplan PI-*, EXFIL-*). ContextForge ondersteunt plugins/guardrails hiervoor.
- **agentgateway** als je later een Rust data-plane wilt naast/voor de beheerlaag.

> Houd altijd een **eigen, dunne RAG-MCP-server** in beheer: alleen de gateway erbuiten plaatsen lost data-autorisatie (laag 2) niet op.

---

## 3. RBAC in twee lagen (het belangrijkste ontwerp)

De bijlage noemt *confused deputy* en *over-retrieval* (§2.1, §2.4) als kernrisico's.
Eén RBAC-laag dekt dat niet. Daarom:

### Laag 1 — Gateway-RBAC (ContextForge): *wie mag welke tool?*
- Definieer **rollen** (bv. `viewer`, `analyst`, `admin`) en **teams/tenants**.
- Koppel rollen aan **virtual servers/tools** met **least privilege** (testplan AUTH-03).
- AuthN via **OAuth/OIDC** (Keycloak/Entra/Auth0); tokens met **audience + issuer-validatie**, korte TTL, **JTI** voor revocatie (AUTH-02).
- Geen anonieme toegang; default-deny (AUTH-01).

### Laag 2 — Data-autorisatie in de RAG-backend: *welke documenten/chunks?*
Dit is de laag die over-retrieval voorkomt en die je zelf moet bouwen:
1. **Identiteit doorgeven:** de gateway geeft de geverifieerde gebruikersidentiteit (JWT-claims / `X-Authenticated-User` header, intern via mTLS) door aan de RAG-MCP-server. De RAG-server vertrouwt **nooit** een door het model/gebruiker meegegeven `user_id` of filter.
2. **Server-side filters:** retrieval-filters (tenant, afdeling, toegangsniveau) worden **server-side** afgeleid uit die identiteit, niet uit toolargumenten (voorkomt filter-injectie, AUTHZ-04).
3. **Row Level Security in pgvector/Supabase:** RLS-policies binden elke `similarity_search` aan de rol/tenant van de aanvragende gebruiker. De DB dwingt af, niet de applicatie alleen (AUTHZ-04).
4. **Per-chunk herkomst & toegangsniveau** in metadata; rechten-intrekking propageert direct naar de index (AUTHZ-05, POIS-04).

> Acceptatietest: een laag-geprivilegieerde gebruiker die een query stelt die een
> **canary-token** in een beperkt document zou ophalen, mag die canary **nergens** terugzien
> (AUTHZ-02, EXFIL-04).

### Confused deputy expliciet vermijden
De RAG-server praat met de vectorstore **namens de gebruiker**, niet met één almachtig
serviceaccount dat alles mag. Of: het serviceaccount mag alles, maar de **RLS-context**
wordt per request op de gebruiker gezet (`SET LOCAL` / scoped connection).

---

## 4. Veiligheidshardening (gemapt op de bijlage)

Volledige config in [SECURITY-CHECKLIST.md](SECURITY-CHECKLIST.md). Kernmaatregelen:

| Risico (bijlage) | Maatregel | Laag |
|---|---|---|
| §2.1 Auth/transport | OAuth/OIDC, JWT (aud/iss/exp/JTI), TLS-only, mTLS intern | Gateway/proxy |
| §2.2 Tool-poisoning / rug-pull / shadowing | Alleen gereviewde, gepinde servers; toolwijziging vereist herbevestiging; naamconflict-detectie; tooldescripties scannen | Gateway + governance |
| §2.3 Injectie (cmd/SQL/path/SSRF) | Strikte schema-validatie, geparametriseerde queries, path-allowlist, **SSRF-allowlist** (blokkeer `169.254.169.254`, RFC1918, localhost) | RAG-server + gateway |
| §2.4 Over-retrieval/tenant-bypass | Twee-lagen-RBAC + RLS (zie §3) | RAG-backend |
| §2.5 Indirecte prompt-injection | Content-inspectielaag, instructie-/datascheiding, verborgen-tekst-normalisatie (zero-width/HTML-comment stripping), spotlighting/delimiting van chunks | RAG-server + guardrail |
| §2.6 Exfiltratie | Output-sanitisatie: blokkeer/relativeer externe afbeeldingen & data-dragende URL's; vectorstore niet publiek | RAG-server + client |
| §2.7 Privacy/AVG | PII-gate (BSN-elfproef/IBAN/gezondheid) vóór externe doorgifte; dataminimalisatie; VOK/DPIA | RAG-server + governance |
| §2.8 DoS/kosten | Rate limiting per gebruiker/tenant, token-/kostenplafond, contextbegrenzing, fail-safe degradatie | Gateway + RAG-server |
| §2.9 Supply chain | Gepinde lockfiles, SCA-scan, signature-verificatie, minimale host-rechten | CI + runtime |
| §2.10 Logging als risico | Gestructureerde audit-log met **PII-maskering**, strikte logtoegang, retentie | Observability |

---

## 5. Betrouwbaarheid & hosting

**Hosting-pad**
1. **Start:** één gehardende VM met `docker compose` (deze repo). Geschikt voor pilot.
2. **Schaal:** Kubernetes + Helm; ≥2 gateway-replicas, Postgres (HA), Redis-sentinel/cluster.

**Betrouwbaarheidsmaatregelen**
- **HA:** meerdere gateway-replicas achter de reverse proxy; health checks + auto-restart.
- **Stateful laag:** Postgres voor configuratie/RBAC; Redis voor sessies/cache. Beide met **backups** + getest **restore** (DR-runbook).
- **Fail-safe:** valt de vectorstore of LLM uit, dan **nette foutmelding zonder lek**, geen open fallback (testplan DOS-03).
- **Rate limiting & quota:** per gebruiker/tenant; token-/kostenplafond stopt uitloop (DOS-01/02/04).
- **Contextbegrenzing:** harde limiet op aantal/grootte chunks en promptgrootte (`CONTENT_MAX_*`).
- **Secret-rotatie:** JWT/encryptie-secrets roteerbaar; korte token-TTL.
- **Configuratie als code:** RBAC-rollen, virtual servers en policies versiebeheren.

**SLO-suggesties (vul aan):** beschikbaarheid 99,5%; p95-latentie < X s; foutbudget bewaakt via OTel/alerting.

---

## 6. Observability, canary & incident response

- **Audit-trail:** elke toolaanroep + retrieval + identiteit, manipulatiebestendig (append-only / WORM), strikt toegankelijk (LOG-01, LOG-04).
- **PII-maskering** in logs; expliciete retentie (PRIV-03).
- **Canary-/honeytokens** per toegangsniveau/tenant in de index; monitor model-output, egress en logs continu; elke hit buiten het geautoriseerde pad → alert + incidentprocedure (bijlage §5, LOG-02/03).
- **Datalek-runbook:** detectie → beoordeling meldplicht (AP/betrokkenen) → afhandeling. Sluit aan op de aanwezige ICTRecht-privacy-skill (`datalek`).

---

## 7. Privacy & AVG

De query en chunks reizen langs embedding-API, vectorstore en LLM — elk een verwerking.
Gebruik de aanwezige **ICTRecht-privacy-plugin** in deze werkmap:
- **`/ictrecht-privacy-basis:dpia`** — DPIA voor de hele verwerking (verplicht bij BSN/bijzondere gegevens, bijlage §2.7).
- **`/ictrecht-privacy-basis:doorgifte`** — doorgifte buiten de EER per provider (SCC/TIA).
- **`/ictrecht-privacy-basis:vok-review`** — verwerkersovereenkomst per externe embedding-/LLM-provider.
- **`/ictrecht-privacy-basis:grondslag`** — grondslag per verwerking.
- **`/ictrecht-privacy-basis:avg-rechten`** — inzage/verwijdering raakt óók index + logs (PRIV-04).

Technisch borgen: **PII-detectie aan de poort** (BSN-elfproef, IBAN, gezondheidstermen) met maskering vóór externe doorgifte (PRIV-05); dataminimalisatie (PRIV-01).

---

## 8. Implementatie-roadmap (gefaseerd)

| Fase | Resultaat | Belangrijkste testplan-ID's |
|---|---|---|
| **0. Inventarisatie** | Datastromen + trust boundaries vastgelegd; synthetische testdata + "vuil corpus" + canary's | §1, 3.2 |
| **1. Gateway live** | ContextForge achter TLS-proxy; OAuth/OIDC; admin-bootstrap; geen anonieme toegang | AUTH-01..05 |
| **2. RBAC + registratie** | RAG-MCP-server als virtual server; rollen/teams/scopes (least privilege) | AUTH-03, TOOL-04 |
| **3. Data-autorisatie** | Identiteitspropagatie → RLS/server-side filters in RAG-backend | AUTHZ-01..05 |
| **4. Hardening** | Inputvalidatie, SSRF-allowlist, prompt-injection-inspectie, output-/exfil-sanitisatie | INJ-*, PI-*, EXFIL-* |
| **5. Betrouwbaarheid** | HA, rate limit, kostenplafond, backups + DR-test, fail-safe gedrag | DOS-01..04 |
| **6. Observability** | Audit-log + PII-maskering + canary-alerting + lek-runbook | LOG-01..04, EXFIL-04 |
| **7. Privacy/AVG** | DPIA, VOK's, EER-doorgifte, PII-gate | PRIV-01..06 |
| **8. Test-gates** | CCI-securityregressies als gate; red-team per release; RAG-kwaliteit (groundedness/retrieval) | INJ/PI/EXFIL/QUAL/SAFE |

**CI-gate (snel, elke wijziging):** AUTH, AUTHZ, INJ, PI, EXFIL-canary, PRIV-logging, SCA.
**Per release:** red-team-ronde + RAG-kwaliteitsevaluatie (gouden set).
**Periodiek:** externe pentest + privacy-review.

---

## 9. Directe vervolgstappen
1. `cp .env.example .env`, secrets genereren, sterke admin-wachtwoorden zetten.
2. `docker compose up -d`; admin-login verifiëren via de TLS-proxy.
3. Je RAG-MCP-server registreren als virtual server en rollen toewijzen.
4. Identiteitspropagatie + RLS bouwen in de RAG-backend (fase 3 — de belangrijkste stap).
5. [SECURITY-CHECKLIST.md](SECURITY-CHECKLIST.md) aflopen; daarna fase 4–8.

> Wil je dat ik de **RAG-MCP-server zelf scaffold** (FastMCP/Python met identiteitspropagatie
> + pgvector-RLS-voorbeeld) en/of een **geautomatiseerde injectie-/canary-testsuite** voor de
> CI-gate bouw? Dat zijn de logische volgende bouwstappen.
