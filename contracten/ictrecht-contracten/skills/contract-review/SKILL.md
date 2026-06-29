---
name: contract-review
description: Beoordeel een contract volledig op risico's, ontbrekende bepalingen en juridische kwetsbaarheden.
argument-hint: "[plak contracttekst of geef bestandspad]"
---

# Contract Review

Voer een grondige juridische beoordeling uit van een contract op risico's, ontbrekende bepalingen en juridische kwetsbaarheden, met concrete verbeterpunten.

## Voorbereiding

Laad het organisatieprofiel via de volgende prioriteitsvolgorde:
1. Lees `~/.claude/plugins/config/ictrecht-contracten/CLAUDE.md` — gebruik de waarden voor context.
2. Als dat bestand niet bestaat: zoek in het Claude-geheugen naar **"ICTRecht Contracten organisatieprofiel"**.
3. Als dat ook ontbreekt: zoek in de project instructions naar het blok `## ICTRecht Contracten Profiel`.
4. Als geen van de drie bronnen beschikbaar is: ga door met generieke BW-standaardinstellingen en toon:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-contracten:cold-start-interview` uit voor gepersonaliseerde analyses. Nu wordt voortgegaan met generieke Nederlandse rechtsstandaarden.*

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
- Ernst: 🔴 Hoog / 🟡 Middel / 🟢 Laag

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
**Huidig:** [huidige tekst of samenvatting]
**Risico:** [uitleg]
**Voorstel:** [concrete herformulering of aanvulling]

---

## Output

Sla de output op als:
`~/.claude/plugins/config/ictrecht-contracten/outputs/contract-review-[datum]-[onderwerp].md`

Als opslaan niet mogelijk is, toon de volledige analyse in de chat.

---

Sluit af met de standaard ICTRecht disclaimer.
