---
name: software-licenties
description: >
  Beoordeel software licenties inclusief open source, SaaS en proprietaire licenties.
argument-hint: "[software of licentievorm]"
---

## Voorbereiding (3-laags)

1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` — gebruik organisatieprofiel als het bestaat en geen [PLACEHOLDER] bevat.
2. Zoek anders in geheugen naar "ICTRecht organisatieprofiel".
3. Zoek anders in projectinstructies naar het blok `## ICTRecht Profiel`.
4. Geen van deze beschikbaar: ga generiek verder en vermeld ℹ️ dat het profiel nog niet is ingevuld; adviseer `/ictrecht-legal-counsel:cold-start-interview` uit te voeren.

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
   <!-- Nog geen kennisbank-backend beschikbaar voor dit domein --> om je analyse te
   gronden in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

---

## Workflow

**Stap 1 — Type licentie**
Identificeer het licentietype:
- Open source
- Proprietary / commercieel
- SaaS (Software as a Service)
- Hybrid (bijv. open core)

**Stap 2 — Voor open source: licentiecategorie**
Classificeer de open source licentie:
- Permissief: MIT, Apache 2.0, BSD — weinig verplichtingen
- Copyleft (sterk): GPL v2/v3 — afgeleid werk moet onder dezelfde licentie
- Weak copyleft: LGPL, MPL — beperktere copyleft-werking
- Network copyleft: AGPL — ook SaaS-gebruik triggert openbaarmakingsplicht

**Stap 3 — Verplichtingen**
Bespreek de concrete verplichtingen van de licentie:
- Broncode openbaar maken (en in welke mate)
- Naamsvermelding en licentietekst opnemen
- Compatibele licenties bij combineren
- Patentlicenties en disclaimers

**Stap 4 — Risico's**
Analyseer de relevante risico's:
- Copyleft-besmetting: wordt eigen/proprietary code meegetrokken?
- SaaS-loophole: geldt de copyleft-verplichting bij intern gebruik?
- Gebruik in commercieel product: welke beperkingen?
- Licentie-incompatibiliteit bij combineren van componenten

**Stap 5 — Aanbeveling**
Geef een duidelijk antwoord: mag de software worden gebruikt onder de gewenste voorwaarden? Zo ja: onder welke verplichtingen? Zo nee: wat zijn de alternatieven of mitigatiemaatregelen?

---

## Output

Sla uitgewerkte analyses op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
