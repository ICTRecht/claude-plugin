---
name: auteursrecht
description: >
  Beantwoord auteursrechtelijke vragen over bescherming, inbreuk en overdracht van creatieve werken en software.
argument-hint: "[werk of situatie]"
---

## Voorbereiding (3-laags)

1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` — gebruik organisatieprofiel als het bestaat en geen [PLACEHOLDER] bevat.
2. Zoek anders in geheugen naar "ICTRecht organisatieprofiel".
3. Zoek anders in projectinstructies naar het blok `## ICTRecht Profiel`.
4. Geen van deze beschikbaar: ga generiek verder en vermeld ℹ️ dat het profiel nog niet is ingevuld; adviseer `/ictrecht-legal-counsel:cold-start-interview` uit te voeren.

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
   <!-- Nog geen kennisbank-backend beschikbaar voor dit domein --> om je analyse te
   gronden in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

---

## Workflow

**Stap 1 — Is het werk auteursrechtelijk beschermd?**
Beoordeel of het werk voldoet aan de beschermingsvereisten: eigen/oorspronkelijk karakter en persoonlijk stempel van de maker (Auteurswet art. 1 en 10 Aw). Ga in op het type werk (software, tekst, afbeelding, database, etc.).

**Stap 2 — Wie is rechthebbende?**
Analyseer de auteursrechtelijke toewijzing: maker als hoofdregel, werk naar ontwerp en onder leiding en toezicht van een ander (art. 6 Aw), werkgeversauteursrecht (art. 7 Aw), of de rechtspersoon die het werk als van haar afkomstig openbaar maakt zonder een natuurlijke persoon als maker te vermelden (art. 8 Aw). Let op: een opdrachtgever wordt níet automatisch rechthebbende — daarvoor is overdracht bij akte vereist (art. 2 Aw). Bespreek overdracht en licentie als van toepassing.

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
- Tijdelijke reproductie (art. 13a Aw)
- Parodie-exceptie (art. 18b Aw)
- Andere toepasselijke excepties

**Stap 6 — Advies en handhavingsopties**
Geef praktisch advies en bespreek handhavingsopties: sommatie/ingebrekestelling, kort geding, bodemprocedure, schadevergoeding (art. 27/27a Aw), winstafdracht.

---

## Output

Sla uitgewerkte analyses op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
