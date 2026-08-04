---
name: doorgifte
description: >
  Beoordeel een internationale doorgifte van persoonsgegevens buiten de EER.
  Gebruik dit bij cloudoplossingen, leveranciers buiten de EU, of als iemand
  vraagt of data naar een bepaald land mag worden gestuurd.
argument-hint: "[naam leverancier of land van doorgifte]"
---

# /ictrecht-privacy-officer:doorgifte

Beoordeel een internationale doorgifte conform AVG hoofdstuk V.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy-officer:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik je kennis van AVG hoofdstuk V, adequaatheidsbesluiten en EU-SCCs 2021.
3. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `a7280324-a663-4c80-b056-ae42fc223abc`
   (Doorgifte Assistent AVG) om je analyse te gronden in actuele ICTRecht-bronnen, naast je
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
  → Zo ja: doorgifte toegestaan, documenteer.
  → **VS:** het EU-U.S. Data Privacy Framework (adequaatheidsbesluit, juli 2023) geldt alleen voor ontvangers met een actieve DPF-certificering — controleer die op dataprivacyframework.gov. Zonder certificering: passende waarborgen vereist.
- **Geen adequaatheidsbesluit** → passende waarborgen vereist.

## Stap 3 — Passende waarborg

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
Beoordeel het recht van het ontvangende land (met name: overheidstoegangsbevoegdheden) en of aanvullende
technische, contractuele of organisatorische maatregelen nodig zijn (EDPB Aanbevelingen 01/2020).

Gebruik je kennis van TIA-methodiek en overheidstoegangsbevoegdheden per land.

## Stap 5 — Conclusie

- Doorgifte toegestaan: **ja / nee / ja mits [maatregelen]**
- Vereiste documentatie
- Eventuele aanvullende maatregelen

## Output

Schrijf beoordeling naar `~/.claude/plugins/config/ictrecht-privacy-officer/outputs/doorgifte-[datum]-[land-leverancier].md`.
Als dat pad niet beschikbaar is, toon de volledige beoordeling in de chat.

Sluit af met de standaard ICTRecht disclaimer.
