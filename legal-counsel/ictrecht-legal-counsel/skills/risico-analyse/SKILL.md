---
name: risico-analyse
description: >
  Breng juridische risico's van een beslissing, product of situatie in kaart.
argument-hint: "[beslissing of situatie]"
---

## Voorbereiding — configuratie laden (3-laags fallback)

Laad het organisatieprofiel in deze volgorde:

1. **Bestand** — lees `~/.claude/plugins/config/ictrecht-legal-counsel/CLAUDE.md`
2. **Memory** — zoek naar memory-entry `ICTRecht Legal Counsel organisatieprofiel`
3. **Project instructions** — zoek naar blok `## ICTRecht Legal Counsel Profiel` in de actieve project instructions

Als **geen van de drie** beschikbaar is:
- Ga door met generieke standaardinstellingen (Nederlands recht, algemene IT-rechtpraktijk)
- Toon bovenaan de output:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-legal-counsel:cold-start-interview` uit voor gepersonaliseerde output.*

---

## Werkwijze

### Stap 1 — Context
Beschrijf wat er wordt overwogen: de beslissing, het product of de situatie die juridisch beoordeeld moet worden. Formuleer helder wat de scope is van de analyse.

### Stap 2 — Juridische risicodomeinen identificeren
Breng systematisch de relevante risicodomeinen in kaart, waaronder:
- **Contractueel** — wanprestatie, garanties, aansprakelijkheidsbedingen
- **Regulatory** — vergunningen, meldplichten, toezicht
- **Aansprakelijkheid** — product-, beroeps-, bestuurdersaansprakelijkheid
- **Intellectueel eigendom** — IE-inbreuk, eigendomsvraagstukken
- **AVG / Privacy** — verwerkingsgrondslag, datalekken, internationale doorgifte
- **Arbeidsrecht** — contractuele verplichtingen, medezeggenschap
- **Sectorspecifiek** — bijv. AI Act, NIS2, DSA, DMA, financieel recht, zorgwetgeving

### Stap 3 — Kans × impact matrix
Beoordeel elk geïdentificeerd risico op:
- **Kans** (laag / middel / hoog)
- **Impact** (laag / middel / hoog / kritiek)
- **Risicoscore** (combinatie van kans en impact)

Presenteer als tabel:

| Risico | Domein | Kans | Impact | Score | Toelichting |
|--------|--------|------|--------|-------|-------------|

### Stap 4 — Mitigerende maatregelen
Geef per hoog- en kritiek-risico concrete mitigerende maatregelen:
- Contractuele bescherming (clausules, vrijwaringen)
- Procedurele maatregelen (beleid, logging, toestemming)
- Technische maatregelen (indien relevant)
- Externe advisering of verzekering

### Stap 5 — Restrisico en aanbeveling go/no-go
Beschrijf het restrisico na mitigatie. Sluit af met een expliciete aanbeveling:
- **Go** — risico's zijn beheersbaar met de genoemde maatregelen
- **Go met voorbehouden** — go mits specifieke acties worden ondernomen
- **No-go** — risico's zijn te groot of niet te mitigeren

---

## Output

Gestructureerde risico-analyse met context, risicodomein-overzicht, kans×impact matrix, mitigerende maatregelen en go/no-go aanbeveling.

Sla de output op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/risico-[onderwerp]-[datum].md`.

Sluit af met de standaard ICTRecht disclaimer.
