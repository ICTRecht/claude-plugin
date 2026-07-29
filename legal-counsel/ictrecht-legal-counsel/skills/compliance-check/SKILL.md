---
name: compliance-check
description: >
  Toets een situatie, product of beleid aan relevante wet- en regelgeving.
argument-hint: "[situatie, product of beleid]"
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

### Stap 1 — Context en sector
Beschrijf de situatie, het product of het beleid dat getoetst wordt. Identificeer:
- De betrokken organisatie(s) en hun rol
- De sector en activiteiten
- De geografische scope (NL / EU / internationaal)
- De doelgroep (consumenten / zakelijk / overheid)

### Stap 2 — Relevante regelgeving inventariseren
Stel een lijst op van toepasselijke wet- en regelgeving op EU- en nationaal niveau. Denk aan:

**EU-regelgeving:**
- Algemene Verordening Gegevensbescherming (AVG / GDPR)
- AI Act
- Digital Services Act (DSA)
- Digital Markets Act (DMA)
- Network and Information Security Directive (NIS2)
- ePrivacy Richtlijn / Telecommunicatiewet
- Productaansprakelijkheidsrichtlijn (EU) 2024/2853 — omvat ook software en AI
- Cybersecurity Act
- Data Act
- Cyber Resilience Act (CRA)
- DORA (financiële sector)

**Nederlands recht:**
- Burgerlijk Wetboek (contracten, aansprakelijkheid)
- Telecommunicatiewet
- Cyberbeveiligingswet (implementatie NIS2; opvolger van de Wbni — controleer de actuele status van inwerkingtreding)
- Sectorspecifieke wetgeving (Wft, WMG, Aanbestedingswet, etc.)

### Stap 3 — Per wet: verplichtingen vs. huidige situatie
Toets per relevante wet de naleving:

| Wet / Regelgeving | Kernverplichting | Status | Toelichting |
|---|---|---|---|
| [Wet X] | [Verplichting] | ✅ Compliant / ⚠️ Gap / ❓ Onduidelijk | [Toelichting] |

### Stap 4 — Prioritering gaps
Categoriseer geconstateerde gaps op risiconiveau:
- **Hoog** — directe handhavingsrisico's, hoge boetes, reputatieschade
- **Middel** — herstelbaar maar vereist actie op korte termijn
- **Laag** — aanbevolen verbeteringen, geen directe risico's

### Stap 5 — Actieplan
Stel per gap een concrete actie voor:
- Wat moet er gedaan worden?
- Door wie (intern / extern)?
- Op welke termijn (direct / 3 maanden / 12 maanden)?

---

## Output

Volledig compliance-rapport met context, regelgevingsoverzicht, toetsingstabel, gap-prioritering en actieplan.

Sla de output op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/compliance-[onderwerp]-[datum].md`.

Sluit af met de standaard ICTRecht disclaimer.
