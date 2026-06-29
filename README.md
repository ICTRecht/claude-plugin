<p align="center">
  <img src="https://ictrecht.nl/wp-content/uploads/2023/01/ictrecht-logo.png" alt="ICTRecht" height="60">
</p>

<h1 align="center">ICTRecht Plugin Suite voor Claude</h1>

<p align="center">
  Juridische AI-plugins van ICTRecht — klaar voor gebruik in Claude Code en Claude Desktop
</p>

<p align="center">
  <img src="https://img.shields.io/badge/versie-1.0.0-1a56db?style=flat-square" alt="Versie 1.0.0">
  <img src="https://img.shields.io/badge/taal-Nederlands-orange?style=flat-square" alt="Nederlands">
  <img src="https://img.shields.io/badge/Claude_Code-compatibel-blueviolet?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/licentie-Proprietary-lightgrey?style=flat-square" alt="Proprietary">
</p>

---

## Plugins

Zeven juridische specialist-plugins, elk met eigen slash-commando's en een optioneel organisatieprofiel.

### Snel installeren (Claude Code)

```
/plugin marketplace add https://github.com/MarkICTRecht/ictrecht-mcp
```

Installeer daarna één of meer plugins:

```
/plugin install ictrecht-privacy@ictrecht-plugins
/plugin install ictrecht-contracten@ictrecht-plugins
/plugin install ictrecht-legal-counsel@ictrecht-plugins
/plugin install ictrecht-ie@ictrecht-plugins
/plugin install ictrecht-data@ictrecht-plugins
/plugin install ictrecht-digital-decade@ictrecht-plugins
```

---

## Overzicht

### Privacy & AVG

