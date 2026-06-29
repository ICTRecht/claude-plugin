# Skill: data-sharing

**Naam:** data-sharing
**Beschrijving:** Beoordeel of stel een data sharing agreement op voor het delen van data tussen organisaties.
**Argument-hint:** `[data, partijen en doel]`

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

Stel de volgende vragen indien niet reeds beantwoord door het argument:
- Welke data wordt gedeeld (type, gevoeligheid, bevat het persoonsgegevens)?
- Tussen welke partijen vindt het delen plaats (namen, rollen, landen)?
- Voor welk doel wordt de data gedeeld?
- Is de data-uitwisseling eenmalig of structureel?

### Stap 2 — Juridische kwalificatie

Beoordeel de juridische relatie tussen de partijen:

**AVG-kwalificatie (indien persoonsgegevens):**
- Gezamenlijke verwerkingsverantwoordelijkheid (art. 26 AVG) — beide partijen bepalen doel en middelen
- Verwerkersrelatie (art. 28 AVG) — één partij verwerkt in opdracht van de ander
- Verstrekking aan derde (art. 6 AVG) — ontvangende partij is zelfstandig verwerkingsverantwoordelijke

**Data Act-kwalificatie (indien van toepassing):**
- Is er sprake van een connected product of related service (art. 2 Data Act)?
- Wie is de data holder en wie is de data recipient?

### Stap 3 — Kernbepalingen data sharing agreement

Zorg dat de volgende bepalingen zijn opgenomen of beoordeeld:

| Bepaling | Aandachtspunten |
|----------|----------------|
| Definities | Data, partijen, rollen, vertrouwelijke informatie |
| Doelbeperking | Data mag alleen voor het overeengekomen doel worden gebruikt |
| Toegangsrechten | Wie heeft toegang, op welke systemen, met welke autorisaties |
| Beveiligingsvereisten | Minimumstandaarden, incidentmelding, audit |
| Retentie | Hoe lang mag de data worden bewaard door de ontvanger |
| Teruggave en verwijdering | Bij beëindiging: teruggave of aantoonbare verwijdering |
| Aansprakelijkheid | Verdeling bij datalekken, schendingen, claims van betrokkenen |
| Doorgiften naar derde landen | Grondslag, SCC, aanvullende maatregelen (Transfer Impact Assessment) |

### Stap 4 — Data Act verplichtingen

Indien de Data Act van toepassing is:
- **Art. 4:** Recht van de gebruiker op toegang tot data gegenereerd door gebruik van connected product
- **Art. 5:** Data holder moet data op verzoek beschikbaar stellen aan derde partijen aangewezen door de gebruiker
- **Art. 6:** Data recipient mag data alleen gebruiken voor overeengekomen doeleinden, geen gebruik voor profilering, geen doorverkoop

Beoordeel of de data sharing agreement hieraan voldoet of hierin moet voorzien.

### Stap 5 — Rode vlaggen en aanbevelingen

Signaleer:
- Ontbrekende of te ruime doelomschrijvingen
- Ontbrekende beveiligingsverplichtingen of -standaarden
- Onduidelijke kwalificatie van de juridische relatie (risico: verkeerde overeenkomst)
- Doorgiften naar derde landen zonder geldige grondslag
- Afwezigheid van incidentmeldplicht richting de andere partij

Sluit af met geprioriteerde aanbevelingen.

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-data/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
