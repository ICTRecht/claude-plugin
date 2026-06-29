<p align="center">
  <img src="https://ictrecht.nl/wp-content/uploads/2023/01/ictrecht-logo.png" alt="ICTRecht" height="50">
</p>

<h1 align="center">ICTRecht Privacy Plugin voor Claude</h1>

<p align="center">
  <img src="https://img.shields.io/badge/versie-1.0.0-1a56db?style=flat-square" alt="v1.0.0">
  <img src="https://img.shields.io/badge/taal-Nederlands-orange?style=flat-square" alt="NL">
  <img src="https://img.shields.io/badge/Claude_Code-compatibel-blueviolet?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/licentie-Proprietary-lightgrey?style=flat-square" alt="Proprietary">
</p>

<p align="center">
  DPIA · Datalekken · AVG-rechten · VOK-review · Doorgifte · Grondslag
</p>

<p align="center">
  <a href="https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-privacy.zip">
    <img src="https://img.shields.io/badge/⬇%20Download-ictrecht--privacy%20v1.0.0%20(met%20connector)-1a56db?style=for-the-badge" alt="Download met connector">
  </a>
  &nbsp;
  <a href="https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-privacy-basis.zip">
    <img src="https://img.shields.io/badge/⬇%20Download-ictrecht--privacy--basis%20v1.0.0%20(gratis)-6b7280?style=for-the-badge" alt="Download gratis">
  </a>
</p>

---

## Twee versies

| | **ictrecht-privacy** | **ictrecht-privacy-basis** |
|---|---|---|
| Skills | Alle 6 | Alle 6 |
| Kennisbankconnector | Ja — ICTRecht + Legal Sources | Nee |
| Analyses gebaseerd op | ICTRecht kennisbanken (actueel) | AVG-kennis Claude (generiek) |
| Upsell naar ICTRecht | Nee | Ja |
| Prijs | Betaald | Gratis |

> Onderdeel van de [ICTRecht Plugin Suite](../README.md) — ook beschikbaar: Contracten, Legal Counsel, IE, Data en Digital Decade.

---

## Welke versie van Claude gebruik jij?

| Ik gebruik… | Hoe herken ik dat? | Ga naar |
|---|---|---|
| **Claude Desktop** | Een chat-app op mijn computer | [Optie A](#optie-a--claude-desktop) |
| **Claude Code** | Een terminal-venster met Claude | [Optie B](#optie-b--claude-code) |

Niet zeker? Kies **Optie A**.

---

## Optie A — Claude Desktop

### Via connector (geen download nodig)

Ga naar **Settings → Connectors → Add connector** en vul in:

- **URL:** `https://ictrecht.fastmcp.app/mcp`
- **Naam:** ICTRecht Privacy

Een browservenster opent voor authenticatie. Na inloggen zijn de kennisbanken beschikbaar.

> ℹ️ Slash-commando's zijn niet beschikbaar in Claude Desktop. Voor de volledige plugin: gebruik Claude Code.

### Via ZIP uploaden

Download een ZIP hierboven en ga naar **Settings → Extensions → Upload plugin**.

---

## Optie B — Claude Code

### Stap 1 — Marketplace toevoegen (eenmalig)

```
/plugin marketplace add https://github.com/MarkICTRecht/ictrecht-mcp
```

### Stap 2 — Plugin installeren

Met connector (betaald):
```
/plugin install ictrecht-privacy@ictrecht-plugins
```

Gratis versie:
```
/plugin install ictrecht-privacy-basis@ictrecht-plugins
```

Kies bij de vraag voor **"alle projecten"** (user scope).

### Stap 3 — Herstart Claude Code

### Stap 4 — Inrichten (optioneel, ~10 minuten)

```
/ictrecht-privacy:cold-start-interview
```

Claude stelt vragen over jouw organisatie. Analyses worden daarna gepersonaliseerd. Overslaan is ook mogelijk — alle commando's werken zonder profiel.

---

## Beschikbare commando's

| Commando | Wat het doet |
|---|---|
| `/ictrecht-privacy:dpia` | DPIA uitvoeren (AVG art. 35) |
| `/ictrecht-privacy:datalek` | Datalek beoordelen en meldplicht bepalen |
| `/ictrecht-privacy:avg-rechten` | Verzoek van een betrokkene behandelen |
| `/ictrecht-privacy:vok-review` | Verwerkersovereenkomst controleren (art. 28) |
| `/ictrecht-privacy:doorgifte` | Internationale doorgifte beoordelen |
| `/ictrecht-privacy:grondslag` | Verwerkingsgrondslag bepalen (art. 6) |

### Voorbeelden

```
/ictrecht-privacy:dpia Nieuw klantportaal met logingegevens en gebruikshistorie
```
```
/ictrecht-privacy:datalek Laptop gestolen met klantgegevens, geen encryptie
```
```
/ictrecht-privacy:vok-review [sleep verwerkersovereenkomst naar het venster]
```

---

## Probleemoplossing

| Probleem | Oplossing |
|---|---|
| `/plugin` werkt niet | Je gebruikt Claude Desktop — volg Optie A |
| "Command not found" na installatie | Herstart Claude Code |
| Analyses zijn generiek | Voer `/ictrecht-privacy:cold-start-interview` uit |
| Inrichting opnieuw doen | Voer cold-start-interview opnieuw uit |

---

## Licentie

© ICTRecht B.V. Alle rechten voorbehouden. Zie [LICENSE](../LICENSE) voor voorwaarden.

---

<p align="center">
  <a href="https://ictrecht.nl">ictrecht.nl</a> · <a href="mailto:support@ictrecht.nl">support@ictrecht.nl</a>
</p>

> *De outputs van deze plugin zijn analyses op basis van ICTRecht-kennisbanken en vormen geen definitief juridisch advies. Raadpleeg een ICTRecht-jurist voor uw specifieke situatie.*
