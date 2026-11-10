---
name: betrokkenen-contact
description: >
  Behandel als FG een rechtstreeks verzoek van een betrokkene (inzage, correctie,
  verwijdering, bezwaar, dataportabiliteit, beperking), conform AVG artikel 38 lid 4.
  Gebruik dit als een betrokkene zich met een privacyvraag of -verzoek tot de FG
  wendt, of als de FG de afhandeling van een verzoek wil toetsen.
argument-hint: "[type verzoek en context]"
---

# /ictrecht-fg:betrokkenen-contact

Behandel een rechtstreeks verzoek van een betrokkene aan de FG, conform AVG artikel 38 lid 4 en hoofdstuk III.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik je kennis van AVG hoofdstuk III (rechten van betrokkenen, art. 15–22).
3. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** de FG is voor betrokkenen het eerste aanspreekpunt over de verwerking van hun
gegevens en de uitoefening van hun rechten (art. 38 lid 4) — dat is een eigen wettelijke
FG-taak, los van wie het verzoek uiteindelijk uitvoert. De feitelijke afhandeling
(gegevens verzamelen, corrigeren, verwijderen) ligt bij de verwerkingsverantwoordelijke; de
FG begeleidt de betrokkene, beoordeelt de ontvankelijkheid en ziet toe op een correcte
afhandeling binnen de termijn.

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `376ab8c4-d17a-40c4-9031-45668128d27a`
   (AVG-Rechten Assistent) om je analyse te gronden in actuele ICTRecht-bronnen, naast je
   eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

## Stap 1 — Identificeer het type verzoek

| Type | AVG artikel | Termijn |
|---|---|---|
| Inzage | Art. 15 | 1 maand |
| Correctie | Art. 16 | 1 maand |
| Verwijdering ('recht op vergetelheid') | Art. 17 | 1 maand |
| Beperking verwerking | Art. 18 | 1 maand |
| Dataportabiliteit | Art. 20 | 1 maand |
| Bezwaar | Art. 21 | 1 maand |
| Rechten bij geautomatiseerde besluitvorming | Art. 22 | 1 maand |

Alle termijnen volgen uit art. 12 lid 3 AVG: reageer binnen één maand na ontvangst; verlenging met maximaal twee maanden is mogelijk bij complexe of talrijke verzoeken, mits de betrokkene binnen de eerste maand over de verlenging wordt geïnformeerd. Behandeling is in beginsel kosteloos; alleen bij kennelijk ongegronde of buitensporige verzoeken mag een redelijke vergoeding worden gevraagd of het verzoek worden geweigerd (art. 12 lid 5 AVG — motiveer dit).

## Stap 2 — Identiteitsverificatie

Is de identiteit van de verzoeker vastgesteld? Zo niet: vraag verificatie.
**Let op:** vraag niet meer gegevens dan nodig voor identificatie.

## Stap 3 — Is het verzoek ontvankelijk?

Controleer:
- Heeft de organisatie persoonsgegevens van deze persoon?
- Geldt een uitzondering? (raadpleeg je kennis van AVG art. 17 lid 3, 23 en nationale uitzonderingen)

Uitzonderingen bij recht op verwijdering (art. 17 lid 3):
- Wettelijke verplichting tot bewaring
- Archiefdoeleinden
- Juridische procedures

## Stap 4 — Doorgeleiden of toetsen

Bepaal wat de FG in dit geval doet:
- **Verzoek net binnengekomen bij de FG:** stel een conceptreactie op en geleid het verzoek voor feitelijke uitvoering door naar de verwerkingsverantwoordelijke of de betrokken afdeling. De FG legt het besluit niet zelf op, maar bewaakt de termijn.
- **Al afgehandeld verzoek, ter toetsing:** beoordeel of de gekozen uitkomst (inwilligen / gedeeltelijk / afwijzen) correct is onderbouwd en of de termijn is gehaald.

Mogelijke uitkomsten:
- **Inwilligen** → bevestig uitvoering
- **Gedeeltelijk inwilligen** → leg uit welk deel en waarom
- **Afwijzen** → onderbouw met artikel en uitzondering
- **Meer informatie nodig** → vraag specificatie

## Stap 5 — Output

Schrijf de conceptreactie of toets naar `~/.claude/plugins/config/ictrecht-fg/outputs/betrokkenen-contact-[datum]-[type].md`.
Als dat pad niet beschikbaar is, toon de volledige reactie in de chat.

Sluit af met de standaard ICTRecht disclaimer.
