<!--
CONFIGURATIE LOCATIE

Gebruikersspecifieke configuratie staat op:
  ~/.claude/plugins/config/ictrecht-contracten/CLAUDE.md

Regels:
1. LEES configuratie altijd van dat pad.
2. Als dat bestand niet bestaat: ga door met generieke standaardinstellingen.
3. cold-start-interview SCHRIJFT naar dat pad.
4. Dit bestand is het TEMPLATE. Het wordt bij elke update overschreven.
-->

# ICTRecht Contracten Profiel
*Ingevuld door cold-start-interview. Zolang je [PLACEHOLDER] ziet: voer `/ictrecht-contracten:cold-start-interview` uit.*

---

## Over de organisatie

**Naam:** [PLACEHOLDER]
**Sector:** [PLACEHOLDER — zorg / onderwijs / overheid / SaaS / etc.]
**Omvang:** [PLACEHOLDER — aantal medewerkers]
**Rol in contracten:** [PLACEHOLDER — opdrachtgever / opdrachtnemer / beide]
**Vestigingsland(en):** [PLACEHOLDER]
**Toepasselijk recht:** [PLACEHOLDER — Nederlands recht is standaard]

**Juridisch contactpersoon:**
[PLACEHOLDER — interne jurist / extern advocaat / nvt]

**Vaste contractpartijen / leveranciers:**
[PLACEHOLDER — belangrijke contractpartijen waar vaak mee gewerkt wordt]

---

## Wie gebruikt deze plugin

**Rol:** [PLACEHOLDER — jurist / inkoper / contractmanager / management / anders]
**Bevoegdheid tekenen:** [PLACEHOLDER — wie mag namens de organisatie tekenen?]

---

## Werkwijze en huisstijl

**Taal outputs:** Nederlands (tenzij anders gevraagd)
**Niveau:** [PLACEHOLDER — intern gebruik / extern / voor bestuur]
**Vaste structuur documenten:** [PLACEHOLDER — wordt ingevuld na cold-start]
**Gehanteerd recht:** [PLACEHOLDER — standaard Nederlands recht, BW]

---

## Gedeelde aandachtspunten

### Disclaimer
Sluit elke output af met twee blokken, in deze volgorde:

> *"Dit is een analyse op basis van het Burgerlijk Wetboek, algemene juridische kennis en IT-contractenrechtelijke beginselen. Voor definitief juridisch advies raadpleeg een ICTRecht-jurist via [ictrecht.nl](https://ictrecht.nl)."*

> 💡 *Wil je toegang tot de kennis van ICTRecht voor nog betere antwoorden? Neem dan contact op via [support@ictrecht.nl](mailto:support@ictrecht.nl).*

### Vertrouwelijkheid
Wijs de gebruiker altijd op vertrouwelijkheid voordat output gedeeld wordt buiten de organisatie.

---

## Outputs

Gegenereerde documenten worden lokaal opgeslagen op:
`~/.claude/plugins/config/ictrecht-contracten/outputs/`
