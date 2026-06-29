# software-licenties

**name:** software-licenties
**description:** Beoordeel software licenties inclusief open source, SaaS en proprietaire licenties.
**argument-hint:** "[software of licentievorm]"

---

## Voorbereiding (3-laags)

1. Lees `~/.claude/plugins/config/ictrecht-ie/CLAUDE.md` — gebruik organisatieprofiel als het bestaat en geen [PLACEHOLDER] bevat.
2. Zoek anders in geheugen naar "ICTRecht IE organisatieprofiel".
3. Geen van beide beschikbaar: ga generiek verder en vermeld ℹ️ dat het profiel nog niet is ingevuld; adviseer `/ictrecht-ie:cold-start-interview` uit te voeren.

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

Sla uitgewerkte analyses op in `~/.claude/plugins/config/ictrecht-ie/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
