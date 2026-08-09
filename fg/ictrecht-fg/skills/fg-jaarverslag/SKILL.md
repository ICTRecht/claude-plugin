---
name: fg-jaarverslag
description: >
  Stel een FG-jaarverslag op voor het bestuur of de hoogste leidinggevende,
  met een terugblik op toezicht, adviezen en incidenten. Gebruik dit als de FG
  jaarlijks moet rapporteren over de uitvoering van zijn taken.
argument-hint: "[periode, en eventueel eerdere rapportages of outputs]"
---

# /ictrecht-fg:fg-jaarverslag

Stel een FG-jaarverslag op voor het hoogste leidinggevende niveau van de organisatie.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Controleer `~/.claude/plugins/config/ictrecht-fg/outputs/` op eerdere FG-outputs uit de verslagperiode (DPIA-adviezen, datalek-toetsen, toezichtsplannen — alleen als dat pad beschikbaar is) om het jaarverslag op te baseren.
3. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** het jaarverslag heeft geen eigen wettelijke basis in de AVG — het is de
gangbare praktische invulling van de directe rapportagelijn aan het hoogste leidinggevende
niveau die art. 38 lid 3 wél wettelijk voorschrijft. Vraag, als de organisatiecontext dit
niet al aangeeft, of het bestuur een specifieke vorm of frequentie van rapportage
verwacht.

## Stap 1 — Bronnen verzamelen

Vraag naar of doorzoek (indien het outputs-pad beschikbaar is) de FG-activiteiten uit de
verslagperiode:
- Uitgevoerde `dpia-toets`- en `fg-advies`-adviezen
- Beoordeelde datalekken (`datalek-toets`)
- Uitgevoerde of geplande onderdelen uit het `toezichtsplan`
- Contact met de AP (`ap-contact`), inclusief eventuele voorafgaande raadplegingen
- Openstaande aanbevelingen uit `register-toets` en `vok-toets`

Ontbreken deze gegevens? Vraag de gebruiker om een samenvatting van de belangrijkste
activiteiten in de periode.

## Stap 2 — Structuur van het jaarverslag

1. **Samenvatting** — de belangrijkste conclusie in enkele zinnen: staat de organisatie er goed voor, en wat vraagt het meeste aandacht.
2. **Uitgevoerd toezicht** — wat is gecontroleerd, en met welke bevindingen.
3. **Adviezen** — hoeveel en welke adviezen zijn gegeven, en zijn ze overgenomen (inclusief eventuele gemotiveerde afwijkingen, art. 39 lid 1 sub c).
4. **Incidenten** — aantal en aard van datalekken in de periode, afhandeling en trend.
5. **Contact met de toezichthouder** — eventuele raadplegingen of vragen van de AP.
6. **Openstaande punten en aanbevelingen** — wat vraagt besluitvorming of actie van het bestuur.
7. **Vooruitblik** — aandachtspunten voor de volgende periode (bv. uit het toezichtsplan).

## Stap 3 — Output

Schrijf het jaarverslag naar `~/.claude/plugins/config/ictrecht-fg/outputs/fg-jaarverslag-[periode].md`.
Als dat pad niet beschikbaar is, toon het volledige jaarverslag in de chat.

Sluit af met de standaard ICTRecht disclaimer.
