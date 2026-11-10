---
name: ie-clausules
description: >
  Beoordeel of stel IP-clausules op in contracten (overdracht, licentie, work-for-hire).
argument-hint: "[contract of clausule]"
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
Toets of de overdrachtsclausule voldoet aan art. 2 Aw: levering vereist een daartoe bestemde (ondertekende) akte; de overdracht omvat alleen de bevoegdheden die in de akte staan vermeld of die noodzakelijk uit de aard of strekking van de titel voortvloeien (art. 2 lid 3 Aw — restrictieve uitleg); toekomstige werken moeten voldoende bepaald zijn; en persoonlijkheidsrechten (art. 25 Aw) moeten afzonderlijk worden geregeld via (gedeeltelijke) afstand.

**Stap 5 — Werknemers en contractors**
Bespreek het onderscheid:
- Werknemer in dienstbetrekking: art. 7 Aw (werkgeversauteursrecht) of art. 8 Aw
- ZZP/freelancer: geen automatische overdracht — expliciete clausule vereist
- Aandachtspunten bij internationale contracten

**Stap 6 — Rode vlaggen en verbeterpunten**
Identificeer ontbrekende of zwakke clausules. Geef concrete verbeteringsvoorstellen of alternatieve clausuleteksten.

---

## Output

Sla uitgewerkte analyses of concept-clausules op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
