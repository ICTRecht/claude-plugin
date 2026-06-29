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

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht-digital-decade/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht Digital Decade organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Digital Decade Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-digital-decade:cold-start-interview` uit voor gepersonaliseerde analyse. Nu wordt generieke CRA-analyse toegepast.*

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
| **Klasse I** | Hogere risicoklasse (Bijlage III, deel 1): identiteitsbeheer, browsers, VPN, wachtwoordbeheer, beveiligingsmonitoring, firewalls, mobiele netwerkapparatuur, IoT algemeen gebruik | Self-assessment met geharmoniseerde norm OF derde partij |
| **Klasse II** | Kritische producten (Bijlage III, deel 2): besturingssystemen, hypervisors, firewalls industrieel gebruik, routers, microprocessors, industriële controlesystemen | Verplichte derde partij conformiteitsbeoordeling |
| **Kritieke kerncomponenten** | Hardwarebeveiligingsmodules, chipkaarten, smartcard-IC | Europees cybersecuritycertificeringsschema vereist |

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

**Tijdlijn CRA:** Aangenomen september 2024; meeste verplichtingen van kracht na 36 maanden (circa eind 2027). Rapportageverplichtingen eerder van kracht (21 maanden na inwerkingtreding).

### Output
Sla de CRA-analyse op naar `~/.claude/plugins/config/ictrecht-digital-decade/outputs/cyberweerbaarheid-act-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
