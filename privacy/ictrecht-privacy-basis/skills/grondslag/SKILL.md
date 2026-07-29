---
name: grondslag
description: >
  Bepaal de juiste verwerkingsgrondslag voor een verwerking van persoonsgegevens.
  Gebruik dit als iemand vraagt op welke grondslag een verwerking is gebaseerd,
  of toestemming nodig is, of een verwerking is toegestaan.
argument-hint: "[omschrijving van de verwerking]"
---

# /ictrecht-privacy-basis:grondslag

Bepaal de verwerkingsgrondslag conform AVG artikel 6 (en art. 9 voor bijzondere categorieën).

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht-privacy-basis/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht Privacy organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Privacy Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy-basis:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik je kennis van AVG art. 6 grondslagen en relevante jurisprudentie.

## Stap 1 — Zijn het bijzondere categorieën?

Bijzondere categorieën (art. 9 lid 1): ras of etnische afkomst, politieke opvattingen, religieuze of
levensbeschouwelijke overtuigingen, vakbondslidmaatschap, genetische gegevens, biometrische gegevens
met het oog op unieke identificatie, gezondheidsgegevens, en gegevens over seksueel gedrag of seksuele gerichtheid.

Als ja → naast een grondslag uit art. 6 is een uitzondering uit art. 9 lid 2 vereist. Let ook op de nationale uitwerkingen in de UAVG (art. 22 e.v.).

**Let op:** strafrechtelijke gegevens vallen niet onder art. 9 maar onder art. 10 AVG (en art. 31-33 UAVG) — verwerking alleen onder overheidstoezicht of op basis van een wettelijke uitzondering.

## Stap 2 — Zes grondslagen (art. 6 AVG)

Beoordeel elke grondslag:

| Grondslag | Wanneer passend | Aandachtspunten |
|---|---|---|
| **Toestemming** (a) | Als de betrokkene een echte vrije keuze heeft en de verwerking optioneel is | Vrij, specifiek, geïnformeerd, ondubbelzinnig. Altijd intrekbaar. In gezagsverhoudingen (zoals werkgever-werknemer) zelden 'vrij'. Geen restgrondslag: kies toestemming niet omdat niets anders past. |
| **Overeenkomst** (b) | Noodzakelijk voor uitvoering contract | Strikt noodzakelijk — niet "handig" |
| **Wettelijke verplichting** (c) | EU/nationale wet schrijft voor | Verwijs naar specifieke wet |
| **Vitaal belang** (d) | Noodsituaties | Zeer beperkt toepasbaar |
| **Algemeen belang / openbaar gezag** (e) | Overheidsorganisaties | Wettelijke basis vereist |
| **Gerechtvaardigd belang** (f) | Private partijen; overheid niet voor de uitoefening van haar publieke taken (art. 6 lid 1, slotzin) | Driestappentoets vereist (doeltoets, noodzakelijkheidstoets, belangenafweging); belangen van kinderen wegen extra zwaar mee |

## Stap 3 — Aanbeveling

Geef de meest passende grondslag met motivering.

Als gerechtvaardigd belang: voer de balancing test uit:
1. Welk belang heeft de verwerkingsverantwoordelijke?
2. Is de verwerking noodzakelijk voor dat belang?
3. Weegt het belang op tegen de belangen van de betrokkene?

## Output

Schrijf analyse naar `~/.claude/plugins/config/ictrecht-privacy-basis/outputs/grondslag-[datum]-[verwerking].md`.
Als dat pad niet beschikbaar is, toon de volledige analyse in de chat.

Sluit af met de standaard ICTRecht disclaimer.
