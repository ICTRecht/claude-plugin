---
name: regelgeving-scan
description: >
  Bepaal welke wet- en regelgeving van toepassing is op een organisatie, product of dienst,
  inclusief een specifieke verdieping op EU-digitale regelgeving (AI Act, NIS2, DSA, DMA,
  eIDAS 2.0, Cyber Resilience Act).
argument-hint: "[organisatie, product of dienst]"
---

## Voorbereiding — configuratie laden (3-laags fallback)

Laad het organisatieprofiel in deze volgorde:

1. **Bestand** — lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
2. **Memory** — zoek naar memory-entry `ICTRecht organisatieprofiel`
3. **Project instructions** — zoek naar blok `## ICTRecht Profiel` in de actieve project instructions

Als **geen van de drie** beschikbaar is:
- Ga door met generieke standaardinstellingen (Nederlands recht, algemene IT-rechtpraktijk)
- Toon bovenaan de output:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-compliance-officer:cold-start-interview` uit voor gepersonaliseerde output.*

Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

---

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `PLACEHOLDER_COLLECTION_ID`
   <!-- Nog geen kennisbank-backend beschikbaar voor dit domein --> om je analyse te gronden
   in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

---

## Werkwijze

### Stap 1 — Activiteit beschrijven
Beschrijf de activiteit, het product of de dienst zo concreet mogelijk:
- Wat doet de organisatie / het product / de dienst, en in welke markt of industrie (sector) opereert de organisatie?
- Wie zijn de afnemers of gebruikers (B2C / B2B / overheid) en welke gebruikersgroepen?
- Wat is de schaal (hoeveel gebruikers/klanten, welke EU-landen)?
- Welke technologie wordt gebruikt (AI, connected devices, online platform, kritieke infrastructuur)?
- Welke data wordt verwerkt (persoonsgegevens, financiële data, gezondheidsdata, etc.)?
- Waar vindt de activiteit plaats (NL / EU / wereldwijd)?

### Stap 2 — Sectorspecifieke regelgeving
Identificeer regelgeving die specifiek geldt voor de sector of activiteit:
- **Zorg** — WMG, Wgbo, Wet kwaliteit klachten en geschillen zorg (Wkkgz), MDR
- **Financiën** — Wft, PSD2, DORA, MiFID II, AML-richtlijnen
- **Overheid** — Aanbestedingswet, Archiefwet, Wet open overheid (Woo), BIO
- **Energie** — Energiewet, RED III
- **Transport / Mobiliteit** — sector-specifieke EU-verordeningen
- **Onderwijs** — onderwijswetgeving en sectorafspraken (o.a. Wet register onderwijsdeelnemers, Convenant Digitale Onderwijsmiddelen en Privacy)
- **Telecom / Media** — Wet elektronische communicatie, AVMS-richtlijn

### Stap 3 — Horizontale regelgeving
Identificeer breed-toepasbare regelgeving die ongeacht sector geldt:
- AVG / GDPR — persoonsgegevensverwerking
- AI Act — AI-systemen (classificatie: verboden / hoog risico / beperkt risico / minimaal risico)
- Digital Services Act (DSA) — onlinediensten en platforms
- Digital Markets Act (DMA) — poortwachters
- NIS2 — netwerk- en informatiebeveiliging (in NL: Cyberbeveiligingswet, opvolger Wbni)
- Cyber Resilience Act — producten met digitale elementen
- Data Act — connected products en cloud switching (van toepassing sinds 12 september 2025)
- Cybersecurity Act — certificering
- ePrivacy — cookies, elektronische communicatie
- Productaansprakelijkheidsrichtlijn (EU) 2024/2853 — omvat ook software en AI
- European Accessibility Act (EAA) — van toepassing sinds 28 juni 2025 op o.a. e-commerce, bankdiensten en e-books

### Stap 4 — Digitale regelgeving (verdieping EU-digitale verordeningen)

Dit is een specifiek aandachtsgebied binnen de scan: een diepere doorlichting van de
EU-brede digitale verordeningen die (mede) via Stap 3 al zijn gesignaleerd, aangevuld met
enkele verordeningen die niet in Stap 3 zijn opgenomen (eIDAS 2.0, Data Governance Act,
EHDS, DORA).

**Stap 4.1 — Scan alle relevante EU digitale verordeningen**

Vul de onderstaande tabel in op basis van de beschreven activiteit:

| Regelgeving | Van toepassing? | Kernreden | Urgentie |
|---|---|---|---|
| **AI Act** | | | |
| **NIS2** | | | |
| **DSA** | | | |
| **DMA** | | | |
| **Cyber Resilience Act** | | | |
| **eIDAS 2.0** | | | |
| **Data Act** | | | |
| **Data Governance Act** | | | |
| **EHDS** (zorg) | | | |
| **AVG / GDPR** | | | |
| **DORA** (financieel) | | | |

**Toelichting per regelgeving:**

- **AI Act:** Van toepassing bij ontwikkeling, in de handel brengen of gebruik van AI-systemen in de EU
- **NIS2:** Van toepassing bij opereren in kritieke sectoren (zie Bijlage I/II) boven omvangsdrempels
- **DSA:** Van toepassing bij aanbieden van intermediaire diensten aan EU-gebruikers
- **DMA:** Van toepassing bij aanwijzing als poortwachter (kernplatformdiensten, grote schaal)
- **Cyber Resilience Act:** Van toepassing bij fabricage of verkoop van producten met digitale elementen
- **eIDAS 2.0:** Van toepassing bij aanbieden van vertrouwensdiensten of digitale identiteitsoplossingen
- **Data Act:** Van toepassing bij aanbieden van connected products of gerelateerde diensten (IoT-data); van toepassing sinds 12 september 2025
- **Data Governance Act:** Van toepassing bij data-intermediairs, data-altruïsme en hergebruik van beschermde overheidsdata
- **EHDS:** Van toepassing bij verwerking van elektronische gezondheidsgegevens (primair en secundair gebruik)
- **AVG:** Van toepassing bij verwerking van persoonsgegevens van EU-burgers
- **DORA:** Van toepassing bij financiële entiteiten (banken, verzekeraars, beleggingsondernemingen, fintechs)

**Stap 4.2 — Prioritering**
Rangschik de toepasselijke regelgeving op basis van:
1. **Urgentie:** Welke heeft de meest nabije inwerkingtredingsdatum of handhavingsdeadline?
2. **Sanctierisico:** Welke heeft de hoogste boetes bij niet-naleving?
3. **Implementatie-inspanning:** Welke vereist de meeste tijd en middelen?

**Stap 4.3 — Overlap en synergie**
Identificeer waar verplichtingen overlappen of versterken:
- AVG + AI Act: privacy by design en data governance overlappen
- NIS2 + CRA: cybersecuritymaatregelen en kwetsbaarheidsbeheer zijn complementair
- DSA + DMA: beide gelden voor grote online platforms (VLOP)
- DORA + NIS2: financiële sector kan aan beide onderworpen zijn (lex specialis)
- eIDAS 2.0 + AVG: identiteitsverificatie en dataminimalisatie

Kansen voor gecombineerde implementatie: welke maatregelen dienen meerdere regelgevingen tegelijk?

**Stap 4.4 — Aanbevolen volgorde van aanpak**
Geef een concrete implementatievolgorde:

1. **Direct aandacht:** [regelgeving met meest urgente deadlines]
2. **Korte termijn (0-6 maanden):** [acties]
3. **Middellange termijn (6-18 maanden):** [acties]
4. **Langere termijn (18+ maanden):** [acties]

Aanbeveling voor verdere verdieping:
- Gebruik `/ictrecht-compliance-officer:ai-act-classificatie` voor AI-systemen
- Gebruik `/ictrecht-compliance-officer:nis2-check` voor NIS2-scope en maatregelen
- Gebruik `/ictrecht-compliance-officer:dsa-verplichtingen` voor platform-verplichtingen
- Gebruik `/ictrecht-compliance-officer:dma-analyse` voor poortwachter-analyse
- Gebruik `/ictrecht-compliance-officer:cyberweerbaarheid-act` voor CRA-analyse

### Stap 5 — Contractuele verplichtingen upstream
Zijn er contractuele verplichtingen die extra regelgeving van toepassing maken?
- Verwerkersovereenkomsten (AVG art. 28)
- Overheidsopdrachten (aanbestedingsrechtelijke verplichtingen)
- Brancheafspraken of certificeringsvereisten (ISO 27001, NEN 7510, etc.)

### Stap 6 — Overzichtstabel
Presenteer het resultaat als overzichtstabel:

| Wet / Regelgeving | Van toepassing? | Kernverplichtingen | Prioriteit |
|---|---|---|---|
| AVG / GDPR | ✅ Ja | Verwerkingsgrondslag, privacyverklaring, verwerkersovereenkomst | Hoog |
| AI Act | ⚠️ Mogelijk | Classificatie AI-systeem bepalen | Middel |
| NIS2 | ❓ Controleren | Aanbieders essentiële diensten? | Middel |
| [Wet X] | ✅ / ⚠️ / ❌ | [Kernverplichtingen] | Hoog / Middel / Laag |

---

## Output

Volledig regelgevingsoverzicht met activiteitsbeschrijving, sectorspecifieke en horizontale
regelgeving, de verdieping op EU-digitale regelgeving (scan, prioritering, overlap en
aanbevolen volgorde), contractuele verplichtingen en geprioriteerde overzichtstabel.

Sla de output op in `~/.claude/plugins/config/ictrecht-compliance-officer/outputs/regelgeving-[onderwerp]-[datum].md`.

Sluit af met de standaard ICTRecht disclaimer.
