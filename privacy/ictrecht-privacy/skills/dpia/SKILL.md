---
name: dpia
description: >
  Voer een Data Protection Impact Assessment (DPIA) uit voor een nieuwe verwerking,
  product of functionaliteit. Gebruik dit als iemand vraagt om een DPIA, PIA,
  gegevensbeschermingseffectbeoordeling, of een nieuwe verwerking wil beoordelen.
argument-hint: "[omschrijving van de verwerking of productfunctionaliteit]"
---

# /ictrecht-privacy:dpia

Voer een gestructureerde DPIA uit conform AVG artikel 35.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht-privacy/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht Privacy organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Privacy Profiel`
   - Geen van deze beschikbaar → meld: "Organisatieprofiel niet gevonden. Voer eerst `/ictrecht-privacy:cold-start-interview` uit." en stop.
2. Controleer `~/.claude/plugins/config/ictrecht-privacy/outputs/` op eerdere DPIA's voor dezelfde verwerking (alleen als dat pad beschikbaar is).
3. Zoek in de kennisbank: gebruik `search_dpia` met een gerichte query over het type verwerking.

## Stap 1 — Is een DPIA verplicht?

Beoordeel of een DPIA verplicht is op grond van:
- AVG artikel 35 (waarschijnlijk hoog risico)
- AP-lijst verplichte DPIA's (gebruik `search_dpia` om te controleren)
- Interne drempel van de organisatie (uit CLAUDE.md)

Meld expliciet: "DPIA verplicht" / "DPIA aanbevolen" / "DPIA niet vereist, wel gedocumenteerd".

## Stap 2 — Verwerkingsbeschrijving

Stel de volgende vragen als ze niet al zijn opgegeven:

1. Wat is het doel van de verwerking?
2. Welke categorieën persoonsgegevens worden verwerkt?
3. Van wie worden de gegevens verwerkt (betrokkenen)?
4. Wie zijn de ontvangers of verwerkers?
5. Worden gegevens doorgegeven buiten de EER?
6. Wat zijn de bewaartermijnen?
7. Welke technische en organisatorische maatregelen zijn voorzien?

## Stap 3 — Noodzakelijkheid en evenredigheid

Gebruik `search_dpia` en `search_gegevensverwerking` voor:
- Verwerkingsgrondslag (art. 6 AVG)
- Doelbinding (art. 5 lid 1 sub b)
- Dataminimalisatie (art. 5 lid 1 sub c)
- Proportionaliteit

## Stap 4 — Risicoanalyse

Identificeer risico's voor betrokkenen. Gebruik `search_dpia` voor risicocategorieën.

Voor elk risico:
| Risico | Kans | Impact | Bruto risico | Maatregel | Netto risico |
|---|---|---|---|---|---|

Schaal: Laag / Gemiddeld / Hoog

## Stap 5 — Maatregelen en conclusie

- Lijst technische maatregelen
- Lijst organisatorische maatregelen
- Conclusie: restrisico aanvaardbaar / raadpleging AP vereist (art. 36 AVG)

## Stap 6 — Output

Schrijf het DPIA-rapport naar `~/.claude/plugins/config/ictrecht-privacy/outputs/dpia-[datum]-[verwerking].md`.
Als dat pad niet beschikbaar is, toon het volledige rapport in de chat.

Sluit af met de standaard ICTRecht disclaimer.
