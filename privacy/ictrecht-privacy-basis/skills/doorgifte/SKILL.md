---
name: doorgifte
description: >
  Beoordeel een internationale doorgifte van persoonsgegevens buiten de EER.
  Gebruik dit bij cloudoplossingen, leveranciers buiten de EU, of als iemand
  vraagt of data naar een bepaald land mag worden gestuurd.
argument-hint: "[naam leverancier of land van doorgifte]"
---

# /ictrecht-privacy-basis:doorgifte

Beoordeel een internationale doorgifte conform AVG hoofdstuk V.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy-basis:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik je kennis van AVG hoofdstuk V, adequaatheidsbesluiten en EU-SCCs 2021.

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

Schrijf beoordeling naar `~/.claude/plugins/config/ictrecht-privacy-basis/outputs/doorgifte-[datum]-[land-leverancier].md`.
Als dat pad niet beschikbaar is, toon de volledige beoordeling in de chat.

Sluit af met de standaard ICTRecht disclaimer.
