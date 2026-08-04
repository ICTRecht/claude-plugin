---
name: cyberweerbaarheid-act
description: >
  Analyseer Cyber Resilience Act verplichtingen voor producten met digitale elementen.
argument-hint: "[product of component]"
---

## Metadata
- **name:** cyberweerbaarheid-act
- **description:** Analyseer Cyber Resilience Act verplichtingen voor producten met digitale elementen.
- **argument-hint:** "[product of component]"

## Voorbereiding (3-laags)

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-compliance-officer:cold-start-interview` uit voor gepersonaliseerde analyse. Nu wordt generieke CRA-analyse toegepast.*

Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

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

## Instructies

Voer de volgende stappen uit voor het opgegeven product of de component:

### Stap 1 — Is de Cyber Resilience Act van toepassing?
Een "product met digitale elementen" is: elk softwareproduct of hardwareproduct dat een directe of indirecte logische of fysieke gegevensverbinding met een apparaat of netwerk heeft.

**Uitsluitingen (CRA niet van toepassing):**
- Producten die al vallen onder andere EU-regelgeving met gelijkwaardige cybersecurityvereisten (medische apparatuur MDR, luchtvaart, motorvoertuigen, marine)
- Open source software (gedeeltelijke uitzondering voor commercieel gebruikte OS)
- Software als dienst (SaaS) — tenzij op afstand toegankelijk component van product

**Rol in de toeleveringsketen:**
- Fabrikant (brengt product op markt): volledige verplichtingen
- Importeur: verificatie en doorgifte documentatie
- Distributeur: verificatie CE-markering en documentatie

**Conclusie:** CRA van toepassing? Welke rol heeft de organisatie?

### Stap 2 — Categorie van het product
| Categorie | Omschrijving | Conformiteitsbeoordeling |
|---|---|---|
| **Standaard** | Producten met lager cybersecurityrisico | Self-assessment mogelijk |
| **Belangrijk — klasse I** | Belangrijke producten (Bijlage III, klasse I): identiteitsbeheer, browsers, VPN, wachtwoordbeheer, beveiligingsmonitoring, firewalls voor consumenten, smart home, IoT algemeen gebruik | Self-assessment met geharmoniseerde norm OF derde partij |
| **Belangrijk — klasse II** | Belangrijke producten (Bijlage III, klasse II): besturingssystemen, hypervisors, firewalls/IDS voor industrieel gebruik, manipulatiebestendige microprocessors | Verplichte conformiteitsbeoordeling door derde partij |
| **Kritiek** | Kritieke producten (Bijlage IV): hardwarebeveiligingsmodules, slimme meters, chipkaarten/smartcard-IC's | Europees cybersecuritycertificeringsschema kan verplicht worden gesteld |

### Stap 3 — Essentiële cybersecurityvereisten (Bijlage I CRA)

**Deel I — Producteigenschappen:**

| Vereiste | Status |
|---|---|
| Security by design en by default | |
| Geen bekende uitgebuite kwetsbaarheden bij levering | |
| Beveiligde configuratie (standaard veilige instellingen) | |
| Bescherming tegen ongeautoriseerde toegang (authenticatie, toegangsbeheer) | |
| Vertrouwelijkheid opgeslagen, verzonden en verwerkte data | |
| Integriteit van data, commando's en configuraties | |
| Beperking aanvalsoppervlak (onnodige poorten, diensten uitschakelen) | |
| Beperking impact beveiligingsincidenten | |
| Logging van beveiligingsrelevante gebeurtenissen | |
| Mogelijkheid tot beveiligde updates | |

**Deel II — Kwetsbaarheidsbeheersproces:**

| Vereiste | Status |
|---|---|
| Identificeren en documenteren van kwetsbaarheden (SBOM) | |
| Onverwijld aanpakken en remediëren van kwetsbaarheden | |
| Gecoördineerde kwetsbaarheidsopenbaring (CVD-beleid) | |
| Gratis beveiligingsupdates beschikbaar stellen | |
| Regelmatige beveiligingstests | |
| Openbaar disclosure beleid voor kwetsbaarheden | |

### Stap 4 — Conformiteitsbeoordeling
Op basis van de categorie (Stap 2):
- **Standaard:** EU-verklaring van overeenstemming + technische documentatie
- **Klasse I met norm:** Self-assessment + technische documentatie
- **Klasse I zonder norm:** Beoordeling door aangemeld orgaan (notified body)
- **Klasse II:** Verplichte beoordeling door aangemeld orgaan
- CE-markering aanbrengen na succesvolle beoordeling

### Stap 5 — Support-periode en beveiligingsupdates
- Minimaal **5 jaar** na het in de handel brengen van het product (of verwachte levensduur indien korter)
- Beveiligingsupdates moeten beschikbaar zijn voor de gehele support-periode
- Updates moeten eenvoudig te installeren zijn
- Eindgebruikers moeten geïnformeerd worden over einddatum support

### Stap 6 — Rapportageverplichtingen
Fabrikanten moeten melden bij:
- **ENISA** (Europees Agentschap voor Cybersecurity): anonieme statistische gegevens kwetsbaarheden
- **CSIRT** van lidstaat van vestiging:
  - **24 uur:** Vroege waarschuwing bij actief uitgebuite kwetsbaarheden
  - **72 uur:** Gedetailleerde melding actief uitgebuite kwetsbaarheden
  - **14 dagen na vroege waarschuwing:** Eindrapport kwetsbaarheid
- **Significante beveiligingsincidenten:** binnen 24 uur vroege waarschuwing, 72 uur volledig rapport

### Stap 7 — Actieplan
Overzicht van:
1. Bevestigde toepasselijkheid CRA en productcategorie
2. Ontbrekende technische maatregelen (Bijlage I)
3. Te implementeren processen (SBOM, CVD-beleid, updateproces)
4. Conformiteitsbeoordelingstraject en tijdlijn
5. Prioritering op basis van inwerkingtreding CRA

**Tijdlijn CRA (Verordening (EU) 2024/2847):**
- In werking getreden op 10 december 2024
- **11 september 2026:** meldplicht voor actief uitgebuite kwetsbaarheden en ernstige incidenten van kracht
- **11 december 2027:** volledige toepassing van de hoofdverplichtingen (essentiële eisen, conformiteitsbeoordeling, CE-markering)

### Output
Sla de CRA-analyse op naar `~/.claude/plugins/config/ictrecht-compliance-officer/outputs/cyberweerbaarheid-act-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
