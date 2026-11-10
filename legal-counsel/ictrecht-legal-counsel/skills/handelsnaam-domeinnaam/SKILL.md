---
name: handelsnaam-domeinnaam
description: >
  Analyseer handelsnaam- en domeinnaamconflicten en beschermingsstrategie.
argument-hint: "[naam of domeinnaam]"
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

**Stap 1 — Handelsnaamrecht**
Analyseer de handelsnaamrechtelijke positie op grond van de Handelsnaamwet (Hnw):
- Is er sprake van gebruik als handelsnaam (duurzaam, in het handelsverkeer)?
- Prioriteit: wie gebruikte de naam het eerst?
- Bescherming te goeder trouw en verwarringsgevaar (art. 5 Hnw)
- Geografisch bereik van de bescherming

**Stap 2 — Merkrecht overlap**
Beoordeel of de naam ook als merk is geregistreerd (Benelux / EU / internationaal). Analyseer samenloop handelsnaamrecht en merkenrecht: welk recht heeft voorrang? Bespreek art. 2.20 lid 2 sub d BVIE (gebruik van een teken anders dan ter onderscheiding van waren of diensten, zoals handelsnaamgebruik).

**Stap 3 — Domeinnaamconflict**
Analyseer het domeinnaamconflict aan de hand van de UDRP/WIPO-procedure criteria (drie cumulatieve vereisten):
1. Domeinnaam is identiek aan of verwarringwekkend gelijkend op het merk/handelsnaam van eiser
2. Verweerder heeft geen recht op of legitiem belang bij de domeinnaam
3. De domeinnaam is te kwader trouw geregistreerd en/of gebruikt

Bespreek ook de SIDN Geschillenbeslechting (voor .nl-domeinen).

**Stap 4 — Opties**
Bespreek de beschikbare acties:
- Sommatie / cease-and-desist brief
- WIPO Arbitration and Mediation Center (voor generieke TLD's)
- SIDN-procedure (voor .nl)
- Kort geding bij de rechtbank
- Bodemzaak (handelsnaamrecht / merkenrecht / onrechtmatige daad)

**Stap 5 — Beschermingsstrategie**
Geef proactief strategisch advies:
- Registreer naam als merk (zo snel mogelijk)
- Registreer relevante domeinnaamvarianten (.nl, .com, .eu, spellingsvarianten)
- Monitor nieuwregistraties (merkbewaking)
- Documenteer gebruik als handelsnaam (bewijspositie)

---

## Output

Sla uitgewerkte analyses op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