| Plugin | Inhoud | Download |
|---|---|---|
| **ictrecht-privacy** | DPIA, datalek, AVG-rechten, VOK-review, doorgifte, grondslag — met ICTRecht kennisbankconnector | [![Download](https://img.shields.io/badge/⬇_download-ictrecht--privacy-1a56db?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-privacy.zip) |
| **ictrecht-privacy-basis** | Zelfde skills, zonder connector, gratis | [![Download](https://img.shields.io/badge/⬇_download-privacy--basis-6b7280?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-privacy-basis.zip) |

**Commando's:**
`/ictrecht-privacy:dpia` · `/ictrecht-privacy:datalek` · `/ictrecht-privacy:avg-rechten` · `/ictrecht-privacy:vok-review` · `/ictrecht-privacy:doorgifte` · `/ictrecht-privacy:grondslag`

---

### Contractenrecht

| Plugin | Inhoud | Download |
|---|---|---|
| **ictrecht-contracten** | Contract review, NDA, algemene voorwaarden, aansprakelijkheid, SLA, onderhandelingsstrategie | [![Download](https://img.shields.io/badge/⬇_download-ictrecht--contracten-1a56db?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-contracten.zip) |

**Commando's:**
`/ictrecht-contracten:contract-review` · `/ictrecht-contracten:nda-review` · `/ictrecht-contracten:algemene-voorwaarden` · `/ictrecht-contracten:aansprakelijkheid` · `/ictrecht-contracten:onderhandeling-prep` · `/ictrecht-contracten:sla-review`

---

### Legal Counsel

| Plugin | Inhoud | Download |
|---|---|---|
| **ictrecht-legal-counsel** | Juridische memo's, risico-analyse, compliance-check, regelgeving-scan, geschilvoorbereiding, adviesstructuur | [![Download](https://img.shields.io/badge/⬇_download-ictrecht--legal--counsel-1a56db?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-legal-counsel.zip) |

**Commando's:**
`/ictrecht-legal-counsel:juridisch-memo` · `/ictrecht-legal-counsel:risico-analyse` · `/ictrecht-legal-counsel:compliance-check` · `/ictrecht-legal-counsel:regelgeving-scan` · `/ictrecht-legal-counsel:geschil-voorbereiding` · `/ictrecht-legal-counsel:advies-structuur`

---

### Intellectueel Eigendom

| Plugin | Inhoud | Download |
|---|---|---|
| **ictrecht-ie** | Auteursrecht, merkenrecht, software-licenties, IE-clausules, handelsnaam/domeinnaam, AI & IP | [![Download](https://img.shields.io/badge/⬇_download-ictrecht--ie-1a56db?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-ie.zip) |

**Commando's:**
`/ictrecht-ie:auteursrecht` · `/ictrecht-ie:merkenrecht` · `/ictrecht-ie:software-licenties` · `/ictrecht-ie:ie-clausules` · `/ictrecht-ie:handelsnaam-domeinnaam` · `/ictrecht-ie:ai-ip`

---

### Data (Juridisch)

| Plugin | Inhoud | Download |
|---|---|---|
| **ictrecht-data** | Verwerkingsregister, data sharing, data governance, EU Data Act, open data, dataverdragen | [![Download](https://img.shields.io/badge/⬇_download-ictrecht--data-1a56db?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-data.zip) |

**Commando's:**
`/ictrecht-data:verwerkingsregister` · `/ictrecht-data:data-sharing` · `/ictrecht-data:data-governance` · `/ictrecht-data:data-act` · `/ictrecht-data:open-data` · `/ictrecht-data:dataverdrag-analyse`

---

### Digital Decade (AI Act · NIS2 · DSA · DMA)

| Plugin | Inhoud | Download |
|---|---|---|
| **ictrecht-digital-decade** | AI Act classificatie & conformiteit, NIS2, DSA, DMA, Cyber Resilience Act, regelgeving-scan | [![Download](https://img.shields.io/badge/⬇_download-ictrecht--digital--decade-1a56db?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-digital-decade.zip) |

**Commando's:**
`/ictrecht-digital-decade:ai-act-classificatie` · `/ictrecht-digital-decade:nis2-check` · `/ictrecht-digital-decade:dsa-verplichtingen` · `/ictrecht-digital-decade:dma-analyse` · `/ictrecht-digital-decade:cyberweerbaarheid-act` · `/ictrecht-digital-decade:regulering-scan`

---

## Installatie

### Claude Code (aanbevolen — volledige plugin met slash-commando's)

**Stap 1** — Voeg de marketplace toe (eenmalig):
```
/plugin marketplace add https://github.com/MarkICTRecht/ictrecht-mcp
```

**Stap 2** — Installeer de gewenste plugin(s):
```
/plugin install ictrecht-privacy@ictrecht-plugins
```

**Stap 3** — Herstart Claude Code en richt in:
```
/ictrecht-privacy:cold-start-interview
```

Het inrichtingsgesprek duurt 10–15 minuten en is optioneel — alle commando's werken ook zonder.

### Claude Desktop (connector — alleen privacy)

Voeg de ICTRecht connector toe via **Settings → Connectors → Add connector**:

- **URL:** `https://ictrecht.fastmcp.app/mcp`

Slash-commando's zijn niet beschikbaar in Claude Desktop.

### ZIP uploaden (zonder terminal)

Download een ZIP via de knoppen hierboven en upload via **Settings → Extensions → Upload plugin**.

---

## Wat levert een plugin op?

Elke plugin bevat gestructureerde workflows die Claude stap voor stap door een juridische analyse leiden. Zonder connector werkt Claude op eigen AVG- en IT-rechtenkennis. Met de ICTRecht kennisbankconnector (`ictrecht-privacy`) worden analyses aangevuld met actuele ICTRecht-bronnen.

Aan het einde van elke analyse verschijnt een verwijzing naar ICTRecht voor definitief juridisch advies.

---

## Licentie

© ICTRecht B.V. Alle rechten voorbehouden.

Deze plugins zijn uitsluitend bedoeld voor gebruik door klanten en relaties van ICTRecht B.V. Verspreiding, wijziging of commercieel gebruik zonder schriftelijke toestemming is niet toegestaan.

---

<p align="center">
  <a href="https://ictrecht.nl">ictrecht.nl</a> · <a href="mailto:info@ictrecht.nl">info@ictrecht.nl</a> · <a href="mailto:support@ictrecht.nl">support@ictrecht.nl</a>
</p>
