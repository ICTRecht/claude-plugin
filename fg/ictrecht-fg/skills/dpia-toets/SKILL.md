---
name: dpia-toets
description: >
  Geef als FG advies over een DPIA en toets de uitvoering ervan conform AVG artikel
  39 lid 1 sub c. Gebruik dit als de FG om advies wordt gevraagd bij een DPIA, of
  wanneer een al uitgevoerde DPIA op volledigheid en methode moet worden getoetst.
argument-hint: "[DPIA-document of omschrijving van de verwerking]"
---

# /ictrecht-fg:dpia-toets

Geef FG-advies over een DPIA conform AVG artikel 39 lid 1 sub c, en toets de uitvoering conform artikel 35.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Controleer `~/.claude/plugins/config/ictrecht-fg/outputs/` op eerdere FG-adviezen over dezelfde verwerking (alleen als dat pad beschikbaar is).
3. Gebruik je kennis van DPIA-methodiek (AVG art. 35, AP-richtlijnen voor verplichte DPIA's).
4. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** de FG is geen toezichthouder en heeft geen corrigerende bevoegdheden — de FG
adviseert en toetst, maar keurt een DPIA niet goed of af. Het besluit blijft bij de
verwerkingsverantwoordelijke. Als die het FG-advies niet volgt, moet dat beargumenteerd in
de DPIA worden vastgelegd (art. 39 lid 1 sub c) — wijs hier expliciet op als de gebruiker
aangeeft het advies niet te willen overnemen.

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `6ea95c7b-0e2c-4efd-ac84-bd7a96fc9356`
   (DPIA Assistent) om je advies te gronden in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

## Stap 1 — Waarover wordt advies gevraagd?

Bepaal de vraag die voorligt (art. 39 lid 1 sub c bestrijkt alle drie):
1. **Is een DPIA verplicht?** — nog geen DPIA uitgevoerd, twijfel of het moet.
2. **Welke methode moet worden gevolgd?** — DPIA staat op de planning, vraag over aanpak.
3. **Zijn de conclusies en adviezen in een afgeronde DPIA correct?** — toets van een bestaand document.

## Stap 2 — Advies over verplichting (indien vraag 1)

Beoordeel of een DPIA verplicht is op grond van:
- AVG artikel 35 (waarschijnlijk hoog risico)
- AP-lijst verplichte DPIA's (raadpleeg je kennis van de AP-richtlijnen)
- Interne drempel van de organisatie (uit CLAUDE.md)

Geef je advies: "DPIA verplicht" / "DPIA aanbevolen" / "DPIA niet vereist, wel documenteren" — met motivering. Het besluit blijft bij de verwerkingsverantwoordelijke.

## Stap 3 — Toets van een uitgevoerde of concept-DPIA (indien vraag 2 of 3)

Doorloop de DPIA op de volgende punten en wijs per punt op hiaten of zwakke plekken — beoordeel niet met een eindcijfer, maar met concrete, adresseerbare bevindingen:

| Onderdeel | Toetsvraag |
|---|---|
| Verwerkingsbeschrijving | Zijn doel, categorieën gegevens, betrokkenen, ontvangers, doorgifte, bewaartermijn volledig beschreven? |
| Noodzakelijkheid en evenredigheid | Is de grondslag (art. 6) onderbouwd, doelbinding en dataminimalisatie expliciet gemaakt? |
| Risicoanalyse | Zijn de risico's voor betrokkenen (niet voor de organisatie) in kaart gebracht, met kans én impact? |
| Maatregelen | Sluiten de maatregelen aantoonbaar aan op de geïdentificeerde risico's, of zijn het generieke standaardmaatregelen? |
| Restrisico en conclusie | Is het restrisico expliciet benoemd, en is terecht bepaald of voorafgaande raadpleging (art. 36) nodig is? |

## Stap 4 — FG-advies

Formuleer het advies:
- **Advies**: concreet, gemotiveerd, per onderdeel uit stap 2 of 3.
- **Als het advies niet wordt overgenomen**: herinner de gebruiker dat dit beargumenteerd in de DPIA moet worden vastgelegd (art. 39 lid 1 sub c) — vraag niet zelf om die motivering, dat is aan de verwerkingsverantwoordelijke.
- **Vervolgtoezicht**: benoem of en wanneer de FG de uitvoering van de genomen maatregelen wil terugzien.

## Stap 5 — Output

Schrijf het FG-advies naar `~/.claude/plugins/config/ictrecht-fg/outputs/dpia-toets-[datum]-[verwerking].md`.
Als dat pad niet beschikbaar is, toon het volledige advies in de chat.

Sluit af met de standaard ICTRecht disclaimer.
