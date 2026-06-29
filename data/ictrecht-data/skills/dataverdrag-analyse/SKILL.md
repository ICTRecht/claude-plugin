# Skill: dataverdrag-analyse

**Naam:** dataverdrag-analyse
**Beschrijving:** Analyseer internationale dataverdragen en grensoverschrijdend dataverkeer buiten de AVG-context.
**Argument-hint:** `[verdrag, land of situatie]`

---

## Voorbereiding

Controleer in deze volgorde of er organisatiecontext beschikbaar is:

1. **Configuratiebestand:** `~/.claude/plugins/config/ictrecht-data/CLAUDE.md` — lees dit bestand als het bestaat.
2. **Geheugen:** Zoek naar geheugenblokken met de titel "ICTRecht Data organisatieprofiel".
3. **Project-instructies:** Zoek naar een sectie `## ICTRecht Data Profiel` in de projectinstructies.

Als geen van de drie bronnen beschikbaar is: ga generiek te werk en voeg onderaan een ℹ️-melding toe:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-data:cold-start-interview` uit voor gepersonaliseerde analyses.*

---

## Workflow

### Stap 1 — Context in kaart brengen

Stel de volgende vragen indien niet reeds beantwoord door het argument of het organisatieprofiel:
- Welke data is betrokken (type, gevoeligheid, volume)?
- Welke landen zijn betrokken (zowel aan zend- als ontvangzijde)?
- Wat is de aanleiding (juridische vraag, contractonderhandeling, overheidsverzoek, compliance-check)?
- Is er al een verdrag of rechtsinstrument geïdentificeerd?

### Stap 2 — Is de AVG van toepassing?

Beoordeel of de data persoonsgegevens bevat:
- **Ja:** AVG is van toepassing (doorgifte buiten EER vereist grondslag: adequaatheidsbesluit, SCC's, bindende bedrijfsvoorschriften of uitzonderingen art. 49 AVG)
- **Nee:** AVG is niet van toepassing; andere juridische kaders zijn relevant
- **Gemengd:** beide regimes kunnen gelden

Bij niet-persoonsgebonden data: de EU Data Act, nationale wetgeving en internationale verdragen zijn het primaire kader.

### Stap 3 — Sectorale verdragen en regelgeving

Beoordeel welke internationale instrumenten van toepassing zijn:

**Strafrecht en overheidsverzoeken:**
- **e-Evidence Verordening (EU) 2023/1543** — grensoverschrijdende toegang tot elektronisch bewijs binnen de EU
- **CLOUD Act (VS)** — Amerikaanse autoriteiten kunnen data opvragen bij Amerikaanse aanbieders, ongeacht opslaglocatie; spanningsverhouding met AVG
- **Budapest Convention (Cybercrimeverdrag)** — internationaal kader voor grensoverschrijdende toegang tot elektronisch bewijs

**Financieel en fiscaal:**
- **FATCA** — Amerikaanse rapportageverplichting voor buitenlandse financiële instellingen
- **CRS/AEOI** — automatische uitwisseling van financiële gegevens (OESO-kader)
- **DAC6/DAC7** — EU-richtlijnen voor uitwisseling van fiscale gegevens

**Gezondheidsdata:**
- **EHDS (European Health Data Space)** — primair en secundair gebruik van gezondheidsdata
- Bilaterale gezondheidsverdragen en WHO-instrumenten

**Overig:**
- Bilaterale investeringsverdragen met data-bepalingen
- WTO GATS — dienstenhandel en data-lokalisatieverplichtingen
- EU-UK Trade and Cooperation Agreement — datadoorgifteregeling na Brexit

### Stap 4 — Spanning tussen verdragsverplichtingen en AVG

Identificeer concrete spanningspunten:

| Instrument | Verplichting | Spanning met AVG/EU-recht |
|-----------|-------------|--------------------------|
| CLOUD Act | Verplichte verstrekking aan VS-autoriteiten | Zonder rechtshulpverdrag: mogelijk strijd met AVG |
| FATCA | Doorgifte financiële gegevens naar VS | Adequaatheidsbesluit ontbreekt voor VS (na Schrems II) |
| e-Evidence | Verstrekking aan buitenlandse autoriteiten | Waarborgen grondrechten vereist |

Adviseer hoe met deze spanning om te gaan (legal analysis, contractuele waarborgen, escalatie).

### Stap 5 — Praktische risico's

Breng de praktische risico's in kaart:
- **Overheidsverzoeken:** kans op verzoeken van buitenlandse autoriteiten, meldplicht, responstijd
- **Conflicterende wettelijke verplichtingen:** organisatie zit tussen twee tegenstrijdige verplichtingen (comply with CLOUD Act vs. comply with GDPR)
- **Reputatierisico:** datadeling met autoritaire regimes of landen zonder adequaatheidsbesluiten
- **Contractuele aansprakelijkheid:** derde partij kan aansprakelijk stellen bij ongeautoriseerde verstrekking

### Stap 6 — Advies en mitigerende maatregelen

Lever een concreet advies:
- Welk verdrag of rechtskader is van toepassing?
- Wat zijn de verplichtingen en risico's?
- Welke mitigerende maatregelen zijn aanbevolen?
  - Contractuele clausules (bijv. meldplicht bij overheidsverzoeken)
  - Technische maatregelen (versleuteling, data-lokalisatie)
  - Organisatorische maatregelen (procedure voor overheidsverzoeken)
  - Escalatie naar juridisch adviseur of toezichthouder

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-data/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
