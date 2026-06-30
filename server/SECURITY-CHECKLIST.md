# Security- & betrouwbaarheidschecklist (gemapt op het testplan)

Loop dit af vóór productie. Kolom "ID" verwijst naar de bijlage
(`Testplan_MCP_RAG_beveiliging.md`). Status: ☐ openstaand · ☑ geborgd.

## A. Authenticatie & transport (AUTH)
- ☐ **AUTH-01** Geen anonieme toegang — gateway default-deny; admin-UI achter auth.
- ☐ **AUTH-02** OAuth/OIDC met issuer + audience-validatie; korte TTL; `REQUIRE_JTI=true` + `REQUIRE_TOKEN_EXPIRATION=true` (revocatie/replay).
- ☐ **AUTH-03** Scopes/rollen least-privilege; tool buiten scope geweigerd.
- ☐ **AUTH-04** TLS-only via proxy; HSTS; geldig cert; `SECURE_COOKIES=true`.
- ☐ **AUTH-05** Sessie-isolatie op SSE/streamable HTTP; sessie-ownership afgedwongen.

## B. Autorisatie & multi-tenancy (AUTHZ) — *de belangrijkste laag*
- ☐ **AUTHZ-01** Geen confused deputy: RLS-context per gebruiker, niet één almachtig serviceaccount.
- ☐ **AUTHZ-02** Document-/chunk-autorisatie: canary in beperkt doc lekt niet naar onbevoegde.
- ☐ **AUTHZ-03** Tenant-isolatie: geen cross-tenant chunks.
- ☐ **AUTHZ-04** RLS in pgvector/Supabase; filters server-side uit identiteit, niet uit toolargumenten.
- ☐ **AUTHZ-05** Rechtenintrekking propageert direct naar index.

## C. Invoervalidatie & injectie (INJ)
- ☐ **INJ-01** Geen shell-uitvoering uit tool-input.
- ☐ **INJ-02** Geparametriseerde queries (geen SQL-concat).
- ☐ **INJ-03** Path-allowlist; geen `../` traversal.
- ☐ **INJ-04** SSRF-allowlist; `SSRF_ALLOW_PRIVATE_NETWORKS=false`; blokkeer `169.254.169.254`/RFC1918/localhost.
- ☐ **INJ-05** Strikte schemavalidatie (type/lengte/enum); geen crash op rommel.

## D. Tool-definitie-integriteit (TOOL)
- ☐ **TOOL-01** Host/agent volgt verborgen instructies in tooldescripties niet op; descripties gescand.
- ☐ **TOOL-02** Toolwijziging na goedkeuring vereist herbevestiging (geen stille swap).
- ☐ **TOOL-03** Naamconflict/shadowing gedetecteerd.
- ☐ **TOOL-04** Gevoelige tools vereisen expliciete goedkeuring.

## E. Indirecte prompt-injection via corpus (PI)
- ☐ **PI-01** Basisinjectie in chunk genegeerd.
- ☐ **PI-02** Verborgen tekst (zero-width/wit-op-wit/HTML-comment) genormaliseerd & genegeerd.
- ☐ **PI-03** Chunk die systeemprompt imiteert → geen privilege-escalatie (instructie-/datascheiding, spotlighting).
- ☐ **PI-04** Geen geheim in output-URL's o.b.v. corpusinstructie.
- ☐ **PI-05** Geen ongeautoriseerde toolaanroep aangestuurd door corpustekst.

## F. Datapoisoning & index-integriteit (POIS)
- ☐ **POIS-01/02** Misleidend/keyword-stuffed doc domineert niet onterecht.
- ☐ **POIS-03** Ingest-validatie: verborgen/uitvoerbare/oversized inhoud geweigerd of gesaneerd.
- ☐ **POIS-04** Herkomst per chunk vastgelegd; ongeauthenticeerde bron geweerd.

## G. Data-exfiltratie & uitvoer (EXFIL)
- ☐ **EXFIL-01/02** Markdown-afbeeldingen/links met externe data-dragende URL's gesaneerd.
- ☐ **EXFIL-03** Vectorstore niet publiek bereikbaar (intern netwerk in compose).
- ☐ **EXFIL-04** Canary end-to-end: lekt nergens buiten geautoriseerd pad.

## H. Privacy & AVG (PRIV)
- ☐ **PRIV-01** Dataminimalisatie naar embedding-/LLM-provider.
- ☐ **PRIV-02** Doorgifte buiten EER bekend; SCC/TIA aanwezig → `/ictrecht-privacy-basis:doorgifte`.
- ☐ **PRIV-03** Logging-hygiëne: PII-maskering + retentie afgedwongen.
- ☐ **PRIV-04** Verwijderrecht raakt index + logs → `/ictrecht-privacy-basis:avg-rechten`.
- ☐ **PRIV-05** PII-gate (BSN-elfproef/IBAN/gezondheid) maskeert vóór externe doorgifte.
- ☐ **PRIV-06** Grondslag + DPIA gedocumenteerd → `/ictrecht-privacy-basis:dpia` + `:grondslag` + `:vok-review`.

## I. Rate limiting, kosten & beschikbaarheid (DOS)
- ☐ **DOS-01** Rate limiting per gebruiker/tenant (gateway) + L7 (nginx).
- ☐ **DOS-02** Token-/kostenplafond stopt uitloop.
- ☐ **DOS-03** Backend-uitval faalt veilig; nette foutmelding, geen lek.
- ☐ **DOS-04** Contextomvang begrensd (`CONTENT_MAX_*`).

## J. Supply chain (SUP)
- ☐ **SUP-01** SCA-scan: geen kritieke/hoge open issues.
- ☐ **SUP-02** Lockfiles + image-tags gepind en geverifieerd.
- ☐ **SUP-03** Alleen gereviewde/getekende MCP-servers actief.
- ☐ **SUP-04** Minimale host-rechten: `read_only`, `cap_drop ALL`, `no-new-privileges`, intern netwerk (in compose toegepast).

## K. Logging, monitoring & IR (LOG)
- ☐ **LOG-01** Manipulatiebestendig auditspoor (toolaanroep + retrieval + identiteit).
- ☐ **LOG-02** Canary-/anomalie-alerting actief.
- ☐ **LOG-03** Datalek-runbook → `/ictrecht-privacy-basis:datalek`.
- ☐ **LOG-04** Logtoegang strikt beperkt; logs beschermd als gevoelige data.

## L. Betrouwbaarheid / RAG-kwaliteit (QUAL)
- ☐ **QUAL-01..08** Groundedness, retrievalkwaliteit, "niet gevonden" i.p.v. verzinnen, conflictdetectie, citatie-integriteit, consistentie, latentie/SLA. Gouden evaluatieset in CI.

## M. Output- & jailbreak-veiligheid (SAFE)
- ☐ **SAFE-01..03** Jailbreak-weerstand, weigering schadelijke output, geen systeemprompt-lek.
