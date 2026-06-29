<p align="center">
  <img <img width="200" height="200" alt="ictrecht_logo" src="https://github.com/user-attachments/assets/9343f1c8-3cd4-4b67-8a9c-d42cc361c33e" />
 
</p>

<h1 align="center">ICTRecht Plugin Suite voor Claude</h1>

<p align="center">
  Juridische AI-plugins van ICTRecht, klaar voor gebruik in Claude Code en Claude Desktop
</p>

<p align="center">
  <img src="https://img.shields.io/badge/versie-1.0.0-1a56db?style=flat-square" alt="Versie 1.0.0">
  <img src="https://img.shields.io/badge/taal-Nederlands-orange?style=flat-square" alt="Nederlands">
  <img src="https://img.shields.io/badge/Claude_Code-compatibel-blueviolet?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/licentie-Proprietary-lightgrey?style=flat-square" alt="Proprietary">
</p>

---

## Wat zijn de ICTRecht plugins?

De ICTRecht Plugin voegt juridische expertise toe aan Claude. Stel vragen over specifieke situaties, laat documenten beoordelen of voer gestructureerde analyses uit met de werkwijze en het kennisniveau van ICTRecht-juristen. De plugins zijn gratis beschikbaar. Wil je ook gebruik maken van de kennis via onze connector? Neem dan contact op om aan te sluiten op onze kennis-MCP.

Elke plugin biedt slash-commando's voor concrete juridische taken: van DPIA's en contractreviews tot AI Act-classificaties en IE-analyses. Een optioneel inrichtingsgesprek (`cold-start-interview`) stemt de analyses af op jouw organisatie.

<p align="center">
  <img src="./assets/demo.gif" alt="ICTRecht Plugin in gebruik" width="720">
</p>

---

## Gratis plugins vs. connector-versie

Alle plugins zijn beschikbaar als **gratis basisversie**. De analyses zijn gebaseerd op de ingebouwde juridische kennis van Claude.

Klanten van ICTRecht kunnen ook de **connector-versie** activeren. Die koppelt Claude direct aan de kennisbanken van ICTRecht: actuele adviezen, standaarddocumenten en juridische bronnen. De connector is onderdeel van de ICTRecht-dienstverlening — neem contact op via [support@ictrecht.nl](mailto:support@ictrecht.nl) voor toegang.

| | Gratis plugin | Met connector |
|---|:---:|:---:|
| Slash-commando's | ✓ | ✓ |
| Analyses gebaseerd op | Kennis van Claude | ICTRecht kennisbanken |
| Organisatieprofiel opslaan | ✓ | ✓ |
| Verwijzing voor definitief advies | ✓ | ✓ |
| Toegang | Vrij te downloaden | Via [support@ictrecht.nl](mailto:support@ictrecht.nl) |

---

## Alle plugins

| Plugin | Vakgebied | Skills | Download |
|---|---|---|---|
| **ictrecht-privacy** * | Privacy & AVG | DPIA · datalek · AVG-rechten · VOK-review · doorgifte · grondslag | [![](https://img.shields.io/badge/⬇_connector-1a56db?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-privacy.zip) |
| **ictrecht-privacy-basis** | Privacy & AVG | DPIA · datalek · AVG-rechten · VOK-review · doorgifte · grondslag | [![](https://img.shields.io/badge/⬇_gratis-6b7280?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-privacy-basis.zip) |
| **ictrecht-contracten** | Contractenrecht | contract-review · NDA · algemene voorwaarden · aansprakelijkheid · SLA · onderhandeling | [![](https://img.shields.io/badge/⬇_gratis-6b7280?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-contracten.zip) |
| **ictrecht-legal-counsel** | Legal Counsel | juridisch-memo · risico-analyse · compliance-check · regelgeving-scan · geschil · adviesstructuur | [![](https://img.shields.io/badge/⬇_gratis-6b7280?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-legal-counsel.zip) |
| **ictrecht-ie** | Intellectueel Eigendom | auteursrecht · merkenrecht · software-licenties · IE-clausules · handelsnaam · AI & IP | [![](https://img.shields.io/badge/⬇_gratis-6b7280?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-ie.zip) |
| **ictrecht-data** | Data (juridisch) | verwerkingsregister · data-sharing · governance · Data Act · open data · dataverdragen | [![](https://img.shields.io/badge/⬇_gratis-6b7280?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-data.zip) |
| **ictrecht-digital-decade** | Digital Decade | AI Act · NIS2 · DSA · DMA · Cyber Resilience Act · regelgeving-scan | [![](https://img.shields.io/badge/⬇_gratis-6b7280?style=flat-square)](https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-digital-decade.zip) |

* Connector-versie beschikbaar via [support@ictrecht.nl](mailto:support@ictrecht.nl)

---

## Installatie

### Claude Desktop (ZIP uploaden)

Download een ZIP via de knoppen in de plugintabel hierboven. Ga vervolgens naar **Settings → Extensions → Upload plugin**. Zie ook de korte visualisering hieronder.

---

<img width="756" height="480" alt="ICTRecht plugin install" src="https://github.com/user-attachments/assets/9f027bd3-e7af-4948-8548-2d57b8c9e8ce" />



### Claude Code (aanbevolen — volledige plugin met slash-commando's)

**Stap 1** — Voeg de marketplace toe (eenmalig):
```
/plugin marketplace add https://github.com/MarkICTRecht/ictrecht-mcp
```

**Stap 2** — Installeer één of meer plugins:
```
/plugin install ictrecht-privacy-basis@ictrecht-plugins
/plugin install ictrecht-contracten@ictrecht-plugins
/plugin install ictrecht-legal-counsel@ictrecht-plugins
/plugin install ictrecht-ie@ictrecht-plugins
/plugin install ictrecht-data@ictrecht-plugins
/plugin install ictrecht-digital-decade@ictrecht-plugins
```

**Stap 3** — Herstart Claude Code.

**Stap 4** — Optioneel: richt in met een organisatieprofiel (~10 minuten):
```
/ictrecht-privacy-basis:cold-start-interview
```
Alle commando's werken ook zonder profiel — analyses zijn dan generiek.

---


## Licentie

© ICTRecht B.V. Alle rechten voorbehouden.

Deze plugins zijn uitsluitend bedoeld voor gebruik door klanten en relaties van ICTRecht B.V. Verspreiding, wijziging of commercieel gebruik zonder schriftelijke toestemming is niet toegestaan. Zie [LICENSE](./LICENSE) voor de volledige licentievoorwaarden.

---

<p align="center">
  <a href="https://ictrecht.nl">ictrecht.nl</a> · <a href="mailto:info@ictrecht.nl">info@ictrecht.nl</a> · <a href="mailto:support@ictrecht.nl">support@ictrecht.nl</a>
</p>
