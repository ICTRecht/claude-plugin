---
name: merkenrecht
description: >
  Analyseer merkenrechtelijke vragen over bescherming, inbreuk, registratie en conflict.
argument-hint: "[merk of situatie]"
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

**Stap 1 — Is het teken beschermbaar als merk?**
Beoordeel onderscheidend vermogen (sterk/zwak/beschrijvend). Toets absolute weigeringsgronden (art. 2.1 BVIE / art. 7 UMVo): beschrijvend, gebruikelijk, gebrek aan onderscheidend vermogen, misleidend, openbare orde.

**Stap 2 — Waar is het merk geregistreerd?**
Stel vast welk register van toepassing is:
- Benelux (BOIP / BBIE)
- Europese Unie (EUIPO — Uniemerk)
- Internationaal (WIPO Madrid-systeem)
Bespreek territorial scope en prioriteitsrechten.

**Stap 3 — Beschermingsomvang**
Analyseer de beschermingsomvang: waren en diensten (Nice-classificatie), soortgelijkheid, gevaar voor verwarring (Global appreciation-test: visuele, auditieve en begripsmatige overeenstemming). Bekendheid als verzwaarde bescherming.

**Stap 4 — Inbreukanalyse**
Beoordeel gebruik in het economisch verkeer (art. 2.20 lid 2 BVIE). Toets overeenstemming teken vs. merk en soortgelijkheid waren/diensten. Weeg verwarringsgevaar of ongerechtvaardigd voordeel/afbreuk aan bekendheid.

**Stap 5 — Opties**
Bespreek beschikbare acties:
- Sommatie / cease-and-desist
- Oppositieprocedure bij BOIP/EUIPO
- Nietigheidsvordering
- Inbreukprocedure (kort geding / bodemprocedure)
- Douane-actie (verordening 608/2013)

**Stap 6 — Merkenstrategie**
Geef strategisch advies: registratie aanbevelen, klassen uitbreiden, bewijs van gebruik, monitoring, licentie- of co-existentieovereenkomst.

---

## Output

Sla uitgewerkte analyses op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
