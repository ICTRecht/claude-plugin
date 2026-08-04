---
name: ai-act-classificatie
description: >
  Classificeer een AI-systeem volgens de AI Act risicocategorieën en bepaal de verplichtingen.
argument-hint: "[beschrijving van het AI-systeem]"
---

## Metadata
- **name:** ai-act-classificatie
- **description:** Classificeer een AI-systeem volgens de AI Act risicocategorieën en bepaal de verplichtingen.
- **argument-hint:** "[beschrijving van het AI-systeem]"

## Voorbereiding (3-laags)

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-compliance-officer:cold-start-interview` uit voor gepersonaliseerde analyse. Nu wordt generieke AI Act classificatie toegepast.*

Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `PLACEHOLDER_COLLECTION_ID`
   <!-- Nog geen kennisbank-backend beschikbaar voor dit domein --> om je analyse te gronden
   in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

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
- Subliminale of manipulatieve technieken die gedrag wezenlijk verstoren
- Misbruik van kwetsbaarheden (leeftijd, handicap, sociaaleconomische situatie)
- Sociale scoring (door overheden én private partijen)
- Risicobeoordeling van strafbare feiten uitsluitend op basis van profilering of persoonskenmerken
- Ongerichte scraping van gezichtsafbeeldingen voor gezichtsherkenningsdatabases
- Emotieherkenning op de werkplek of in het onderwijs (m.u.v. medische of veiligheidsdoeleinden)
- Biometrische categorisering op basis van gevoelige kenmerken
- Real-time biometrische identificatie op afstand in openbare ruimten t.b.v. rechtshandhaving (met beperkte uitzonderingen)

**Let op:** deze verboden gelden al sinds 2 februari 2025.

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

**Uitzondering (art. 6 lid 3):** een Bijlage III-systeem is toch níet hoog-risico als het geen significant risico vormt voor gezondheid, veiligheid of grondrechten (bijv. een enge procedurele of louter voorbereidende taak). Uitzondering geldt nooit bij profilering van natuurlijke personen. Documenteer en registreer deze beoordeling.

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

### Stap 7 — Tijdlijn en toezicht
- **2 februari 2025:** verboden praktijken (art. 5) en AI-geletterdheid (art. 4) van kracht
- **2 augustus 2025:** verplichtingen GPAI-modellen en governancestructuur van kracht
- **2 augustus 2026:** verplichtingen voor hoog-risicosystemen (Bijlage III) en transparantieverplichtingen (art. 50) volledig van toepassing
- **2 augustus 2027:** hoog-risico als veiligheidscomponent onder Bijlage I-productwetgeving
- **Nederland:** toezicht wordt sectoraal belegd; de AP (coördinatie algoritmetoezicht) en de RDI spelen een centrale rol — controleer de actuele aanwijzing van markttoezichtautoriteiten.

### Output
Sla de classificatie op naar `~/.claude/plugins/config/ictrecht-compliance-officer/outputs/ai-act-classificatie-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
