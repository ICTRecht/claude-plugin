---
name: verwerkingsregister
description: >
  Stel een verwerkingsregister op of review een bestaand register op AVG-conformiteit.
argument-hint: "[verwerking of bestaand register]"
---

## Voorbereiding

Controleer in deze volgorde of er organisatiecontext beschikbaar is:

1. **Configuratiebestand:** `~/.claude/plugins/config/ictrecht/CLAUDE.md` — lees dit bestand als het bestaat.
2. **Geheugen:** Zoek naar geheugenblokken met de titel "ICTRecht organisatieprofiel".
3. **Project-instructies:** Zoek naar een sectie `## ICTRecht Profiel` in de projectinstructies.

Als geen van de drie bronnen beschikbaar is: ga generiek te werk en voeg onderaan een ℹ️-melding toe:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses.*

Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `2f3b3297-a449-4848-b38b-44cf61d58c2a`
   (Gegevensverwerking Assistent, hergebruikt) om je analyse te gronden in actuele
   ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

---

## Workflow

### Stap 1 — Scope bepalen

Stel vast wat de gebruiker wil:
- **Nieuw:** een nieuwe verwerking toevoegen aan het register
- **Review:** een bestaand (deel van een) register toetsen aan AVG art. 30

Vraag indien onduidelijk welke scope van toepassing is.

### Stap 2 — AVG art. 30-vereisten doorlopen

Doorloop per verwerking de volgende verplichte velden conform art. 30 AVG:

| Veld | Omschrijving |
|------|-------------|
| Naam en contactgegevens verwerkingsverantwoordelijke | Inclusief eventuele vertegenwoordiger en FG |
| Doel van de verwerking | Concreet en specifiek omschreven |
| Categorieën van betrokkenen | Bijv. klanten, medewerkers, patiënten |
| Categorieën van persoonsgegevens | Bijv. NAW, financieel, bijzondere categorie |
| Ontvangers of categorieën van ontvangers | Intern en extern, inclusief verwerkers |
| Doorgiften naar derde landen | Land, grondslag (bijv. adequaatheidsbesluit, SCC) |
| Bewaartermijnen | Per categorie gegevens, onderbouwd |
| Beveiligingsmaatregelen | Technisch en organisatorisch (art. 32 AVG) |

**Uitzondering (art. 30 lid 5 AVG):** organisaties met minder dan 250 medewerkers zijn alleen vrijgesteld als de verwerking incidenteel is, geen risico inhoudt én geen bijzondere of strafrechtelijke gegevens betreft — in de praktijk is een register dus vrijwel altijd verplicht.

### Stap 3 — Volledigheidscheck

Beoordeel of er verwerkingen ontbreken door te vragen naar:
- Verwerkingen voor HRM, salarisadministratie, financiële administratie
- Klant- en leveranciersrelaties
- Marketing en communicatie
- IT-systemen en monitoring
- Bijzondere categorieën persoonsgegevens (art. 9 AVG)

### Stap 4 — Kwaliteitscheck

Toets de kwaliteit van bestaande of nieuwe vermeldingen:
- Zijn doelen concreet en specifiek genoeg (niet: "verbetering dienstverlening")?
- Zijn bewaartermijnen onderbouwd met wettelijke grondslag of beleidskeuze?
- Zijn bijzondere categorieën correct geïdentificeerd en voorzien van een uitzonderingsgrond (art. 9 lid 2 AVG)?
- Zijn doorgiften naar derde landen volledig en actueel?

### Stap 5 — Output

Lever af:
- **Nieuw:** een ingevulde registerrij in tabelformaat, klaar voor opname in het register
- **Review:** een reviewrapport met bevindingen per veld, aangevuld met prioriteiten (hoog/middel/laag) en concrete aanbevelingen

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-fg/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
