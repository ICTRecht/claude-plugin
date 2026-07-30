---
name: regulering-scan
description: >
  Bepaal welke EU digitale regelgeving van toepassing is op een organisatie, product of dienst.
argument-hint: "[organisatie, product of dienst]"
---

## Metadata
- **name:** regulering-scan
- **description:** Bepaal welke EU digitale regelgeving van toepassing is op een organisatie, product of dienst.
- **argument-hint:** "[organisatie, product of dienst]"

## Voorbereiding (3-laags)

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-digital-decade:cold-start-interview` uit voor gepersonaliseerde analyse. Nu wordt generieke reguleringscan uitgevoerd.*

## Instructies

Voer de volgende stappen uit voor de opgegeven organisatie, het product of de dienst:

### Stap 1 — Beschrijf de activiteit of het product
Verzamel of vraag naar:
- **Sector:** In welke markt of industrie opereert de organisatie?
- **Type dienst of product:** Wat wordt aangeboden? (software, hardware, platform, dienst)
- **Doelgroep:** B2C, B2B, overheid? Welke gebruikersgroepen?
- **Schaal:** Hoeveel gebruikers/klanten? Welke EU-landen?
- **Technologie:** AI, connected devices, online platform, kritieke infrastructuur?
- **Data:** Welk soort data wordt verwerkt? (persoonsgegevens, financiële data, gezondheidsdata)

### Stap 2 — Scan alle relevante EU digitale verordeningen

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

### Stap 3 — Prioritering
Rangschik de toepasselijke regelgeving op basis van:
1. **Urgentie:** Welke heeft de meest nabije inwerkingtredingsdatum of handhavingsdeadline?
2. **Sanctierisico:** Welke heeft de hoogste boetes bij niet-naleving?
3. **Implementatie-inspanning:** Welke vereist de meeste tijd en middelen?

### Stap 4 — Overlap en synergie
Identificeer waar verplichtingen overlappen of versterken:
- AVG + AI Act: privacy by design en data governance overlappen
- NIS2 + CRA: cybersecuritymaatregelen en kwetsbaarheidsbeheer zijn complementair
- DSA + DMA: beide gelden voor grote online platforms (VLOP)
- DORA + NIS2: financiële sector kan aan beide onderworpen zijn (lex specialis)
- eIDAS 2.0 + AVG: identiteitsverificatie en dataminimalisatie

Kansen voor gecombineerde implementatie: welke maatregelen dienen meerdere regelgevingen tegelijk?

### Stap 5 — Aanbevolen volgorde van aanpak
Geef een concrete implementatievolgorde:

1. **Direct aandacht:** [regelgeving met meest urgente deadlines]
2. **Korte termijn (0-6 maanden):** [acties]
3. **Middellange termijn (6-18 maanden):** [acties]
4. **Langere termijn (18+ maanden):** [acties]

Aanbeveling voor verdere verdieping:
- Gebruik `/ictrecht-digital-decade:ai-act-classificatie` voor AI-systemen
- Gebruik `/ictrecht-digital-decade:nis2-check` voor NIS2-scope en maatregelen
- Gebruik `/ictrecht-digital-decade:dsa-verplichtingen` voor platform-verplichtingen
- Gebruik `/ictrecht-digital-decade:dma-analyse` voor poortwachter-analyse
- Gebruik `/ictrecht-digital-decade:cyberweerbaarheid-act` voor CRA-analyse

### Output
Sla de reguleringscan op naar `~/.claude/plugins/config/ictrecht-digital-decade/outputs/regulering-scan-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
