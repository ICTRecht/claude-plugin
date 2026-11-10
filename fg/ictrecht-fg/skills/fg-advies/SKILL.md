---
name: fg-advies
description: >
  Stel een formeel FG-advies op over een DPIA, datalek, verwerking of ander
  gegevensbeschermingsvraagstuk, conform AVG artikel 39 lid 1 sub a. Gebruik dit
  als iemand vraagt "wat zou ik als FG hiervan moeten vinden", een formeel advies
  wil vastleggen, of een FG-standpunt nodig heeft voor een dossier of het bestuur.
argument-hint: "[het vraagstuk, de DPIA, het datalek of de verwerking]"
---

# /ictrecht-fg:fg-advies

Stel een formeel FG-advies op conform AVG artikel 39 lid 1 sub a: de kerntaak van de FG om verwerkingsverantwoordelijke, verwerker en werknemers te informeren en adviseren over hun verplichtingen.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Controleer `~/.claude/plugins/config/ictrecht-fg/outputs/` op eerdere adviezen over hetzelfde vraagstuk (alleen als dat pad beschikbaar is).
3. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** dit is de generieke FG-adviesskill voor vraagstukken die niet al door een
specifiekere skill worden gedekt (gebruik `dpia-toets` voor een DPIA-specifiek advies,
`datalek-toets` voor een incident, `grondslag-advies` of `doorgifte-advies` voor die
specifieke vragen). De FG informeert en adviseert (art. 39 lid 1 sub a) — het is geen
besluit en geen goed- of afkeuring; de verwerkingsverantwoordelijke of werknemer die om
advies vraagt, blijft verantwoordelijk voor het gevolg dat aan het advies wordt gegeven.

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool om je advies te gronden in actuele ICTRecht-bronnen,
   naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

## Stap 1 — Wat is de vraag?

Stel vast wie iets van de FG wil weten en waarover:
- Wie vraagt om advies (bestuur, een collega, de verwerkingsverantwoordelijke zelf)?
- Waar gaat het over: een specifieke verwerking, een voorgenomen product, een beleidskeuze, een eerder genomen besluit?

Vraag door als de situatie nog onvoldoende concreet is om een advies op te baseren.

## Stap 2 — Juridisch kader

Breng de relevante normen in kaart: welke AVG-artikelen, UAVG-bepalingen of sectorspecifieke
regelgeving raken deze vraag. Maak onderscheid tussen wat verplicht is, wat aan te raden is
en wat een vrije keuze van de organisatie is.

## Stap 3 — FG-perspectief

Beoordeel de vraag vanuit de FG-rol (art. 39): welk risico voor betrokkenen speelt hier, en
welk toezichts- of adviespunt is voor de FG relevant — dit is een andere invalshoek dan een
generieke compliance-blik. Benoem concreet waar een FG in dit geval op zou letten en waarom.

## Stap 4 — Advies

Formuleer het advies:
- **Kernadvies**: in 1-3 zinnen, direct en stellig.
- **Onderbouwing**: gekoppeld aan concrete artikelen of normen.
- **Randvoorwaarden**: wat er moet gebeuren wil het advies opgaan (bv. "mits toestemming vrijwillig is").
- **Als het advies niet wordt gevolgd**: benoem wat de organisatie dan in ieder geval moet documenteren of motiveren.

## Stap 5 — Output

Schrijf het advies naar `~/.claude/plugins/config/ictrecht-fg/outputs/fg-advies-[datum]-[onderwerp].md`.
Als dat pad niet beschikbaar is, toon het volledige advies in de chat.

Sluit af met de standaard ICTRecht disclaimer.
