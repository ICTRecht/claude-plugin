---
name: nis2-check
description: >
  Bepaal of een organisatie onder NIS2 valt en wat de verplichtingen zijn.
argument-hint: "[organisatie of sector]"
---

## Metadata
- **name:** nis2-check
- **description:** Bepaal of een organisatie onder NIS2 valt en wat de verplichtingen zijn.
- **argument-hint:** "[organisatie of sector]"

## Voorbereiding (3-laags)

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht-digital-decade/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht Digital Decade organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Digital Decade Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-digital-decade:cold-start-interview` uit voor gepersonaliseerde analyse. Nu wordt generieke NIS2 check toegepast.*

## Instructies

Voer de volgende stappen uit voor de opgegeven organisatie of sector:

### Stap 1 — Valt de organisatie onder NIS2?
Controleer sectorindeling (Bijlage I = hoog-kritisch, Bijlage II = overig kritisch):

**Bijlage I — Hoog-kritische sectoren:**
- Energie (elektriciteit, olie, gas, waterstof)
- Transport (lucht, spoor, water, weg)
- Bankwezen
- Financiële marktinfrastructuur
- Gezondheidszorg
- Drinkwater
- Afvalwater
- Digitale infrastructuur (DNS, TLD, cloud, datacenters, CDN, TSP, elektronische communicatie)
- ICT-dienstverlening (beheerde diensten, beheerde beveiligingsdiensten)
- Overheid (centraal, regionaal)
- Ruimtevaart

**Bijlage II — Overige kritische sectoren:**
- Post en koeriers
- Afvalstoffenbeheer
- Chemische stoffen
- Levensmiddelen
- Fabricage (medische apparatuur, computers, elektronica, machines, voertuigen)
- Digitale aanbieders (online marktplaatsen, online zoekmachines, sociale netwerken)
- Onderzoek

**Omvangsdrempels:**
- Middelgroot: ≥50 werknemers OF ≥€10M omzet/balanstotaal
- Groot: ≥250 werknemers OF ≥€50M omzet OF ≥€43M balanstotaal
- Uitzonderingen: ongeacht omvang voor bepaalde kritieke sectoren (bijv. DNS, TLD, overheid)

**Conclusie:** Valt de organisatie onder NIS2? Zo nee: meld dit en adviseer over vrijwillige maatregelen.

### Stap 2 — Categorie: essentiële of belangrijke entiteit
- **Essentiële entiteit:** Bijlage I sector + groot, OF Bijlage I digitale infrastructuur/overheid/ruimtevaart ongeacht omvang
- **Belangrijke entiteit:** Bijlage I middelgroot, OF Bijlage II middelgroot/groot

Verschil in toezicht:
- Essentieel: proactief toezicht (audits, inspecties)
- Belangrijk: reactief toezicht (na incident of klacht)

### Stap 3 — Zorgplicht (art. 21 NIS2)
Beoordeel de vereiste technische en organisatorische maatregelen:

| Maatregel | Vereist | Huidige status (indien bekend) |
|---|---|---|
| Risicoanalyse en beveiligingsbeleid | Ja | |
| Incidentafhandeling | Ja | |
| Bedrijfscontinuïteit en crisisbeheer | Ja | |
| Beveiliging toeleveringsketen | Ja | |
| Beveiliging bij verwerving systemen | Ja | |
| Effectiviteitsbeoordeling maatregelen | Ja | |
| Basis cyberhygiëne en training | Ja | |
| Cryptografie en encryptie | Ja | |
| Personeelsbeveiliging en toegangsbeheer | Ja | |
| Multi-factor authenticatie (MFA) | Ja | |
| Patchbeheer en kwetsbaarheidsbeheer | Ja | |

### Stap 4 — Meldplicht (art. 23 NIS2)
Tijdlijn bij significante incidenten:
- **24 uur:** Vroege waarschuwing aan CSIRT/bevoegde autoriteit
- **72 uur:** Incidentmelding (oorzaak, ernst, indicatoren van compromittering)
- **1 maand:** Eindrapport (volledige beoordeling, maatregelen, grensoverschrijdend effect)

Wat is een significant incident? Ernstige operationele verstoring OF financiële schade OF impact op anderen.

### Stap 5 — Registratieplicht
Essentiële en belangrijke entiteiten moeten zich registreren bij de bevoegde nationale autoriteit (in Nederland: NCSC/RDI).

### Stap 6 — Persoonlijke aansprakelijkheid bestuurders
- Bestuurders kunnen persoonlijk aansprakelijk worden gesteld voor niet-naleving
- Maximale boetes: essentieel €10M of 2% wereldomzet; belangrijk €7M of 1,4% wereldomzet
- Tijdelijk bestuursverbod mogelijk

### Stap 7 — Actieplan gaps
Op basis van de analyse: welke maatregelen ontbreken of zijn onvoldoende? Prioriteer op basis van risico en deadline.

### Output
Sla de NIS2-check op naar `~/.claude/plugins/config/ictrecht-digital-decade/outputs/nis2-check-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
