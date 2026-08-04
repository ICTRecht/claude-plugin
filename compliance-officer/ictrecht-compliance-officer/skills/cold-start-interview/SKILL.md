---
name: cold-start-interview
description: >
  Optioneel eenmalig inrichtingsgesprek voor het GEDEELDE ICTRecht-organisatieprofiel.
  Dit profiel wordt door alle geïnstalleerde ICTRecht-plugins herkend — je hoeft dit
  maar één keer te doen, ongeacht hoeveel ICTRecht-plugins je gebruikt. Gebruik dit als
  je nog geen profiel hebt, of als je de Compliance Officer-plugin verder wilt inrichten.
argument-hint: ""
---

# /ictrecht-compliance-officer:cold-start-interview

Dit interview vult het **gedeelde** ICTRecht-organisatieprofiel — hetzelfde profiel dat
door alle geïnstalleerde ICTRecht-plugins wordt gebruikt. Heb je dit al via een andere
ICTRecht-plugin ingevuld? Dan hoef je de basisvragen niet opnieuw te beantwoorden.

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

## Stap 0 — Bestaand profiel checken

Probeer in volgorde:
1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
2. Of zoek in geheugen naar "ICTRecht organisatieprofiel"
3. Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`

**Basisprofiel al aanwezig** (geen [PLACEHOLDER] meer bij "Over de organisatie")?
Toon een korte samenvatting en vraag: "Je hebt al een ICTRecht-organisatieprofiel —
mogelijk aangemaakt via een andere ICTRecht-plugin. Wil je (a) niets doen en direct verder
met de Compliance Officer-skills, (b) alleen de Compliance Officer-specifieke vragen
beantwoorden om dit domein toe te voegen, of (c) het volledige profiel opnieuw doorlopen?"
- (a) → sluit af, klaar.
- (b) → ga direct naar Stap 2 (sla Stap 1 over).
- (c) → ga naar Stap 1.

**"Compliance Officer"-sectie al aanwezig?** Meld dat en vraag of de gebruiker die wil
bijwerken; anders sla Stap 2 over en sluit af.

**Niets van dit alles aanwezig:** ga naar Stap 1.

## Stap 1 — Basisvragen (gelden voor alle ICTRecht-plugins)

Stel de volgende vragen in een vriendelijke, professionele toon. Stel maximaal twee vragen
tegelijk, alleen als ze nog niet beantwoord zijn. Wacht op antwoord voor je verdergaat.

1. Wat is de naam en sector van uw organisatie?
2. Wat is de omvang van de organisatie (bijv. aantal medewerkers of type: mkb / overheid / groot bedrijf)?
3. In welke landen is uw organisatie gevestigd of actief?
4. Wat is uw rol? (bijv. compliance officer, data officer, privacy officer, juridisch adviseur)
5. Wie is het juridisch contactpersoon (indien anders dan uzelf)?
6. Voor welk publiek worden outputs primair opgesteld? (intern gebruik / extern / bestuursniveau)

## Stap 2 — Compliance Officer-specifieke vragen

1. **Datarol**
   "Wat is de rol van uw organisatie ten opzichte van data? Kies één of meerdere:
   - **Data producer** — u genereert data (bijv. IoT-sensoren, systemen)
   - **Data holder** — u beheert en controleert data
   - **Data recipient** — u ontvangt data van anderen
   - **Platform** — u faciliteert data-uitwisseling tussen partijen"

2. **Governance en wetgeving**
   "Welke wetgeving is op uw organisatie van toepassing? (bijv. AVG, EU Data Act, Open Data Richtlijn, sectorspecifieke regelgeving zoals NIS2, DORA, AI Act)"

3. **Data governance structuur**
   "Heeft uw organisatie al een data governance structuur? Zo ja: wie is verantwoordelijk (bijv. CDO, DPO, juridische afdeling)?"

4. **Verwerkingsregister**
   "Wat is de huidige status van het verwerkingsregister? (aanwezig en actueel / in opbouw / ontbreekt)"

5. **Type organisatie**
   "Hoe zou je je organisatie het best omschrijven?
   - Online platform of marktplaats
   - Producent van hardware/software/connected products
   - Dienstverlener (B2B of B2C)
   - Overheid of publieke instelling
   - Kritieke infrastructuur (energie, water, transport, gezondheidszorg)
   - Anders"

6. **EU-markten**
   "In welke EU-lidstaten ben je actief of ben je van plan actief te worden?"

7. **Relevante producten en diensten**
   "Welke producten of diensten zijn het meest relevant voor Compliance Officer-vraagstukken? Denk aan:
   - AI-systemen of AI-ondersteunde producten
   - Online platforms of digitale marktplaatsen
   - Connected products (IoT, smart devices)
   - Digitale identiteitsdiensten
   - Netwerk- en informatiesystemen"

8. **Huidige compliance-status**
   "Welke (EU) regelgeving heb je al geïmplementeerd of ben je mee bezig? (AVG, EU Data Act, AI Act, NIS2, DSA, DMA, eIDAS 2.0, Cyber Resilience Act — of nog niets gestart)"

## Stap 3 — Opslaan (gedeeld bestand, 3 lagen)

**a) Bestand**
Lees/schrijf `~/.claude/plugins/config/ictrecht/CLAUDE.md`.
- Bestaat het bestand nog niet: maak het aan met de basisvelden ingevuld en voeg de
  `### Compliance Officer`-sectie toe onder "Domeinspecifieke aanvullingen".
