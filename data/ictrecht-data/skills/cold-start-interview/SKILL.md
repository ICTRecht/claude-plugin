---
name: cold-start-interview
description: >
  Optioneel eenmalig inrichtingsgesprek voor het GEDEELDE ICTRecht-organisatieprofiel.
  Dit profiel wordt door alle geïnstalleerde ICTRecht-plugins herkend — je hoeft dit
  maar één keer te doen, ongeacht hoeveel ICTRecht-plugins je gebruikt. Gebruik dit als
  je nog geen profiel hebt, of als je de Data-plugin verder wilt inrichten.
argument-hint: ""
---

# /ictrecht-data:cold-start-interview

Dit interview vult het **gedeelde** ICTRecht-organisatieprofiel — hetzelfde profiel dat
door alle geïnstalleerde ICTRecht-plugins wordt gebruikt. Heb je dit al via een andere
ICTRecht-plugin ingevuld? Dan hoef je de basisvragen niet opnieuw te beantwoorden.

## Stap 0 — Bestaand profiel checken

Probeer in volgorde:
1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
2. Of zoek in geheugen naar "ICTRecht organisatieprofiel"
3. Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`

**Basisprofiel al aanwezig** (geen [PLACEHOLDER] meer bij "Over de organisatie")?
Toon een korte samenvatting en vraag: "Je hebt al een ICTRecht-organisatieprofiel —
mogelijk aangemaakt via een andere ICTRecht-plugin. Wil je (a) niets doen en direct verder
met de Data-skills, (b) alleen de data-specifieke vragen beantwoorden om dit domein toe te
voegen, of (c) het volledige profiel opnieuw doorlopen?"
- (a) → sluit af, klaar.
- (b) → ga direct naar Stap 2 (sla Stap 1 over).
- (c) → ga naar Stap 1.

**"Data (juridisch)"-sectie al aanwezig?** Meld dat en vraag of de gebruiker die wil
bijwerken; anders sla Stap 2 over en sluit af.

**Niets van dit alles aanwezig:** ga naar Stap 1.

## Stap 1 — Basisvragen (gelden voor alle ICTRecht-plugins)

Stel de volgende vragen in een vriendelijke, professionele toon. Stel maximaal twee vragen
tegelijk, alleen als ze nog niet beantwoord zijn. Wacht op antwoord voor je verdergaat.

1. Wat is de naam en sector van uw organisatie?
2. Wat is de omvang van de organisatie (bijv. aantal medewerkers of type: mkb / overheid / groot bedrijf)?
3. In welke landen is uw organisatie gevestigd of actief?
4. Wat is uw rol? (bijv. data officer, privacy officer, juridisch adviseur, compliance manager)
5. Wie is het juridisch contactpersoon (indien anders dan uzelf)?
6. Voor welk publiek worden outputs primair opgesteld? (intern gebruik / extern / bestuursniveau)

## Stap 2 — Data-specifieke vragen

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

## Stap 3 — Opslaan (gedeeld bestand, 3 lagen)

**a) Bestand**
Lees/schrijf `~/.claude/plugins/config/ictrecht/CLAUDE.md`.
- Bestaat het bestand nog niet: maak het aan met de basisvelden ingevuld en voeg de
  `### Data (juridisch)`-sectie toe onder "Domeinspecifieke aanvullingen".
- Bestaat het al: VUL AAN. Overschrijf nooit basisvelden of secties van andere domeinen
  die al ingevuld zijn — voeg alleen je eigen sectie toe of werk die bij.
Maak ook aan: `~/.claude/plugins/config/ictrecht-data/outputs/`.

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

### Data (juridisch)
**Rol t.o.v. data:** [producer/holder/recipient/platform]
**Toepasselijke wetgeving:** [wetgeving]
**Data governance structuur:** [verantwoordelijke]
**Huidige verwerkingsregister:** [status]

Alle ICTRecht-plugins gebruiken dit gedeelde profiel als organisatiecontext.

--- EINDE BLOK ---
```

## Stap 4 — Afsluiting

Toon een overzicht van het opgeslagen profiel en meld:

> "Data (juridisch) is toegevoegd aan je ICTRecht-organisatieprofiel. Je kunt nu alle
> `/ictrecht-data:`-skills gebruiken met je organisatiecontext:
> - `/ictrecht-data:verwerkingsregister`
> - `/ictrecht-data:data-sharing`
> - `/ictrecht-data:data-governance`
> - `/ictrecht-data:data-act`
> - `/ictrecht-data:open-data`
> - `/ictrecht-data:dataverdrag-analyse`
>
> Andere ICTRecht-plugins gebruiken automatisch dit gedeelde profiel — je hoeft dit
> interview niet opnieuw te doen als je een andere ICTRecht-plugin installeert. Gebruik
> `/ictrecht-data:cold-start-interview` opnieuw om dit domein bij te werken."

---

## Outputs

Sla gegenereerde bestanden op in:
`~/.claude/plugins/config/ictrecht-data/outputs/`

Sluit af met de standaard ICTRecht disclaimer.
