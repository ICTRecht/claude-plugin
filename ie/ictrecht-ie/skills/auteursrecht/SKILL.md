---
name: auteursrecht
description: >
  Beantwoord auteursrechtelijke vragen over bescherming, inbreuk en overdracht van creatieve werken en software.
argument-hint: "[werk of situatie]"
---

## Voorbereiding (3-laags)

1. Lees `~/.claude/plugins/config/ictrecht-ie/CLAUDE.md` — gebruik organisatieprofiel als het bestaat en geen [PLACEHOLDER] bevat.
2. Zoek anders in geheugen naar "ICTRecht IE organisatieprofiel".
3. Geen van beide beschikbaar: ga generiek verder en vermeld ℹ️ dat het profiel nog niet is ingevuld; adviseer `/ictrecht-ie:cold-start-interview` uit te voeren.

---

## Workflow

**Stap 1 — Is het werk auteursrechtelijk beschermd?**
Beoordeel of het werk voldoet aan de beschermingsvereisten: eigen/oorspronkelijk karakter en persoonlijk stempel van de maker (Auteurswet art. 1 en 10 Aw). Ga in op het type werk (software, tekst, afbeelding, database, etc.).

**Stap 2 — Wie is rechthebbende?**
Analyseer de auteursrechtelijke toewijzing: maker als hoofdregel, of werkgeversauteursrecht (art. 7 Aw), of fictief makerschap opdrachtgever (art. 8 Aw). Bespreek overdracht en licentie als van toepassing.

**Stap 3 — Wat zijn de rechten?**
Beschrijf de relevante rechten:
- Exploitatierechten (verveelvoudiging, openbaarmaking)
- Persoonlijkheidsrechten (naamsvermelding, integriteitsrecht — art. 25 Aw)

**Stap 4 — Is er sprake van inbreuk?**
Beoordeel of sprake is van verveelvoudiging of openbaarmaking zonder toestemming van de rechthebbende. Weeg overeenstemming en totaalindruk.

**Stap 5 — Uitzonderingen**
Bespreek relevante uitzonderingen:
- Citaatrecht (art. 15a Aw)
- Onderwijsexceptie (art. 16 Aw)
- Tijdelijk reproductierecht (art. 13a Aw)
- Andere toepasselijke excepties

**Stap 6 — Advies en handhavingsopties**
Geef praktisch advies en bespreek handhavingsopties: sommatie/ingebrekestelling, kort geding, bodemprocedure, schadevergoeding (art. 27/27a Aw), winstafdracht.

---

## Output

Sla uitgewerkte analyses op in `~/.claude/plugins/config/ictrecht-ie/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
