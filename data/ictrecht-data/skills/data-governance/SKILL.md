---
name: data-governance
description: >
  Toets of ontwikkel een data governance framework voor de organisatie.
argument-hint: "[huidige situatie of vraagstuk]"
---

## Voorbereiding

Controleer in deze volgorde of er organisatiecontext beschikbaar is:

1. **Configuratiebestand:** `~/.claude/plugins/config/ictrecht-data/CLAUDE.md` — lees dit bestand als het bestaat.
2. **Geheugen:** Zoek naar geheugenblokken met de titel "ICTRecht Data organisatieprofiel".
3. **Project-instructies:** Zoek naar een sectie `## ICTRecht Data Profiel` in de projectinstructies.

Als geen van de drie bronnen beschikbaar is: ga generiek te werk en voeg onderaan een ℹ️-melding toe:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-data:cold-start-interview` uit voor gepersonaliseerde analyses.*

---

## Workflow

### Stap 1 — Huidige situatie in kaart brengen

Stel de volgende vragen indien niet reeds beantwoord door het argument of het organisatieprofiel:
- Welke typen data beheert de organisatie (persoonsgegevens, bedrijfsgevoelige data, open data, IoT-data)?
- Wie heeft momenteel toegang tot welke data, en op basis waarvan?
- Welke interne regels of beleidslijnen bestaan er al rondom data?
- Zijn er recente incidenten of audits geweest die aanleiding geven tot dit traject?

### Stap 2 — Wettelijk kader vaststellen

Breng het toepasselijke juridisch kader in kaart:
- **AVG** — verwerking van persoonsgegevens, verwerkingsregister, beveiliging, rechten betrokkenen
- **EU Data Act** — toegangsrechten, verplichtingen data holders, portabiliteit
- **Sectorspecifieke regelgeving** — NIS2 (cybersecurity), DORA (financiële sector), AI Act (AI-systemen), EHDS (gezondheidsdata), Open Data Richtlijn (overheden)

Geef aan welke wet- en regelgeving concrete governance-verplichtingen oplegt.

### Stap 3 — Governance-elementen beoordelen

Beoordeel de aanwezigheid en kwaliteit van de volgende governance-elementen:

| Element | Aanwezig? | Kwaliteit / Bevinding |
|---------|-----------|----------------------|
| Rollen en verantwoordelijkheden | — | Bijv. CDO, DPO, data stewards |
| Datakwaliteitsbeleid | — | Definitie, meting, verbetering |
| Toegangsbeheer | — | Autorisatiebeleid, need-to-know principe |
| Dataclassificatie | — | Niveaus: openbaar / intern / vertrouwelijk / geheim |
| Retentiebeleid | — | Per datacategorie, aansluitend op wettelijke termijnen |
| Incidentresponse | — | Detectie, melding, herstel, evaluatie |

### Stap 4 — Gaps identificeren

Beschrijf per governance-element wat ontbreekt of onduidelijk is. Prioriteer op:
- **Juridisch risico** — ontbreekt dit element leidt tot non-compliance
- **Operationeel risico** — ontbreekt dit element leidt tot datalekken of dataverlies
- **Strategisch risico** — ontbreekt dit element belemmert data-driven werken of datadeling

### Stap 5 — Prioriteitenmatrix

Stel een prioriteitenmatrix op:

| Prioriteit | Element | Actie | Tijdlijn |
|-----------|---------|-------|---------|
| Hoog | ... | ... | ... |
| Middel | ... | ... | ... |
| Laag | ... | ... | ... |

### Stap 6 — Aanbevelingen framework

Lever concrete aanbevelingen voor het opzetten of verbeteren van het data governance framework:
- Wie moet wat doen (rollen en taken)
- Welke beleidslijnen moeten worden opgesteld of geactualiseerd
- Welke tools of processen ondersteunen de governance
- Hoe wordt het framework geborgd en periodiek geëvalueerd

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-data/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
