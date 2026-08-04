---
name: compliance-check
description: >
  Toets een situatie, product of beleid aan relevante wet- en regelgeving.
argument-hint: "[situatie, product of beleid]"
---

## Voorbereiding — configuratie laden (3-laags fallback)

Laad het organisatieprofiel in deze volgorde:

1. **Bestand** — lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
2. **Memory** — zoek naar memory-entry `ICTRecht organisatieprofiel`
3. **Project instructions** — zoek naar blok `## ICTRecht Profiel` in de actieve project instructions

Als **geen van de drie** beschikbaar is:
- Ga door met generieke standaardinstellingen (Nederlands recht, algemene IT-rechtpraktijk)
- Toon bovenaan de output:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-compliance-officer:cold-start-interview` uit voor gepersonaliseerde output.*

Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

---

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `PLACEHOLDER_COLLECTION_ID`
   <!-- Nog geen kennisbank-backend beschikbaar voor dit domein --> om je analyse te gronden
   in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

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

Sla de output op in `~/.claude/plugins/config/ictrecht-compliance-officer/outputs/compliance-[onderwerp]-[datum].md`.

Sluit af met de standaard ICTRecht disclaimer.
