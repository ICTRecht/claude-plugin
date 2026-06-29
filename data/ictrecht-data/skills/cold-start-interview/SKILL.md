# Skill: cold-start-interview

**Naam:** cold-start-interview
**Prefix:** `/ictrecht-data:`
**Beschrijving:** Stel een organisatieprofiel op voor de ICTRecht Data plugin via een gestructureerd interview.

---

## Voorbereiding

Controleer in deze volgorde of er al profielinformatie beschikbaar is:

1. **Configuratiebestand:** `~/.claude/plugins/config/ictrecht-data/CLAUDE.md` — lees dit bestand als het bestaat en sla de reeds bekende velden over.
2. **Geheugen:** Zoek naar geheugenblokken met de titel "ICTRecht Data organisatieprofiel".
3. **Project-instructies:** Zoek naar een sectie `## ICTRecht Data Profiel` in de projectinstructies.

Als alle velden al zijn ingevuld: meld dit aan de gebruiker en sla het interview over. Bied aan specifieke velden bij te werken indien gewenst.

---

## Interview

Stel de volgende vragen in een vriendelijke, professionele toon. Stel maximaal twee vragen tegelijk. Wacht op antwoord voor je verdergaat.

**Blok 1 — Organisatie:**
1. Wat is de naam en sector van uw organisatie?
2. Wat is de omvang van de organisatie (bijv. aantal medewerkers of type: mkb / overheid / groot bedrijf)?

**Blok 2 — Datarol:**
3. Wat is de rol van uw organisatie ten opzichte van data? Kies één of meerdere:
   - **Data producer** — u genereert data (bijv. IoT-sensoren, systemen)
   - **Data holder** — u beheert en controleert data
   - **Data recipient** — u ontvangt data van anderen
   - **Platform** — u faciliteert data-uitwisseling tussen partijen
4. In welke landen is uw organisatie gevestigd of actief?

**Blok 3 — Governance en wetgeving:**
5. Welke wetgeving is op uw organisatie van toepassing? (bijv. AVG, EU Data Act, Open Data Richtlijn, sectorspecifieke regelgeving zoals NIS2, DORA, AI Act)
6. Heeft uw organisatie al een data governance structuur? Zo ja: wie is verantwoordelijk (bijv. CDO, DPO, juridische afdeling)?

**Blok 4 — Verwerkingsregister en contact:**
7. Wat is de huidige status van het verwerkingsregister? (aanwezig en actueel / in opbouw / ontbreekt)
8. Wie is het juridisch contactpersoon voor datavraagstukken binnen uw organisatie?

**Blok 5 — Gebruiker en niveau:**
9. Wat is uw rol? (bijv. data officer, privacy officer, juridisch adviseur, compliance manager)
10. Voor welk publiek worden outputs primair opgesteld? (intern gebruik / extern / bestuursniveau)

---

## Opslaan — standaard 3-save patroon

Na afronding van het interview: sla het profiel op via de drie onderstaande methoden.

### Stap 1 — Schrijf configuratiebestand

Schrijf het ingevulde profiel naar:
`~/.claude/plugins/config/ictrecht-data/CLAUDE.md`

Gebruik de CLAUDE.md template uit de plugin root als basis en vervang alle `[PLACEHOLDER]`-velden door de gegeven antwoorden.

Maak de map aan als die nog niet bestaat:
`~/.claude/plugins/config/ictrecht-data/`

### Stap 2 — Sla op in geheugen

Sla een geheugenblok op met:
- **Titel:** `ICTRecht Data organisatieprofiel`
- **Inhoud:** kernvelden uit het interview (naam, sector, datarol, wetgeving, verwerkingsregisterstatus, juridisch contact)

### Stap 3 — Bevestig aan gebruiker

Toon een overzicht van het opgeslagen profiel en meld:

> "Uw organisatieprofiel is opgeslagen. U kunt nu alle `/ictrecht-data:`-skills gebruiken met uw organisatiecontext. Gebruik `/ictrecht-data:cold-start-interview` opnieuw om het profiel bij te werken."

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-data/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
