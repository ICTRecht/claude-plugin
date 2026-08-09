---
name: toezichtsplan
description: >
  Stel een risicogeoriënteerd FG-toezichtsplan op voor naleving van de AVG,
  conform artikel 39 lid 1 sub b. Gebruik dit als de FG een jaarplan, auditagenda
  of bewustmakingsprogramma wil opstellen voor het komende jaar of kwartaal.
argument-hint: "[periode en eventuele focusgebieden]"
---

# /ictrecht-fg:toezichtsplan

Stel een FG-toezichtsplan op conform AVG artikel 39 lid 1 sub b: toezien op de naleving van de verordening, toewijzing van verantwoordelijkheden, bewustmaking en opleiding van betrokken personeel, en audits.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Controleer `~/.claude/plugins/config/ictrecht-fg/outputs/` op eerdere toezichtsplannen of registerreviews (alleen als dat pad beschikbaar is).
3. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** dit is geen standaardchecklist die voor elke organisatie hetzelfde is — de FG
moet bij de uitvoering van zijn taken naar behoren rekening houden met het risico van de
verwerkingen, en met de aard, omvang, context en doeleinden daarvan (art. 39 lid 2). Het
toezichtsplan volgt dus uit de risico's van déze organisatie, niet uit een generieke lijst.

## Stap 1 — Risicoprofiel bepalen

Breng in kaart waar het grootste risico zit, op basis van (indien beschikbaar) het
organisatieprofiel, eerdere DPIA's, datalekken en verwerkingsregister:
- Welke verwerkingen zijn grootschalig, betreffen bijzondere categorieën, of omvatten stelselmatige monitoring (de criteria die een FG-aanstelling verplicht maken, art. 37 lid 1)?
- Welke eerdere bevindingen (uit `dpia-toets`, `datalek-toets`, `register-toets`, `vok-toets`) staan nog open?
- Welke nieuwe verwerkingen, producten of leveranciers zijn dit jaar te verwachten?

## Stap 2 — Toezichtsonderdelen uitwerken

Voor elk relevant onderdeel:

| Onderdeel | Frequentie | Reikwijdte |
|---|---|---|
| Steekproef verwerkingsregister | bv. kwartaal | Volledigheid en actualiteit van hoog-risico verwerkingen |
| Audit verwerkersovereenkomsten | bv. jaarlijks | Nieuwe en bestaande leveranciers met toegang tot persoonsgegevens |
| Toets openstaande DPIA-adviezen | continu | Zijn niet-overgenomen adviezen gemotiveerd vastgelegd? |
| Bewustmaking en opleiding | bv. per afdeling, jaarlijks | Personeel dat met persoonsgegevens werkt |
| Datalekregistratie doorlichten | bv. kwartaal | Patronen, herhaalde oorzaken, tijdige melding |

Pas frequentie en reikwijdte aan op het risicoprofiel uit stap 1 — een organisatie met veel bijzondere persoonsgegevens vereist een intensiever plan dan een organisatie met vooral administratieve verwerkingen.

## Stap 3 — Bewustmaking en opleiding

Benoem concreet welke doelgroepen welke kennis nodig hebben (bv. HR over sollicitantengegevens, marketing over toestemming en profilering, IT over beveiliging en datalekherkenning) en in welke vorm (training, e-learning, korte instructie).

## Stap 4 — Output

Lever een toezichtsplan met per onderdeel: wat, wanneer, door wie te ondersteunen (de FG voert dit zelf uit of vraagt de organisatie om ondersteuning conform art. 38 lid 2), en welke eerdere bevinding dit adresseert.

Schrijf het plan naar `~/.claude/plugins/config/ictrecht-fg/outputs/toezichtsplan-[periode].md`.
Als dat pad niet beschikbaar is, toon het volledige plan in de chat.

Sluit af met de standaard ICTRecht disclaimer.
