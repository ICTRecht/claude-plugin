---
name: contract-review
description: Beoordeel een contract volledig op risico's, ontbrekende bepalingen en juridische kwetsbaarheden.
argument-hint: "[plak contracttekst of geef bestandspad]"
---

# Contract Review

Voer een grondige juridische beoordeling uit van een contract op risico's, ontbrekende bepalingen en juridische kwetsbaarheden, met concrete verbeterpunten.

## Voorbereiding

Laad het organisatieprofiel via de volgende prioriteitsvolgorde:
1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` — gebruik de waarden voor context.
2. Als dat bestand niet bestaat: zoek in het Claude-geheugen naar **"ICTRecht organisatieprofiel"**.
3. Als dat ook ontbreekt: zoek in de project instructions naar het blok `## ICTRecht Profiel`.
4. Als geen van de drie bronnen beschikbaar is: ga door met generieke BW-standaardinstellingen en toon:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-legal-counsel:cold-start-interview` uit voor gepersonaliseerde analyses. Nu wordt voortgegaan met generieke Nederlandse rechtsstandaarden.*

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

## Werkwijze

### Stap 1 — Voorbereiding en context

Vraag (indien niet opgegeven als argument):
- Wat voor type contract betreft het? (bijv. softwarelicentie, dienstverlening, agentuurovereenkomst, koop, SaaS, etc.)
- Wie zijn de contractpartijen en wat is hun rol?
- Welk recht is van toepassing (indien vermeld in het contract)?
- Wat is de positie van de gebruiker: opdrachtgever, opdrachtnemer, of neutraal?

Lees vervolgens de aangeleverde contracttekst.

### Stap 2 — Structuurcheck

Controleer of alle standaardelementen aanwezig zijn. Gebruik een checklist:

| Element | Aanwezig | Opmerking |
|---|---|---|
| Identificatie partijen | | |
| Omschrijving object/dienst | | |
| Prijs en betalingsvoorwaarden | | |
| Looptijd en verlenging | | |
| Beëindigingsgronden | | |
| Aansprakelijkheidsbeperking | | |
| Intellectueel eigendom | | |
| Geheimhouding | | |
| Toepasselijk recht | | |
| Forumkeuze / arbitrage | | |
| Overmacht | | |
| Wijzigingsprocedure | | |

### Stap 3 — Risicoanalyse per clausule

Analyseer elke relevante clausule aan de hand van:
- BW boek 6 (verbintenissenrecht: wanprestatie, onrechtmatige daad, schadevergoeding)
- IT-contractenrechtelijke beginselen (specifiek voor software, data, dienstverlening)
- Positie van de gebruiker (welke clausules zijn nadelig voor hen?)

Geef per risico:
- Clausule of artikel
- Wat het risico is
- Beoordeling conform de ICTRecht-driedeling:
  - 🔴 **Kritiek punt (dealbreaker)** — strijd met dwingend recht, ongeldige afspraak of ontbrekend kernonderdeel
  - 🟠 **Risico** — juridisch ambigu, onvolledig of onredelijk verschoven verantwoordelijkheid
  - ⚡ **Aandachtspunt** — afwijking van best practice; verbetering aanbevolen

### Stap 4 — Rode vlaggen

Som alle kritieke punten op die directe aandacht vereisen:
- Ontbrekende aansprakelijkheidsbeperking of juist een onbeperkte aansprakelijkheid
- Eenzijdige wijzigingsbevoegdheid
- Ontbrekende beëindigingsmogelijkheden
- Onduidelijke intellectueel eigendomsoverdracht
- Onredelijke boeteclausules
- Ontbrekende of onduidelijke geheimhoudingsbepalingen

### Stap 5 — Aanbevelingen

Geef per rode vlag of risico een concrete tekstsuggestie voor aanpassing of aanvulling. Gebruik de volgende structuur:

**Clausule:** [naam/nummer]
**Beoordeling:** 🔴 Kritiek punt / 🟠 Risico / ⚡ Aandachtspunt
**Huidig:** [huidige tekst of samenvatting]
**Risico:** [uitleg]
**Voorstel:** [concrete herformulering of aanvulling]

Groepeer: eerst 🔴 kritieke punten, dan 🟠 risico's, dan ⚡ aandachtspunten. Sluit af met een samenvattende tabel (Clausule | Bevinding | Korte samenvatting).

---

## Output

Sla de output op als:
`~/.claude/plugins/config/ictrecht-legal-counsel/outputs/contract-review-[datum]-[onderwerp].md`

Als opslaan niet mogelijk is, toon de volledige analyse in de chat.

---

Sluit af met de standaard ICTRecht disclaimer.
