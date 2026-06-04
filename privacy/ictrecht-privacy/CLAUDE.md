<!--
CONFIGURATIE LOCATIE

Gebruikersspecifieke configuratie staat op een versie-onafhankelijk pad:
  ~/.claude/plugins/config/ictrecht-privacy/CLAUDE.md

Regels voor elke skill en commando in deze plugin:
1. LEES configuratie altijd van dat pad. Niet van dit bestand.
2. Als dat bestand niet bestaat of nog [PLACEHOLDER] bevat: STOP. Zeg:
   "Deze plugin moet eerst worden ingericht. Voer /ictrecht-privacy:cold-start-interview uit —
   dit duurt 10-15 minuten en alle commando's zijn ervan afhankelijk."
3. cold-start-interview SCHRIJFT naar dat pad.
4. Dit bestand is het TEMPLATE. Het wordt bij elke update overschreven.
-->

# ICTRecht Privacy Profiel
*Ingevuld door cold-start-interview. Zolang je [PLACEHOLDER] ziet: voer `/ictrecht-privacy:cold-start-interview` uit.*

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
Sluit elke output af met:
> *"Dit is een eerste analyse op basis van ICTRecht-kennisbanken. Voor definitief juridisch advies raadpleeg een ICTRecht-jurist via [ictrecht.nl](https://ictrecht.nl)."*

### Vertrouwelijkheid
Wijs de gebruiker altijd op vertrouwelijkheid voordat output gedeeld wordt buiten de organisatie.

### Ernstvloer
Als een eerdere `/datalek` of `/dpia` analyse een hoog risico heeft vastgesteld, kan een latere analyse voor hetzelfde onderwerp dit niet stilzwijgend verlagen zonder expliciete motivering.

---

## Kennisbanken

De volgende ICTRecht kennisbanken zijn beschikbaar via MCP:

| Tool | Inhoud |
|---|---|
| `search_privacy_guide` | AVG, verwerkersovereenkomsten, privacybeleid |
| `search_avg_rechten` | Rechten van betrokkenen (inzage, correctie, verwijdering) |
| `search_datalekken` | Beoordeling en melding datalekken |
| `search_data_act` | EU Data Act |
| `search_wpg` | Wet politiegegevens |
| `search_gegevensverwerking` | Grondslagen, verwerkingsregister, bewaartermijnen |
| `search_dpia` | DPIA-methodiek en risicoanalyse |
| `search_doorgifte` | Internationale doorgifte buiten EER |

---

## Outputs

Gegenereerde documenten worden lokaal opgeslagen op:
`~/.claude/plugins/config/ictrecht-privacy/outputs/`
