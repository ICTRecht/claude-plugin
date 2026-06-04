# ICTRecht Privacy Plugin voor Claude

Met deze plugin gebruik je de juridische kennisbanken van ICTRecht rechtstreeks vanuit Claude. Je kunt DPIA's uitvoeren, datalekken beoordelen, verwerkersovereenkomsten controleren en meer — volledig in het Nederlands, afgestemd op jouw organisatie.

<p align="center">
  <a href="https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-privacy.zip">
    <img src="https://img.shields.io/badge/⬇%20Download%20Plugin-ICTRecht%20Privacy%20v1.0.0-1a1a2e?style=for-the-badge&logoColor=white" alt="Download ICTRecht Privacy Plugin">
  </a>
</p>

---

## Welke versie van Claude gebruik jij?

Er zijn twee versies van Claude. Kies de juiste installatiehandleiding:

| Ik gebruik… | Hoe herken ik dat? | Ga naar |
|---|---|---|
| **Claude Desktop** | Een chat-app op mijn computer | [Optie A](#optie-a--claude-desktop-via-instellingen) |
| **Claude Code** | Een terminal-venster met Claude | [Optie B](#optie-b--claude-code-via-terminal) |

Niet zeker? Als je geen terminal gebruikt, kies dan **Optie A**.

---

## Optie A — Claude Desktop (via instellingen)

Met Claude Desktop voeg je de kennisbanken toe als connector. Je krijgt direct toegang tot alle kennisbanken — geen download of installatie nodig.

### Stap 1 — Open Claude Desktop instellingen

Klik linksonder op je naam of het ⚙️-icoon → **Settings** → **Connectors** (of **Connected Apps**).

### Stap 2 — Voeg de ICTRecht connector toe

Klik op **"Add connector"** of **"+"** en vul in:

- **URL:** `https://ictrecht.fastmcp.app/mcp`
- **Naam:** ICTRecht Privacy

### Stap 3 — Inloggen

Een browservenster opent. Log in met je Horizon-account (of maak er een aan op [horizon.prefect.io](https://horizon.prefect.io)).

### Stap 4 — Klaar

De ICTRecht kennisbanken zijn nu beschikbaar. Stel een privacyvraag in Claude Desktop, bijvoorbeeld:

> *"Wat moet ik melden bij een datalek aan de Autoriteit Persoonsgegevens?"*

> ℹ️ De slash-commando's (`/ictrecht-privacy:dpia` etc.) zijn niet beschikbaar in Claude Desktop. Voor de volledige plugin met commando's: gebruik Claude Code (Optie B).

---

## Optie B — Claude Code (via terminal)

Met Claude Code krijg je de volledige plugin inclusief slash-commando's.

### Stap 1 — Download en uitpakken

Klik op de downloadknop bovenaan deze pagina. Pak het ZIP-bestand uit. Je krijgt een map `ictrecht-privacy`.

### Stap 2 — Open Claude Code

Start Claude Code in je terminal.

### Stap 3 — Voeg de plugin toe

Typ in Claude Code:

```
/plugin marketplace add /pad/naar/ictrecht-privacy
```

💡 **Tip voor Mac:** typ `/plugin marketplace add ` (met spatie) en sleep de map `ictrecht-privacy` vanuit Finder naar het terminalvenster. Het pad wordt automatisch ingevuld.

### Stap 4 — Installeer

```
/plugin install ictrecht-privacy
```

Kies bij de vraag voor **"alle projecten"** (user scope).

### Stap 5 — Herstart Claude Code

Sluit Claude Code en open het opnieuw.

### Stap 6 — Eerste inrichting (eenmalig, ~10 minuten)

```
/ictrecht-privacy:cold-start-interview
```

Claude stelt vragen over jouw organisatie. Na afloop zijn alle commando's beschikbaar.

---

## Beschikbare commando's (Claude Code)

| Commando | Wat het doet |
|---|---|
| `/ictrecht-privacy:dpia` | DPIA uitvoeren voor een nieuwe verwerking |
| `/ictrecht-privacy:datalek` | Datalek beoordelen en meldplicht bepalen |
| `/ictrecht-privacy:avg-rechten` | Verzoek van een betrokkene behandelen |
| `/ictrecht-privacy:vok-review` | Verwerkersovereenkomst controleren |
| `/ictrecht-privacy:doorgifte` | Internationale doorgifte beoordelen |
| `/ictrecht-privacy:grondslag` | Verwerkingsgrondslag bepalen |

### Voorbeelden

```
/ictrecht-privacy:dpia Nieuw klantportaal met logingegevens en gebruikshistorie
```
```
/ictrecht-privacy:datalek Laptop gestolen met klantgegevens, geen encryptie
```
```
/ictrecht-privacy:vok-review [sleep je VOK-document naar het venster]
```

---

## Problemen?

| Probleem | Oplossing |
|---|---|
| "/plugin isn't available" | Je gebruikt Claude Desktop — volg Optie A |
| "Command not found" na installatie | Herstart Claude Code (stap 5 overgeslagen) |
| "Run setup first" | Voer `/ictrecht-privacy:cold-start-interview` uit |
| Je wilt de inrichting opnieuw doen | Voer cold-start-interview opnieuw uit |

---

## Over ICTRecht

ICTRecht B.V. is een gespecialiseerd juridisch adviesbureau op het gebied van IT-recht, privacy en gegevensbescherming.

🌐 [ictrecht.nl](https://ictrecht.nl) · ✉️ info@ictrecht.nl

---

> *De outputs van deze plugin zijn analyses op basis van ICTRecht-kennisbanken en vormen geen definitief juridisch advies. Raadpleeg een ICTRecht-jurist voor uw specifieke situatie.*
