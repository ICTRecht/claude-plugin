# ie-clausules

**name:** ie-clausules
**description:** Beoordeel of stel IP-clausules op in contracten (overdracht, licentie, work-for-hire, non-compete).
**argument-hint:** "[contract of clausule]"

---

## Voorbereiding (3-laags)

1. Lees `~/.claude/plugins/config/ictrecht-ie/CLAUDE.md` — gebruik organisatieprofiel als het bestaat en geen [PLACEHOLDER] bevat.
2. Zoek anders in geheugen naar "ICTRecht IE organisatieprofiel".
3. Geen van beide beschikbaar: ga generiek verder en vermeld ℹ️ dat het profiel nog niet is ingevuld; adviseer `/ictrecht-ie:cold-start-interview` uit te voeren.

---

## Workflow

**Stap 1 — Context**
Breng de contractcontext in kaart: welk type contract (ontwikkelovereenkomst, arbeidscontract, freelance/ZZP-overeenkomst, SaaS-agreement, NDA, samenwerkingsovereenkomst)? Welke partijen? Wat wordt gemaakt of geleverd?

**Stap 2 — Eigendomsregeling**
Analyseer wie rechthebbende wordt van de door opdrachtnemer/werknemer gegenereerde IE. Bespreek het verschil tussen stilzwijgende licentie en expliciete eigendomsoverdracht. Wijs op risico's van onduidelijke eigendomsregelingen.

**Stap 3 — Licentiebepalingen**
Beoordeel of stel licentiebepalingen op:
- Exclusief vs. niet-exclusief
- Omvang (territorium, toepassingsgebied, subdomeinen)
- Duur (tijdelijk of eeuwigdurend)
- Sublicentiëring (toegestaan of niet?)
- Overdraagbaarheid bij fusie/overname

**Stap 4 — Overdrachtsclausule**
Toets of de overdrachtsclausule voldoet aan art. 2 Aw: schriftelijk vereiste, specificiteitseis (toekomstige werken moeten voldoende bepaald zijn), en of persoonlijkheidsrechten afzonderlijk worden behandeld.

**Stap 5 — Werknemers en contractors**
Bespreek het onderscheid:
- Werknemer in dienstbetrekking: art. 7 Aw (werkgeversauteursrecht) of art. 8 Aw
- ZZP/freelancer: geen automatische overdracht — expliciete clausule vereist
- Aandachtspunten bij internationale contracten

**Stap 6 — Rode vlaggen en verbeterpunten**
Identificeer ontbrekende of zwakke clausules. Geef concrete verbeteringsvoorstellen of alternatieve clausuleteksten.

---

## Output

Sla uitgewerkte analyses of concept-clausules op in `~/.claude/plugins/config/ictrecht-ie/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
