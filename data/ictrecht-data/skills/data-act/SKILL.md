# Skill: data-act

**Naam:** data-act
**Beschrijving:** Analyseer de verplichtingen van de EU Data Act voor een product, dienst of organisatie.
**Argument-hint:** `[product, dienst of situatie]`

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

### Stap 1 — Is de Data Act van toepassing?

Beoordeel aan de hand van art. 1 en 2 Data Act of de verordening van toepassing is:

**Connected product:** een product dat data genereert of verzamelt via sensoren of andere middelen, en dat data kan communiceren via een netwerk (bijv. IoT-apparaten, slimme apparaten, voertuigen, medische hulpmiddelen).

**Related service:** een digitale dienst die noodzakelijk is voor de werking van het connected product, of die specifiek is ontworpen om het product een bepaalde functie te geven (bijv. bijbehorende apps, cloud-diensten).

Concludeer:
- Valt het product/de dienst onder de definitie? (ja / nee / nader onderzoek vereist)
- Is de organisatie data holder, data recipient, of gebruiker in de zin van de Data Act?

### Stap 2 — Data holder verplichtingen

Indien de organisatie kwalificeert als **data holder**:

**Art. 4 — Toegangsrecht van de gebruiker:**
- De gebruiker heeft recht op toegang tot data gegenereerd door gebruik van het connected product
- Data moet direct en gratis toegankelijk zijn, voor zover technisch mogelijk
- Data moet toegankelijk zijn in een gestructureerd, gangbaar en machine-leesbaar formaat

**Art. 5 — Toegang door derde partijen op verzoek van de gebruiker:**
- De data holder moet data delen met een derde aangewezen door de gebruiker
- Voorwaarden: het verzoek moet worden nageleefd onverwijld en kosteloos (of tegen redelijke vergoeding bij B2B)
- De data holder mag het verzoek alleen weigeren op limitatieve gronden (bijv. bedrijfsgeheimen)

### Stap 3 — Data recipient rechten en plichten

Indien de organisatie kwalificeert als **data recipient** (art. 6 Data Act):
- Data mag uitsluitend worden gebruikt voor de overeengekomen doeleinden
- Verbod op gebruik van data voor profilering van natuurlijke personen
- Verbod op doorverkoop van data of gebruik voor ontwikkeling van concurrerende producten
- Data moet worden verwijderd zodra het doel is bereikt, tenzij anders overeengekomen

### Stap 4 — Portabiliteit en cloud switching

**Art. 23-31 — Switching van cloud-diensten:**
- Aanbieders van clouddiensten moeten switching faciliteren
- Maximale uitfaseerperiode: 12 maanden (later teruggebracht)
- Exportformaten moeten interoperabel zijn
- Switching-kosten mogen na transitieperiode niet worden berekend

Beoordeel of de organisatie als afnemer of aanbieder van clouddiensten hieraan voldoet of hiervan profiteert.

### Stap 5 — Verhouding tot de AVG

Maak onderscheid tussen:
- **Niet-persoonsgebonden data** — valt primair onder de Data Act
- **Persoonsgegevens** — valt onder de AVG én de Data Act (cumulatieve toepassing)
- **Gemengde datasets** — beide regimes van toepassing; anonimisering kan AVG-verplichtingen wegnemen maar is niet altijd haalbaar

Signaleer spanning: de Data Act-verplichting tot datadeling kan botsen met de AVG-verplichting tot dataminimalisatie of doelbinding.

### Stap 6 — Actieplan compliance

Lever een concreet actieplan:

| Actie | Artikel | Prioriteit | Verantwoordelijke |
|-------|---------|-----------|------------------|
| ... | ... | Hoog/Middel/Laag | ... |

Inclusief:
- Contractuele aanpassingen (leveringsvoorwaarden, SLA's, data sharing agreements)
- Technische maatregelen (API's voor data-toegang, exportfunctionaliteit)
- Beleidsmaatregelen (procedure voor verzoeken gebruikers, retentiebeleid)

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-data/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
