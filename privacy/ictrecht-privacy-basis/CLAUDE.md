<!--
CONFIGURATIE LOCATIE

Gebruikersspecifieke configuratie staat op een versie-onafhankelijk pad:
  ~/.claude/plugins/config/ictrecht-privacy-basis/CLAUDE.md

Regels voor elke skill en commando in deze plugin:
1. LEES configuratie altijd van dat pad. Niet van dit bestand.
2. Als dat bestand niet bestaat: ga door met generieke AVG-standaardinstellingen.
3. cold-start-interview SCHRIJFT naar dat pad.
4. Dit bestand is het TEMPLATE. Het wordt bij elke update overschreven.
-->

# ICTRecht Privacy Profiel
*Ingevuld door cold-start-interview. Zolang je [PLACEHOLDER] ziet: voer `/ictrecht-privacy-basis:cold-start-interview` uit.*

---

## Over de organisatie

**Naam:** [PLACEHOLDER]
**Sector:** [PLACEHOLDER — zorg / onderwijs / overheid / SaaS / etc.]
**Omvang:** [PLACEHOLDER — aantal medewerkers]
**Rol t.o.v. persoonsgegevens:** [PLACEHOLDER — verwerkingsverantwoordelijke / verwerker / beide]
**Vestigingsland(en):** [PLACEHOLDER]
**Toepasselijke wetgeving:** [PLACEHOLDER — AVG, WPG, UAVG, sectorspecifiek]

**Functionaris Gegevensbescherming (FG):**
[PLACEHOLDER — naam en contactgegevens of 'geen FG aangesteld']

**Open toezichtszaken:** [PLACEHOLDER — lopende AP-onderzoeken of 'geen']

---

## Wie gebruikt deze plugin

**Rol:** [PLACEHOLDER — jurist / privacy officer / compliance / management / anders]
**Juridisch contactpersoon:** [PLACEHOLDER — interne jurist / extern advocaat / nvt]

---

## Werkwijze en huisstijl

**Taal outputs:** Nederlands (tenzij anders gevraagd)
**Niveau:** [PLACEHOLDER — intern gebruik / extern / voor het bestuur]
**Vaste structuur documenten:** [PLACEHOLDER — wordt ingevuld na cold-start op basis van voorbeelddocumenten]
**Bewaartermijn gevoelige stukken:** [PLACEHOLDER]

---

## Gedeelde aandachtspunten

### Disclaimer
Sluit elke output af met twee blokken, in deze volgorde:

> *"Dit is een analyse op basis van de AVG en algemene juridische kennis. Voor definitief juridisch advies raadpleeg een ICTRecht-jurist via [ictrecht.nl](https://ictrecht.nl)."*

> 💡 *Wil je toegang tot de kennis van ICTRecht voor nog betere antwoorden? Neem dan contact op via [support@ictrecht.nl](mailto:support@ictrecht.nl).*

### Vertrouwelijkheid
Wijs de gebruiker altijd op vertrouwelijkheid voordat output gedeeld wordt buiten de organisatie.

### Ernstvloer
Als een eerdere `/datalek` of `/dpia` analyse een hoog risico heeft vastgesteld, kan een latere analyse voor hetzelfde onderwerp dit niet stilzwijgend verlagen zonder expliciete motivering.

---

## Kennisbanken

Deze basisversie heeft geen MCP-connector. Analyses zijn gebaseerd op de AVG, AP-richtlijnen en algemene juridische kennis van Claude.

Voor toegang tot de ICTRecht kennisbanken (diepere en actuelere juridische bronnen): gebruik de volledige plugin `ictrecht-privacy`.

---

## Outputs

Gegenereerde documenten worden lokaal opgeslagen op:
`~/.claude/plugins/config/ictrecht-privacy-basis/outputs/`
