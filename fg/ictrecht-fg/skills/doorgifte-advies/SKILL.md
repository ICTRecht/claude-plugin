---
name: doorgifte-advies
description: >
  Geef als FG advies over een internationale doorgifte van persoonsgegevens
  buiten de EER, conform AVG artikel 39. Gebruik dit bij cloudoplossingen,
  leveranciers buiten de EU, of als de FG om advies wordt gevraagd of data naar
  een bepaald land mag worden gestuurd.
argument-hint: "[naam leverancier of land van doorgifte]"
---

# /ictrecht-fg:doorgifte-advies

Geef FG-advies over een internationale doorgifte conform AVG hoofdstuk V, als onderdeel van de informerende en adviserende taak (art. 39 lid 1 sub a).

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik je kennis van AVG hoofdstuk V, adequaatheidsbesluiten en EU-SCCs 2021.
3. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** het besluit om met een partij buiten de EER te werken en de keuze van het
doorgiftemechanisme liggen bij de verwerkingsverantwoordelijke. De FG adviseert over de
juridische houdbaarheid van die keuze, maar bepaalt hem niet.

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `a7280324-a663-4c80-b056-ae42fc223abc`
   (Doorgifte Assistent AVG) om je advies te gronden in actuele ICTRecht-bronnen, naast je
   eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

## Stap 1 — Is er sprake van doorgifte?

Doorgifte = verstrekking of toegang tot persoonsgegevens vanuit de EER naar een derde land.
Let op: remote access door een medewerker buiten de EER telt ook.

## Stap 2 — Naar welk land?

Controleer:
- **Adequaatheidsbesluit** aanwezig? (raadpleeg je kennis van actuele adequaatheidsbesluiten; controleer bij twijfel de actuele lijst van de Europese Commissie)
  → Zo ja: doorgifte toegestaan, advies: documenteren.
  → **VS:** het EU-U.S. Data Privacy Framework (adequaatheidsbesluit, juli 2023) geldt alleen voor ontvangers met een actieve DPF-certificering — controleer die op dataprivacyframework.gov. Zonder certificering: passende waarborgen vereist.
- **Geen adequaatheidsbesluit** → passende waarborgen vereist.

## Stap 3 — Advies over passende waarborg

Als geen adequaatheidsbesluit:

| Grondslag | Wanneer |
|---|---|
| Standard Contractual Clauses (SCCs) | Meest gebruikte optie |
| Binding Corporate Rules (BCRs) | Intra-concern |
| Gedragscode / certificering | Specifieke sectoren |
| Uitzondering (art. 49) | Alleen in bijzondere gevallen |

Gebruik je kennis van de EU-SCCs 2021 (Uitvoeringsbesluit 2021/914).

## Stap 4 — Transfer Impact Assessment (TIA)

Bij SCCs (en BCRs) is sinds het Schrems II-arrest (HvJ EU C-311/18) in de praktijk altijd een TIA vereist.
Adviseer over het recht van het ontvangende land (met name: overheidstoegangsbevoegdheden) en of aanvullende
technische, contractuele of organisatorische maatregelen nodig zijn (EDPB Aanbevelingen 01/2020).

Gebruik je kennis van TIA-methodiek en overheidstoegangsbevoegdheden per land.

## Stap 5 — FG-advies

- **Advies**: doorgifte houdbaar **ja / nee / ja mits [maatregelen]**, met motivering.
- **Vereiste documentatie**: wat de verwerkingsverantwoordelijke moet vastleggen.
- **Als het advies niet wordt overgenomen**: dit is aan de organisatie om te beargumenteren; de FG signaleert het risico maar heeft geen vetorecht.

## Output

Schrijf het advies naar `~/.claude/plugins/config/ictrecht-fg/outputs/doorgifte-advies-[datum]-[land-leverancier].md`.
Als dat pad niet beschikbaar is, toon het volledige advies in de chat.

Sluit af met de standaard ICTRecht disclaimer.
