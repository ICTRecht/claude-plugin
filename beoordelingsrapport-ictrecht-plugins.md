# Beoordelingsrapport ICTRecht-plugins

**Datum:** 2 juli 2026 · **Scope:** 6 plugins, 42 skills, 6 CLAUDE.md-templates · **Referentie:** [ICTRecht/Legal-GenAI-Resources](https://github.com/ICTRecht/Legal-GenAI-Resources) · **Versie na review:** 1.1.0

## Algemeen oordeel

De plugins zijn goed opgezet: consistente structuur (3-laags configuratie, cold-start-interview, disclaimer, outputpad), degelijke stappenplannen en overwegend correcte juridische kaders. De vergelijking met de Legal-GenAI-Resources repository liet twee structurele verschillen zien die zijn overgenomen, en de inhoudelijke toets bracht een aantal juridische onjuistheden en verouderde punten aan het licht die zijn gecorrigeerd. Alle wijzigingen zijn doorgevoerd in de bijgeleverde zips (versie 1.1.0).

## 1. Overgenomen uit de GitHub-repository

De repo-prompts (dpa_checker, nda_checker, dpia_assistant) hanteren een vaste kwalificatiesystematiek en expliciete zorgvuldigheidsinstructies die in de plugins ontbraken.

**ICTRecht-driedeling.** De reviewskills gebruikten uiteenlopende schalen (🔴 Hoog / 🟡 Middel / 🟢 Laag). Deze zijn vervangen door de repo-standaard 🔴 Kritiek punt (strijd met dwingend recht of ontbrekend kernonderdeel) / 🟠 Risico (vaag, onvolledig, onredelijk verschoven) / ⚡ Aandachtspunt (afwijking van best practice), inclusief samenvattende tabel en de regel "toon alleen onderdelen met een bevinding". Doorgevoerd in: vok-review, nda-review, contract-review en algemene-voorwaarden.

**Juridische zorgvuldigheid en pseudonimisering.** Aan alle zes CLAUDE.md-templates is een blok toegevoegd: geen verzonnen vindplaatsen of ECLI-nummers, onzekerheid expliciet markeren, verificatie via officiële bronnen, peildatum bij snel veranderende regelgeving. De vertrouwelijkheidsparagraaf verwijst nu naar pseudonimiseren vóór het delen van documenten (conform de repo-prompt 'pseudonimiseren').

## 2. Juridische correcties per plugin

### ictrecht-privacy-basis
- **avg-rechten:** de termijn voor bezwaar (art. 21) stond op "zo snel mogelijk" en verlenging alleen bij inzage. Gecorrigeerd naar de systematiek van art. 12 lid 3 AVG (één maand voor alle rechten, verlengbaar met twee maanden) plus kosteloosheid en art. 12 lid 5.
- **datalek:** de meldingsdrempel "niet verwaarloosbaar risico" is vervangen door de wettelijke formulering van art. 33 lid 1 (melden tenzij risico onwaarschijnlijk); "72 uur na ontdekking" gepreciseerd naar "na kennisname"; voorlopige melding via het AP-meldloket (aanvullen/intrekken) toegevoegd.
- **grondslag:** de art. 9-lijst bevatte fouten — strafrechtelijke gegevens vallen onder art. 10 AVG (en art. 31-33 UAVG), niet art. 9; genetische gegevens ontbraken. Toestemming stond neergezet als restgrondslag ("als geen andere past") — juist andersom. "Niet voor arbeidsrelaties" en "niet voor kinderen" genuanceerd conform AVG/EDPB-lijn; de driestappentoets bij gerechtvaardigd belang benoemd.
- **doorgifte:** EU-U.S. Data Privacy Framework toegevoegd (adequaatheid alleen bij actieve certificering); TIA gecorrigeerd van "is een TIA vereist?" naar "bij SCC's altijd vereist sinds Schrems II" met verwijzing naar EDPB Aanbevelingen 01/2020.
- **vok-review:** het verplichte element uit de aanhef van art. 28 lid 3 (onderwerp, duur, aard, doel, soort gegevens, categorieën betrokkenen) ontbrak in de checklist — toegevoegd. Plus driedeling en input-check.
- **cold-start-interview:** taalfout ("is u actief") hersteld.

### ictrecht-contracten
- **aansprakelijkheid:** de stelling dat een exoneratie voor opzet/grove schuld "nietig" is, is onjuist — gecorrigeerd naar de juiste dogmatiek: beroep op het beding is naar maatstaven van redelijkheid en billijkheid onaanvaardbaar (art. 6:248 lid 2 BW), beperkt tot opzet/bewuste roekeloosheid van de schuldenaar zelf of de bedrijfsleiding.
- **algemene-voorwaarden:** vage verwijzing "Wet OHP, Richtlijn Digitale Inhoud" vervangen door de juiste Nederlandse vindplaatsen (art. 6:230m BW, art. 6:193a e.v. BW, titel 1AA Boek 7 BW); terhandstelling voorzien van art. 6:233/234/230c BW; reflexwerking voor kleine ondernemers toegevoegd.
- **nda-review:** verwijzing naar de Wet bescherming bedrijfsgeheimen toegevoegd (redelijke geheimhoudingsmaatregelen als voorwaarde voor Wbb-bescherming).

### ictrecht-digital-decade
- **ai-act-classificatie:** "sociale scoring door overheden" verruimd (geldt ook voor private partijen); twee ontbrekende verboden toegevoegd (ongerichte scraping gezichtsafbeeldingen, risicobeoordeling strafbare feiten); de art. 6 lid 3-uitzondering op Bijlage III toegevoegd; volledige tijdlijn opgenomen (2-2-2025 / 2-8-2025 / **2-8-2026 hoog-risico — nu direct relevant** / 2-8-2027) plus Nederlands toezicht (AP/RDI).
- **nis2-check:** Nederlandse implementatie via de Cyberbeveiligingswet (opvolger Wbni) toegevoegd, met RDI/NCSC-rolverdeling en de instructie de actuele inwerkingtredingsstatus te controleren.
- **cyberweerbaarheid-act:** vage tijdlijn vervangen door exacte data (Verordening 2024/2847; meldplicht per 11-9-2026 — over tien weken; hoofdverplichtingen per 11-12-2027); categorie-indeling gecorrigeerd naar Bijlage III (belangrijk, klasse I/II) en Bijlage IV (kritiek).
- **dsa-verplichtingen:** onjuiste rij "bewaarplicht 6 maanden (art. 17)" verwijderd (staat niet in de DSA); art. 12 (contactpunt afnemers) toegevoegd; de micro/klein-uitzondering van art. 19/29 toegevoegd; ACM als digitaledienstencoördinator en AP-rol benoemd.
- **dma-analyse:** Booking (aangewezen 2024, Nederlandse poortwachter) toegevoegd; typo "meest-begunstigd-nation" hersteld.
- **regulering-scan:** Data Governance Act en EHDS toegevoegd aan de scantabel.

### ictrecht-data
- **data-act:** toepassingsdatum 12 september 2025 toegevoegd (de verordening geldt al); cloud switching gecorrigeerd — "maximale uitfaseerperiode 12 maanden" was onjuist; nu: opzegtermijn max. 2 maanden, transitieperiode 30 dagen (verlengbaar), switching-kosten volledig verboden per 12 januari 2027; hoofdstuk V (B2G-datatoegang) toegevoegd.
- **open-data:** Who-vermelding geactualiseerd (herzien 2024) en Data Governance Act toegevoegd.
- **dataverdrag-analyse:** verouderde stelling "adequaatheidsbesluit ontbreekt voor VS (na Schrems II)" gecorrigeerd naar de situatie sinds het Data Privacy Framework (2023).
- **verwerkingsregister:** nuance bij de art. 30 lid 5-uitzondering (<250 medewerkers) toegevoegd.

### ictrecht-ie
- **auteursrecht:** art. 8 Aw stond onjuist omschreven als "fictief makerschap opdrachtgever" — gecorrigeerd (openbaarmaking door rechtspersoon zonder naamsvermelding), art. 6 Aw toegevoegd en expliciet gemaakt dat een opdrachtgever niet automatisch rechthebbende wordt; parodie-exceptie (art. 18b Aw) toegevoegd.
- **ie-clausules:** art. 2 Aw gepreciseerd: akte-vereiste voor levering en de restrictieve uitleg van art. 2 lid 3 Aw.
- **merkenrecht / handelsnaam-domeinnaam:** artikelverwijzingen bijgewerkt naar de BVIE-nummering sinds 2019 (art. 2.20 lid 2).
- **ai-ip:** AI Act art. 53 toegevoegd (auteursrechtbeleid GPAI-aanbieders, TDM-opt-outs, samenvatting trainingsdata).

### ictrecht-legal-counsel
- **compliance-check:** niet-bestaande "Wet elektronische communicatie" verwijderd; Wbni vervangen door Cyberbeveiligingswet; Data Act, CRA, DORA en de nieuwe Productaansprakelijkheidsrichtlijn (2024/2853, incl. software/AI) toegevoegd.
- **regelgeving-scan:** niet-bestaande "Wet bescherming persoonsgegevens in het onderwijs" vervangen door bestaande sectorkaders; EAA geactualiseerd (van toepassing sinds 28-6-2025); CRA en Data Act toegevoegd.

## 3. Niet gewijzigd, wel het vermelden waard

- De 3-laags configuratie-aanpak (bestand → geheugen → projectinstructies) is consistent en goed doordacht; ongemoeid gelaten.
- De skills steunen bewust op modelkennis zonder kennisbankconnector ("basis"-versies). De toegevoegde zorgvuldigheidsinstructies mitigeren het hallucinatierisico, maar voor de betaalde variant blijft een MCP-kennisbankconnector de structurele oplossing.
- Overweeg voor een volgende versie: de playbook-benadering uit de repo (JSON-beoordelingskader per contracttype) als optionele bijlage per reviewskill, zodat organisaties eigen playbooks kunnen inpluggen — de repo-README beschrijft dit patroon expliciet.
- De disclaimers en ICTRecht-verwijzingen zijn consistent; versies zijn opgehoogd naar 1.1.0.

---
*Peildatum juridische inhoud: 2 juli 2026. Controleer de inwerkingtredingsstatus van de Cyberbeveiligingswet en de actuele AI Act-toezichtsaanwijzing vóór publicatie.*
