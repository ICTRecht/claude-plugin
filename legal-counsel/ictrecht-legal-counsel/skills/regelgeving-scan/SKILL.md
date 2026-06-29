---
name: regelgeving-scan
description: >
  Bepaal welke wet- en regelgeving van toepassing is op een organisatie, product of dienst.
argument-hint: "[organisatietype, product of dienst]"
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

### Stap 1 — Activiteit beschrijven
Beschrijf de activiteit, het product of de dienst zo concreet mogelijk:
- Wat doet de organisatie / het product / de dienst?
- Wie zijn de afnemers of gebruikers?
- Welke data wordt verwerkt?
- Waar vindt de activiteit plaats (NL / EU / wereldwijd)?

### Stap 2 — Sectorspecifieke regelgeving
Identificeer regelgeving die specifiek geldt voor de sector of activiteit:
- **Zorg** — WMG, Wgbo, Wet kwaliteit klachten en geschillen zorg (Wkkgz), MDR
- **Financiën** — Wft, PSD2, DORA, MiFID II, AML-richtlijnen
- **Overheid** — Aanbestedingswet, Archiefwet, Wet open overheid (Woo), BIO
- **Energie** — Energiewet, RED III
- **Transport / Mobiliteit** — sector-specifieke EU-verordeningen
- **Onderwijs** — Wet bescherming persoonsgegevens in het onderwijs
- **Telecom / Media** — Wet elektronische communicatie, AVMS-richtlijn

### Stap 3 — Horizontale regelgeving
Identificeer breed-toepasbare regelgeving die ongeacht sector geldt:
- AVG / GDPR — persoonsgegevensverwerking
- AI Act — AI-systemen (classificatie: verboden / hoog risico / beperkt risico / minimaal risico)
- Digital Services Act (DSA) — onlinediensten en platforms
- Digital Markets Act (DMA) — poortwachters
- NIS2 — netwerk- en informatiebeveiliging
- Cybersecurity Act — certificering
- ePrivacy — cookies, elektronische communicatie
- Productaansprakelijkheidsrichtlijn — digitale producten
- Toegankelijkheidsrichtlijn (WCAG / EAA)

### Stap 4 — Contractuele verplichtingen upstream
Zijn er contractuele verplichtingen die extra regelgeving van toepassing maken?
- Verwerkersovereenkomsten (AVG art. 28)
- Overheidsopdrachten (aanbestedingsrechtelijke verplichtingen)
- Brancheafspraken of certificeringsvereisten (ISO 27001, NEN 7510, etc.)

### Stap 5 — Overzichtstabel
Presenteer het resultaat als overzichtstabel:

| Wet / Regelgeving | Van toepassing? | Kernverplichtingen | Prioriteit |
|---|---|---|---|
| AVG / GDPR | ✅ Ja | Verwerkingsgrondslag, privacyverklaring, verwerkersovereenkomst | Hoog |
| AI Act | ⚠️ Mogelijk | Classificatie AI-systeem bepalen | Middel |
| NIS2 | ❓ Controleren | Aanbieders essentiële diensten? | Middel |
| [Wet X] | ✅ / ⚠️ / ❌ | [Kernverplichtingen] | Hoog / Middel / Laag |

---

## Output

Volledig regelgevingsoverzicht met activiteitsbeschrijving, sectorspecifieke en horizontale regelgeving, contractuele verplichtingen en geprioriteerde overzichtstabel.

Sla de output op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/regelgeving-[onderwerp]-[datum].md`.

Sluit af met de standaard ICTRecht disclaimer.
