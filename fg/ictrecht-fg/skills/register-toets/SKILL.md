---
name: register-toets
description: >
  Toets als FG een verwerkingsregister op volledigheid en kwaliteit conform AVG
  artikel 30, en toezien op naleving conform artikel 39. Gebruik dit als de FG
  een bestaand register wil beoordelen of een steekproef wil doen.
argument-hint: "[bestaand register of specifieke verwerking]"
---

# /ictrecht-fg:register-toets

Toets een verwerkingsregister conform AVG artikel 30, als onderdeel van het FG-toezicht op naleving (art. 39 lid 1 sub b).

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** het register wordt bijgehouden door de verwerkingsverantwoordelijke (art.
30 AVG) — de FG houdt het register niet zelf bij. Zelf de inhoud van het register bepalen
(welke verwerkingen, welke doelen, welke grondslag) raakt aan besluiten over doel en
middelen van verwerking, en dat is precies het soort taak waarbij een belangenconflict kan
ontstaan (art. 38 lid 6). De FG toetst, signaleert hiaten en adviseert over herstel.

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `2f3b3297-a449-4848-b38b-44cf61d58c2a`
   (Gegevensverwerking Assistent) om je toets te gronden in actuele ICTRecht-bronnen, naast
   je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

## Stap 1 — Scope van de toets

Stel vast wat wordt getoetst:
- **Volledig register**: alle verwerkingen doorlopen op aanwezigheid van verplichte velden.
- **Specifieke verwerking**: één vermelding in detail toetsen.
- **Steekproef**: een aantal willekeurige vermeldingen ter controle van de algehele kwaliteit.

## Stap 2 — AVG art. 30-vereisten toetsen

Toets per verwerking of de verplichte velden aanwezig én inhoudelijk toereikend zijn:

| Veld | Toetsvraag |
|------|-------------|
| Naam en contactgegevens verwerkingsverantwoordelijke | Aanwezig, inclusief FG-contactgegevens? |
| Doel van de verwerking | Concreet en specifiek, niet generiek geformuleerd? |
| Categorieën van betrokkenen | Volledig, geen ontbrekende categorie? |
| Categorieën van persoonsgegevens | Inclusief bijzondere categorieën (art. 9) correct gemarkeerd? |
| Ontvangers of categorieën van ontvangers | Intern én extern, inclusief verwerkers? |
| Doorgiften naar derde landen | Land én grondslag vermeld? |
| Bewaartermijnen | Per categorie onderbouwd, niet alleen "zo lang als nodig"? |
| Beveiligingsmaatregelen | Verwijzing naar concreet beveiligingsbeleid (art. 32)? |

**Let op de vrijstelling (art. 30 lid 5):** deze geldt alleen bij organisaties onder 250
medewerkers én uitsluitend voor incidentele verwerkingen zonder risico en zonder bijzondere
of strafrechtelijke gegevens — signaleer als een organisatie zich hierop beroept voor een
structurele verwerking, want dat is onterecht.

## Stap 3 — Volledigheidscheck

Signaleer mogelijk ontbrekende verwerkingen door te vragen naar veelvoorkomende categorieën
(HRM, salarisadministratie, klant- en leveranciersrelaties, marketing, IT-monitoring,
bijzondere persoonsgegevens) en te vergelijken met wat al in het register staat.

## Stap 4 — FG-oordeel

Geef per hiaat of zwak punt:
- **Bevinding**: wat ontbreekt of is onvoldoende specifiek.
- **Risico**: wat dit betekent bij een AP-controle of datalek.
- **Aanbeveling**: wie de aanvulling moet doen (dit doet de FG niet zelf) en op welke termijn.

Sluit af met een samenvattende tabel (Verwerking | Bevinding | Prioriteit).

## Stap 5 — Output

Schrijf de toets naar `~/.claude/plugins/config/ictrecht-fg/outputs/register-toets-[datum].md`.
Als dat pad niet beschikbaar is, toon de volledige toets in de chat.

Sluit af met de standaard ICTRecht disclaimer.
