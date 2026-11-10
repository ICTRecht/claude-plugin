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

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-compliance-officer:cold-start-interview` uit voor gepersonaliseerde analyse. Nu wordt generieke NIS2 check toegepast.*

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
Essentiële en belangrijke entiteiten moeten zich registreren bij de bevoegde nationale autoriteit (in Nederland: de RDI; het NCSC fungeert als CSIRT).

**Nederlandse implementatie:** NIS2 wordt in Nederland geïmplementeerd via de **Cyberbeveiligingswet (Cbw)**, de opvolger van de Wbni. De implementatie is later dan de EU-deadline van 17 oktober 2024 — controleer de actuele stand van inwerkingtreding en de per sector aangewezen toezichthouders.

### Stap 6 — Persoonlijke aansprakelijkheid bestuurders
- Bestuurders kunnen persoonlijk aansprakelijk worden gesteld voor niet-naleving
- Maximale boetes: essentieel €10M of 2% wereldomzet; belangrijk €7M of 1,4% wereldomzet
- Tijdelijk bestuursverbod mogelijk

### Stap 7 — Actieplan gaps
Op basis van de analyse: welke maatregelen ontbreken of zijn onvoldoende? Prioriteer op basis van risico en deadline.

### Output
Sla de NIS2-check op naar `~/.claude/plugins/config/ictrecht-compliance-officer/outputs/nis2-check-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
