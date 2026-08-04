<p align="center">
  <img width="200" height="200" alt="ictrecht_logo" src="https://github.com/user-attachments/assets/9343f1c8-3cd4-4b67-8a9c-d42cc361c33e" />
</p>

<h1 align="center">ICTRecht Plugin Suite voor Claude</h1>

<p align="center">
  Juridische AI-plugins van ICTRecht, ingedeeld per rol, klaar voor gebruik in Claude Code en Claude Desktop
</p>

<p align="center">
  <img src="https://img.shields.io/badge/versie-2.0.0-1a56db?style=flat-square" alt="Versie 2.0.0">
  <img src="https://img.shields.io/badge/taal-Nederlands-orange?style=flat-square" alt="Nederlands">
  <img src="https://img.shields.io/badge/Claude_Code-compatibel-blueviolet?style=flat-square" alt="Claude Code">
  <img src="https://img.shields.io/badge/licentie-CC%20BY--SA%204.0-blue?style=flat-square" alt="CC BY-SA 4.0">
</p>

---

## Wat zijn de ICTRecht plugins?

De ICTRecht Plugin Suite voegt juridische expertise toe aan Claude, ingedeeld naar de rol die je vervult: **Privacy Officer**, **FG**, **Legal Counsel** of **Compliance Officer**. Stel vragen over specifieke situaties, laat documenten beoordelen of voer gestructureerde analyses uit met de werkwijze en het kennisniveau van ICTRecht-juristen.

Elke plugin biedt slash-commando's voor concrete juridische taken: van DPIA's en contractreviews tot AI Act-classificaties en IE-analyses. Een optioneel inrichtingsgesprek (`cold-start-interview`) stemt de analyses af op jouw organisatie — je hoeft dit maar één keer te doen, ook als je meerdere ICTRecht-plugins installeert.

<p align="center">
  <img src="./assets/demo.gif" alt="ICTRecht Plugin in gebruik" width="720">
</p>

---

## Eén plugin per rol, connector optioneel

Alle plugins zijn gratis en werken direct met de ingebouwde juridische kennis van Claude — dat is een volwaardige manier om ze te gebruiken. Wil je analyses laten gronden in actuele ICTRecht-kennisbanken? Voeg dan zelf de **ictrecht-knowledge-server**-connector toe (via Claude Desktop *Settings → Connectors*, of `claude mcp add` in Claude Code). Skills detecteren de connector automatisch als hij er is, en werken er zonder problemen ook zonder — geen foutmeldingen, geen apart "basis"-plugin meer nodig.

Neem voor toegang tot de connector contact op via [support@ictrecht.nl](mailto:support@ictrecht.nl).

---

## Alle plugins

| Plugin | Rol | Skills | Download |
|---|---|---|---|
| **ictrecht-privacy-officer** | Privacy Officer | dpia · datalek · avg-rechten · doorgifte · grondslag · vok-review · verwerkingsregister · data-sharing · data-governance · ai-act-classificatie | [![](https://img.shields.io/badge/⬇_download-1a56db?style=flat-square)](https://github.com/ICTRecht/claude-plugin/releases/latest/download/ictrecht-privacy-officer.zip) |
| **ictrecht-fg**  | FG | dpia · datalek · avg-rechten · doorgifte · grondslag · vok-review · verwerkingsregister · data-sharing · data-governance · ai-act-classificatie | [![](https://img.shields.io/badge/⬇_download-1a56db?style=flat-square)](https://github.com/ICTRecht/claude-plugin/releases/latest/download/ictrecht-fg.zip) |
| **ictrecht-legal-counsel** | Legal Counsel | contract-review · nda-review · algemene-voorwaarden · aansprakelijkheid · onderhandeling-prep · sla-review · juridisch-memo · risico-analyse · geschil-voorbereiding · advies-structuur · vok-review · ie-clausules · auteursrecht · merkenrecht · software-licenties · handelsnaam-domeinnaam · ai-ip | [![](https://img.shields.io/badge/⬇_download-1a56db?style=flat-square)](https://github.com/ICTRecht/claude-plugin/releases/latest/download/ictrecht-legal-counsel.zip) |
| **ictrecht-compliance-officer** | Compliance Officer | verwerkingsregister · data-sharing · data-governance · data-act · open-data · dataverdrag-analyse · risico-analyse · compliance-check · regelgeving-scan · ai-act-classificatie · nis2-check · dsa-verplichtingen · dma-analyse · cyberweerbaarheid-act | [![](https://img.shields.io/badge/⬇_download-1a56db?style=flat-square)](https://github.com/ICTRecht/claude-plugin/releases/latest/download/ictrecht-compliance-officer.zip) |

Sommige skills (bv. `vok-review`, `risico-analyse`, `verwerkingsregister`, `data-sharing`, `data-governance`, `ai-act-classificatie`) zijn relevant voor meerdere rollen en staan daarom in meer dan één plugin.

---

## Installatie

### Claude Desktop (ZIP uploaden)

Download een ZIP via de knoppen in de plugintabel hierboven. Ga vervolgens naar **Settings → Extensions → Upload plugin**. Zie ook de korte visualisering hieronder.

---

<img width="756" height="480" alt="ICTRecht plugin install" src="https://github.com/user-attachments/assets/9f027bd3-e7af-4948-8548-2d57b8c9e8ce" />

### Claude Code (aanbevolen — volledige plugin met slash-commando's)

**Stap 1** — Voeg de marketplace toe (eenmalig):
```
/plugin marketplace add https://github.com/ICTRecht/claude-plugin
```

**Stap 2** — Installeer de plugin(s) die bij jouw rol horen:
```
/plugin install ictrecht-privacy-officer@ictrecht-plugins
/plugin install ictrecht-fg@ictrecht-plugins
/plugin install ictrecht-legal-counsel@ictrecht-plugins
/plugin install ictrecht-compliance-officer@ictrecht-plugins
```

**Stap 3** — Herstart Claude Code.

**Stap 4** — Optioneel: richt in met een organisatieprofiel (~10 minuten):
```
/ictrecht-privacy-officer:cold-start-interview
```
Alle commando's werken ook zonder profiel — analyses zijn dan generiek. Installeer je meerdere ICTRecht-plugins? Dan hoef je dit interview maar één keer te doen — het gedeelde profiel wordt door elke plugin herkend.

---

## Schrijfwijzer

Elke plugin bevat een `SCHRIJFWIJZER.md` met de verplichte ICTRecht-huisstijl: toon, structuur, de ICTRecht-driedeling (kritiek punt / risico / aandachtspunt) en opmaakconventies. Elke skill verwijst hier verplicht naar.

---

## Licentie

De plugins van ICTRecht B.V. worden uitgegeven met een CC BY-SA 4.0 licentie. Wil je een kopie inzien? Kijk hier: https://creativecommons.org/licenses/by-sa/4.0/

---

<p align="center">
  <a href="https://ictrecht.nl">ictrecht.nl</a> · <a href="mailto:info@ictrecht.nl">info@ictrecht.nl</a> · <a href="mailto:support@ictrecht.nl">support@ictrecht.nl</a>
</p>
