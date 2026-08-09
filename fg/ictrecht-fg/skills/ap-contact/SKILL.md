---
name: ap-contact
description: >
  Bereid als FG het contact met de Autoriteit Persoonsgegevens voor, inclusief
  een voorafgaande raadpleging (art. 36 AVG). Gebruik dit als de FG contact moet
  opnemen met de AP, een DPIA een hoog restrisico aangeeft, of de organisatie
  een vraag van de AP moet beantwoorden.
argument-hint: "[aanleiding: DPIA met restrisico, AP-vraag, of ander contactmoment]"
---

# /ictrecht-fg:ap-contact

Bereid het contact met de Autoriteit Persoonsgegevens voor, conform AVG artikel 36 en artikel 39 lid 1 sub d en e.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** de FG is het aangewezen eerste aanspreekpunt voor de toezichthouder over alle
aangelegenheden die de verwerking betreffen (art. 39 lid 1 sub d en e) — de FG mag de AP
ook zelf actief benaderen, bijvoorbeeld voor informatie over rechtmatige verwerkingen (art.
57 lid 1 sub d). Dit is een van de weinige FG-taken die inhoudelijk verder gaat dan alleen
adviseren: de FG voert dit contact zelf.

## Stap 1 — Aanleiding bepalen

Stel vast welk type contactmoment het betreft:

| Aanleiding | Grondslag | Vereist |
|---|---|---|
| DPIA wijst op een hoog restrisico dat niet met redelijke middelen is te beperken | Art. 36 lid 1 | Voorafgaande raadpleging vóór start van de verwerking |
| De AP stelt een vraag of doet onderzoek | Art. 31 (medewerkingsplicht), art. 39 lid 1 sub d | Tijdige, volledige beantwoording |
| De FG wil zelf informatie inwinnen over een rechtmatige verwerking | Art. 57 lid 1 sub d | Geen — dit mag proactief |

## Stap 2 — Voorafgaande raadpleging (art. 36) voorbereiden

Als de aanleiding een hoog restrisico uit een DPIA is, stel de raadpleging samen met:
- Een samenvatting van de betrokken verwerking en de rollen van eventuele gezamenlijke verwerkingsverantwoordelijken (art. 36 lid 3 sub a).
- Het doel en de middelen van de voorgenomen verwerking (art. 36 lid 3 sub b).
- De maatregelen en waarborgen die al zijn getroffen (art. 36 lid 3 sub c).
- De contactgegevens van de FG (art. 36 lid 3 sub d).
- De DPIA zelf (art. 36 lid 3 sub e).
- Overige door de AP gevraagde informatie (art. 36 lid 3 sub f).

**Let op:** de verwerking mag niet starten voordat de raadpleging is afgerond. De AP heeft in beginsel acht weken (verlengbaar met zes weken bij complexe zaken) om te reageren.

## Stap 3 — Reactie op een AP-vraag voorbereiden

Als de aanleiding een vraag of onderzoek van de AP is:
- Stel vast wat precies wordt gevraagd en binnen welke termijn.
- Verzamel de relevante documentatie (verwerkingsregister, DPIA, verwerkersovereenkomsten, datalekregistratie).
- Formuleer een feitelijk, volledig antwoord — de medewerkingsplicht (art. 31) laat geen ruimte om informatie achter te houden.

## Stap 4 — Concept opstellen

Stel het concept-document op (raadplegingsverzoek of antwoordbrief), met:
- Contactgegevens van de FG als eerste aanspreekpunt.
- Een heldere, feitelijke toon zonder juridisch pleidooi — de AP toetst, de FG informeert.

## Stap 5 — Output

Schrijf het concept naar `~/.claude/plugins/config/ictrecht-fg/outputs/ap-contact-[datum]-[onderwerp].md`.
Als dat pad niet beschikbaar is, toon het volledige concept in de chat.

Sluit af met de standaard ICTRecht disclaimer.
