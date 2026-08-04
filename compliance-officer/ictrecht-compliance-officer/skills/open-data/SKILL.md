---
name: open-data
description: >
  Analyseer open data verplichtingen en hergebruiksvraagstukken voor overheden en bedrijven.
argument-hint: "[dataset of situatie]"
---

## Voorbereiding

Controleer in deze volgorde of er organisatiecontext beschikbaar is:

1. **Configuratiebestand:** `~/.claude/plugins/config/ictrecht/CLAUDE.md` — lees dit bestand als het bestaat.
2. **Geheugen:** Zoek naar geheugenblokken met de titel "ICTRecht organisatieprofiel".
3. **Project-instructies:** Zoek naar een sectie `## ICTRecht Profiel` in de projectinstructies.

Als geen van de drie bronnen beschikbaar is: ga generiek te werk en voeg onderaan een ℹ️-melding toe:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-compliance-officer:cold-start-interview` uit voor gepersonaliseerde analyses.*

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

## Workflow

### Stap 1 — Is er sprake van open data?

Beoordeel of de dataset kwalificeert als open data:
- Is de data afkomstig van een overheidsorgaan of publiekrechtelijke instelling?
- Is de data (mede) gefinancierd met publieke middelen?
- Valt de dataset onder de categorie High Value Datasets (HVD)?
- Heeft de organisatie al vrijwillig gekozen voor open data-beleid?

Concludeer of er sprake is van een (potentiële) open data-verplichting of -mogelijkheid.

### Stap 2 — Toepasselijke regelgeving

Breng het juridisch kader in kaart:

| Regelgeving | Toepassingsbereik |
|------------|-----------------|
| Open Data Richtlijn 2019/1024 (PSI-richtlijn) | Overheidsorganen en publiekrechtelijke instellingen in de EU |
| Wet hergebruik van overheidsinformatie (Who, herzien in 2024) | Nederlandse implementatie van de Open Data Richtlijn |
| Data Governance Act (EU) 2022/868 | Hergebruik van beschermde overheidsdata (o.a. vertrouwelijke gegevens en persoonsgegevens) |
| INSPIRE-richtlijn 2007/2/EG | Ruimtelijke data bij overheidsorganen |
| HVD-uitvoeringsverordening (EU) 2023/138 | Specifieke verplichtingen voor High Value Datasets |
| AVG | Indien de dataset persoonsgegevens bevat |

### Stap 3 — High Value Datasets (HVD)

Beoordeel of de dataset valt onder de HVD-uitvoeringsverordening. De zes categorieën zijn:

1. **Georuimtelijke data** — kaarten, kadastrale gegevens, bestemmingsplannen
2. **Aardobservatie en milieu** — satellietdata, klimaatdata, luchtkwaliteit
3. **Meteorologie** — weerdata, klimaatprojecties
4. **Statistiek** — nationale statistieken, demografische data
5. **Mobiliteit** — verkeer, openbaar vervoer, wegennet
6. **Bedrijven en eigendom** — handelsregisterdata, eigendomsdata

Bij HVD gelden aanvullende verplichtingen:
- Beschikbaar stellen via API
- Machine-leesbaar formaat
- Gratis beschikbaar (tenzij uitzondering van toepassing)
- Licentie: Creative Commons CC BY 4.0 of gelijkwaardig

### Stap 4 — Hergebruikslicentie

Beoordeel welke licentie van toepassing is of aanbevolen wordt:

| Licentie | Beschrijving | Geschikt voor |
|---------|-------------|--------------|
| CC0 (publiek domein) | Geen restricties | Overheidsdata, HVD |
| CC BY 4.0 | Naamsvermelding vereist | Meeste open data |
| CC BY-SA 4.0 | Naamsvermelding + share-alike | Data met copyleft-vereiste |
| Open Government Licence (OGL) | Specifiek voor overheidsdata | VK-context, soms NL |
| Geen open licentie | Gesloten of beperkt hergebruik | Niet-open data |

Adviseer de meest passende licentie, rekening houdend met de HVD-vereisten.

### Stap 5 — Beperkingen

Signaleer mogelijke beperkingen op publicatie of hergebruik:
- **Persoonsgegevens** — AVG-verplichting tot anonimisering of pseudonimisering vóór publicatie
- **Intellectueel eigendom van derden** — auteursrechten, databankrechten, licenties
- **Nationale veiligheid en openbare orde** — uitzonderingsgrond art. 1 lid 6 Open Data Richtlijn
- **Bedrijfsvertrouwelijke informatie** — beperkte uitzondering, toets proportionaliteit
- **Statistische vertrouwelijkheid** — wettelijke geheimhoudingsplichten bij statistiekdata

### Stap 6 — Publicatieverplichtingen en aanbevelingen

Lever concrete aanbevelingen:
- Welke datasets moeten of kunnen worden gepubliceerd?
- Via welk kanaal (data.overheid.nl, eigen portaal, API)?
- In welk formaat (CSV, JSON, RDF, GML)?
- Welke licentie?
- Welke aanvullende stappen zijn nodig (anonimisering, kwaliteitscontrole)?

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-compliance-officer/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
