---
name: avg-rechten
description: >
  Behandel een verzoek van een betrokkene (inzage, correctie, verwijdering, bezwaar,
  dataportabiliteit, beperking). Gebruik dit als iemand een privacyverzoek ontvangt
  of wil weten hoe te reageren op een verzoek van een burger of klant.
argument-hint: "[type verzoek en context]"
---

# /ictrecht-privacy:avg-rechten

Behandel een verzoek van een betrokkene conform AVG hoofdstuk III.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht-privacy/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht Privacy organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Privacy Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik `search_avg_rechten` voor de relevante rechten en uitzonderingen.

## Stap 1 — Identificeer het type verzoek

| Type | AVG artikel | Termijn |
|---|---|---|
| Inzage | Art. 15 | 1 maand (max. 3 maanden) |
| Correctie | Art. 16 | 1 maand |
| Verwijdering ('recht op vergetelheid') | Art. 17 | 1 maand |
| Beperking verwerking | Art. 18 | 1 maand |
| Dataportabiliteit | Art. 20 | 1 maand |
| Bezwaar | Art. 21 | Zo snel mogelijk |
| Niet onderworpen aan geautomatiseerde besluitvorming | Art. 22 | 1 maand |

## Stap 2 — Identiteitsverificatie

Is de identiteit van de verzoeker vastgesteld? Zo niet: vraag verificatie.
**Let op:** vraag niet meer gegevens dan nodig voor identificatie.

## Stap 3 — Is het verzoek ontvankelijk?

Controleer:
- Heeft de organisatie persoonsgegevens van deze persoon?
- Geldt een uitzondering? (gebruik `search_avg_rechten`)

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

Schrijf concept-reactiebrief naar `~/.claude/plugins/config/ictrecht-privacy/outputs/avg-verzoek-[datum]-[type].md`.
Als dat pad niet beschikbaar is, toon de volledige reactiebrief in de chat.

Sluit af met de standaard ICTRecht disclaimer.
