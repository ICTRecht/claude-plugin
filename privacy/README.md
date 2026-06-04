# ICTRecht Privacy Plugin voor Claude

Met deze plugin gebruik je de juridische kennisbanken van ICTRecht rechtstreeks vanuit Claude. Je kunt DPIA's uitvoeren, datalekken beoordelen, verwerkersovereenkomsten controleren en meer — volledig in het Nederlands, afgestemd op jouw organisatie.

<p align="center">
  <a href="https://github.com/MarkICTRecht/ictrecht-mcp/releases/latest/download/ictrecht-privacy.zip">
    <img src="https://img.shields.io/badge/⬇%20Download%20Plugin-ICTRecht%20Privacy%20v1.0.0-1a1a2e?style=for-the-badge&logoColor=white" alt="Download ICTRecht Privacy Plugin">
  </a>
</p>

---

## Wat heb je nodig?

- **Claude Desktop** (gratis te downloaden op [claude.com/download](https://claude.com/download))
- **Een Claude-account** — een gratis account volstaat voor persoonlijk gebruik; voor teams adviseren we Claude for Work

---

## Installatie — stap voor stap

### Stap 1 — Download de plugin

Klik rechtsboven op de groene knop **"Code"** → **"Download ZIP"** op de GitHub-pagina.

Pak het ZIP-bestand uit. Je krijgt een map genaamd `ictrecht-privacy`.

---

### Stap 2 — Open Claude Desktop

Start Claude Desktop op je computer.

---

### Stap 3 — Voeg de plugin toe

Typ het volgende commando in het chatvenster van Claude. Vervang het pad door de locatie waar je de map hebt uitgepakt:

```
/plugin marketplace add /pad/naar/ictrecht-privacy
```

**Voorbeeld op Mac:**
```
/plugin marketplace add /Users/jouwnaam/Downloads/ictrecht-privacy
```

**Voorbeeld op Windows:**
```
/plugin marketplace add C:\Users\jouwnaam\Downloads\ictrecht-privacy
```

> 💡 **Tip voor Mac:** typ `/plugin marketplace add ` (met een spatie achteraan) en sleep daarna de map `ictrecht-privacy` vanuit Finder naar het chatvenster. Het pad wordt automatisch ingevuld.

Druk op **Enter**.

---

### Stap 4 — Installeer de plugin

Typ vervolgens:

```
/plugin install ictrecht-privacy
```

Druk op **Enter** en wacht tot Claude de installatie bevestigt.

> ⚠️ Als gevraagd wordt of je de plugin wilt installeren voor "dit project" of "alle projecten": kies **alle projecten** (user scope). Dit is nodig om bestanden op je computer te kunnen openen.

---

### Stap 5 — Herstart Claude Desktop

**Sluit Claude Desktop volledig af en open het opnieuw.** Dit is verplicht — de plugin is pas actief na een herstart.

---

### Stap 6 — Eerste inrichting (eenmalig, 10-15 minuten)

Bij de eerste keer gebruik stel je de plugin in op jouw organisatie. Typ:

```
/ictrecht-privacy:cold-start-interview
```

Claude stelt je een aantal vragen over je organisatie (naam, sector, FG, etc.). Na afloop zijn alle commando's klaar voor gebruik.

> ✅ Je hoeft dit maar **één keer** te doen. De antwoorden worden opgeslagen en door alle commando's gebruikt.

---

## Beschikbare commando's

Na de eerste inrichting kun je deze commando's gebruiken:

| Commando | Wat het doet |
|---|---|
| `/ictrecht-privacy:dpia` | DPIA uitvoeren voor een nieuwe verwerking of product |
| `/ictrecht-privacy:datalek` | Datalek beoordelen en meldplicht bepalen (AP en/of betrokkenen) |
| `/ictrecht-privacy:avg-rechten` | Verzoek van een betrokkene behandelen (inzage, verwijdering, etc.) |
| `/ictrecht-privacy:vok-review` | Verwerkersovereenkomst controleren op AVG-conformiteit |
| `/ictrecht-privacy:doorgifte` | Internationale doorgifte van persoonsgegevens beoordelen |
| `/ictrecht-privacy:grondslag` | Juiste verwerkingsgrondslag bepalen (art. 6 AVG) |

### Gebruik

Typ een commando, eventueel gevolgd door een omschrijving:

```
/ictrecht-privacy:dpia Nieuw klantportaal met logingegevens en gebruikshistorie
```

```
/ictrecht-privacy:datalek Laptop gestolen met klantgegevens, geen encryptie
```

```
/ictrecht-privacy:vok-review [sleep je VOK-document naar het chatvenster]
```

---

## Problemen?

| Probleem | Oplossing |
|---|---|
| "Command not found" | Herstart Claude Desktop (stap 5 overgeslagen) |
| "Run setup first" | Voer `/ictrecht-privacy:cold-start-interview` uit |
| Plugin doet niets na installatie | Controleer of je hebt gekozen voor "user scope" bij installatie |
| Je wilt de inrichting opnieuw doen | Voer `/ictrecht-privacy:cold-start-interview` opnieuw uit |

---

## Over ICTRecht

ICTRecht B.V. is een gespecialiseerd juridisch adviesbureau op het gebied van IT-recht, privacy en gegevensbescherming.

🌐 [ictrecht.nl](https://ictrecht.nl) · ✉️ info@ictrecht.nl

---

> *De outputs van deze plugin zijn analyses op basis van ICTRecht-kennisbanken en vormen geen definitief juridisch advies. Raadpleeg een ICTRecht-jurist voor uw specifieke situatie.*
