---
name: doorgifte
description: >
  Beoordeel een internationale doorgifte van persoonsgegevens buiten de EER.
  Gebruik dit bij cloudoplossingen, leveranciers buiten de EU, of als iemand
  vraagt of data naar een bepaald land mag worden gestuurd.
argument-hint: "[naam leverancier of land van doorgifte]"
---

# /ictrecht-privacy:doorgifte

Beoordeel een internationale doorgifte conform AVG hoofdstuk V.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht-privacy/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht Privacy organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Privacy Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik `search_doorgifte` voor actuele grondslagen en vereisten.

## Stap 1 — Is er sprake van doorgifte?

Doorgifte = verstrekking of toegang tot persoonsgegevens vanuit de EER naar een derde land.
Let op: remote access door een medewerker buiten de EER telt ook.

## Stap 2 — Naar welk land?

Controleer:
- **Adequaatheidsbesluit** aanwezig? (gebruik `search_doorgifte` voor actuele lijst)
  → Zo ja: doorgifte toegestaan, documenteer.
- **Geen adequaatheidsbesluit** → passende waarborgen vereist.

## Stap 3 — Passende waarborg

Als geen adequaatheidsbesluit:

| Grondslag | Wanneer |
|---|---|
| Standard Contractual Clauses (SCCs) | Meest gebruikte optie |
| Binding Corporate Rules (BCRs) | Intra-concern |
| Gedragscode / certificering | Specifieke sectoren |
| Uitzondering (art. 49) | Alleen in bijzondere gevallen |

Gebruik `search_doorgifte` voor actuele SCC-informatie (EU-SCCs 2021).

## Stap 4 — Transfer Impact Assessment (TIA)

Bij SCCs: is een TIA vereist?
Beoordeel het recht van het ontvangende land (met name: overheidstoegangsbevoegdheden).

Gebruik `search_doorgifte` voor TIA-methodiek en aandachtspunten.

## Stap 5 — Conclusie

- Doorgifte toegestaan: **ja / nee / ja mits [maatregelen]**
- Vereiste documentatie
- Eventuele aanvullende maatregelen

## Output

Schrijf beoordeling naar `~/.claude/plugins/config/ictrecht-privacy/outputs/doorgifte-[datum]-[land-leverancier].md`.
Als dat pad niet beschikbaar is, toon de volledige beoordeling in de chat.

Sluit af met de standaard ICTRecht disclaimer.
