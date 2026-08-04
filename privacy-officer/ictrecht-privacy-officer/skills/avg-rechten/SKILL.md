---
name: avg-rechten
description: >
  Behandel een verzoek van een betrokkene (inzage, correctie, verwijdering, bezwaar,
  dataportabiliteit, beperking). Gebruik dit als iemand een privacyverzoek ontvangt
  of wil weten hoe te reageren op een verzoek van een burger of klant.
argument-hint: "[type verzoek en context]"
---

# /ictrecht-privacy-officer:avg-rechten

Behandel een verzoek van een betrokkene conform AVG hoofdstuk III.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy-officer:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik je kennis van AVG hoofdstuk III (rechten van betrokkenen, art. 15–22).
3. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

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

## Stap 4 — Reactie opstellen

Stel een conceptreactie op. Toon en niveau conform CLAUDE.md.

Mogelijke uitkomsten:
- **Inwilligen** → bevestig uitvoering
- **Gedeeltelijk inwilligen** → leg uit welk deel en waarom
- **Afwijzen** → onderbouw met artikel en uitzondering
- **Meer informatie nodig** → vraag specificatie

## Stap 5 — Output

Schrijf concept-reactiebrief naar `~/.claude/plugins/config/ictrecht-privacy-officer/outputs/avg-verzoek-[datum]-[type].md`.
Als dat pad niet beschikbaar is, toon de volledige reactiebrief in de chat.

Sluit af met de standaard ICTRecht disclaimer.
