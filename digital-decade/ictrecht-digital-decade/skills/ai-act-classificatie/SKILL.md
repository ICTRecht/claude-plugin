# ai-act-classificatie

Classificeer een AI-systeem volgens de AI Act risicocategorieën en bepaal de verplichtingen.

## Metadata
- **name:** ai-act-classificatie
- **description:** Classificeer een AI-systeem volgens de AI Act risicocategorieën en bepaal de verplichtingen.
- **argument-hint:** "[beschrijving van het AI-systeem]"

## Voorbereiding (3-laags)

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht-digital-decade/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht Digital Decade organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Digital Decade Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-digital-decade:cold-start-interview` uit voor gepersonaliseerde analyse. Nu wordt generieke AI Act classificatie toegepast.*

## Instructies

Voer de volgende stappen uit voor het opgegeven AI-systeem:

### Stap 1 — Beschrijf het AI-systeem
Vat samen:
- Doel en beoogde werking van het systeem
- Gebruikers (wie interageert met het systeem?)
- Context van gebruik (sector, toepassing, schaal)
- Technologie (machine learning, LLM, computer vision, etc.)

Vraag om verduidelijking als de beschrijving onvoldoende is voor classificatie.

### Stap 2 — Verboden AI-praktijken toetsen (AI Act art. 5)
Toets of het systeem valt onder een van de verboden praktijken:
- Subliminale manipulatie van gedrag
- Misbruik van kwetsbare groepen
- Sociale scoring door overheden
- Real-time biometrische identificatie op afstand in openbare ruimten (met beperkte uitzonderingen)
- Emotieherkenning op werkplek of onderwijs
- Biometrische categorisering op basis van gevoelige kenmerken
- Predictive policing op basis van persoonskenmerken

**Conclusie:** Verboden? → Stop hier en adviseer. Niet verboden? → Door naar Stap 3.

### Stap 3 — Hoog-risico classificatie (Bijlage III AI Act)
Controleer of het systeem valt onder een van de hoog-risico categorieën:
- Kritieke infrastructuur (energie, water, transport)
- Onderwijs en beroepsopleiding (toegang, beoordeling)
- Werkgelegenheid (werving, ontslag, prestatiebeoordeling)
- Essentiële private/publieke diensten (krediet, sociale voorzieningen)
- Wetshandhaving (risicobeoordeling, bewijsanalyse)
- Migratie en grenscontrole
- Rechtsbedeling en democratische processen
- Veiligheidscomponenten van producten (Bijlage I Richtlijn machines, medische apparatuur, etc.)

**Conclusie:** Hoog-risico? → Noteer en ga naar Stap 6.

### Stap 4 — GPAI-modellen (art. 51 AI Act)
Is het systeem een General Purpose AI model?
- Getraind op grote hoeveelheid data, kan diverse taken uitvoeren?
- Systeemrisico: getraind met meer dan 10^25 FLOP? (aanwijzing voor hoog systeemrisico)

**Conclusie:** GPAI met systeemrisico → aanvullende verplichtingen art. 55.

### Stap 5 — Overige systemen
Als niet verboden en niet hoog-risico:
- **Transparantieverplichtingen** (art. 50): chatbots, deepfakes, AI-gegenereerde content → melding aan gebruiker verplicht
- **Laag risico:** aanbevelingssystemen, spam filters → geen verplichte maatregelen, wel AI-geletterdheid (art. 4)
- **Minimaal risico:** AI in videogames, eenvoudige automatisering → vrij te gebruiken

### Stap 6 — Verplichtingen per categorie
Stel een verplichtingenmatrix op:

| Verplichting | Van toepassing? | Toelichting |
|---|---|---|
| Conformiteitsbeoordeling | | |
| Registratie in EU-database | | |
| Technische documentatie (Bijlage IV) | | |
| Risicobeheerssysteem | | |
| Data governance | | |
| Logging en monitoring | | |
| Menselijk toezicht | | |
| Nauwkeurigheid, robuustheid, cybersecurity | | |
| Transparantie naar gebruikers | | |
| Post-market monitoring | | |

### Output
Sla de classificatie op naar `~/.claude/plugins/config/ictrecht-digital-decade/outputs/ai-act-classificatie-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