- Bestaat het al: VUL AAN. Overschrijf nooit basisvelden of secties van andere domeinen
  die al ingevuld zijn — voeg alleen je eigen sectie toe of werk die bij.
Maak ook aan: `~/.claude/plugins/config/ictrecht-compliance-officer/outputs/`.

**b) Geheugen**
Sla het VOLLEDIGE actuele profiel (basisvelden + alle tot nu toe bekende domeinsecties) op
onder de titel "ICTRecht organisatieprofiel". Update de bestaande entry als die er al is;
maak geen tweede entry aan.

**c) Projectinstructies-blok**
Toon het complete, actuele blok `## ICTRecht Profiel` (inclusief alle tot nu toe ingevulde
domeinsecties), zodat de gebruiker dit kan kopiëren naar de instructies van een Claude
Project:

```
--- KOPIEER DIT NAAR JE CLAUDE PROJECT INSTRUCTIES ---

## ICTRecht Profiel

**Organisatie:** [naam]
**Sector:** [sector]
**Omvang:** [medewerkers]
**Vestigingsland:** [land]
**Rol:** [rol]
**Juridisch contactpersoon:** [intern / extern / nvt]

### Compliance Officer
**Rol t.o.v. data:** [producer/holder/recipient/platform]
**Toepasselijke wetgeving:** [wetgeving]
**Data governance structuur:** [verantwoordelijke]
**Huidige verwerkingsregister:** [status]
**Type organisatie:** [platform/producent/dienstverlener/overheid/kritieke infra]
**Actief in EU-markten:** [landen]
**Relevante producten/diensten:** [lijst]
**Huidige compliance-status:** [status]

Alle ICTRecht-plugins gebruiken dit gedeelde profiel als organisatiecontext.

--- EINDE BLOK ---
```

## Stap 4 — Afsluiting

Toon een overzicht van het opgeslagen profiel en meld:

> "Compliance Officer is toegevoegd aan je ICTRecht-organisatieprofiel. Je kunt nu alle
> `/ictrecht-compliance-officer:`-skills gebruiken met je organisatiecontext:
> - `/ictrecht-compliance-officer:verwerkingsregister`
> - `/ictrecht-compliance-officer:data-sharing`
> - `/ictrecht-compliance-officer:data-governance`
> - `/ictrecht-compliance-officer:data-act`
> - `/ictrecht-compliance-officer:open-data`
> - `/ictrecht-compliance-officer:dataverdrag-analyse`
> - `/ictrecht-compliance-officer:risico-analyse`
> - `/ictrecht-compliance-officer:compliance-check`
> - `/ictrecht-compliance-officer:regelgeving-scan`
> - `/ictrecht-compliance-officer:ai-act-classificatie`
> - `/ictrecht-compliance-officer:nis2-check`
> - `/ictrecht-compliance-officer:dsa-verplichtingen`
> - `/ictrecht-compliance-officer:dma-analyse`
> - `/ictrecht-compliance-officer:cyberweerbaarheid-act`
>
> Andere ICTRecht-plugins gebruiken automatisch dit gedeelde profiel — je hoeft dit
> interview niet opnieuw te doen als je een andere ICTRecht-plugin installeert. Gebruik
> `/ictrecht-compliance-officer:cold-start-interview` opnieuw om dit domein bij te werken."

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-compliance-officer/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
