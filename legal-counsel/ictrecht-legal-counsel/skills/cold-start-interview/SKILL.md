---
name: cold-start-interview
description: >
  Optioneel eenmalig inrichtingsgesprek voor het GEDEELDE ICTRecht-organisatieprofiel.
  Dit profiel wordt door alle geïnstalleerde ICTRecht-plugins herkend — je hoeft dit
  maar één keer te doen, ongeacht hoeveel ICTRecht-plugins je gebruikt. Gebruik dit als
  je nog geen profiel hebt, of als je de Legal Counsel-plugin verder wilt inrichten.
argument-hint: ""
---

# /ictrecht-legal-counsel:cold-start-interview

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
met de Legal Counsel-skills, (b) alleen de legal counsel-specifieke vragen beantwoorden om
dit domein toe te voegen, of (c) het volledige profiel opnieuw doorlopen?"
- (a) → sluit af, klaar.
- (b) → ga direct naar Stap 2 (sla Stap 1 over).
- (c) → ga naar Stap 1.

**"Legal Counsel"-sectie al aanwezig?** Meld dat en vraag of de gebruiker die wil
bijwerken; anders sla Stap 2 over en sluit af.

**Niets van dit alles aanwezig:** ga naar Stap 1.

## Stap 1 — Basisvragen (gelden voor alle ICTRecht-plugins)

Leg vooraf uit wat je gaat doen:
> "Ik stel je een aantal vragen om het gedeelde ICTRecht-organisatieprofiel in te stellen.
> Dit duurt ongeveer 5 minuten. Je kunt vragen overslaan door 'overslaan' te typen."

Stel deze vragen één voor één, alleen als ze nog niet beantwoord zijn:
1. Wat is de naam van je organisatie?
2. In welke sector werk je? (bijv. SaaS, zorg, overheid, retail, financiën)
3. Hoeveel medewerkers heeft de organisatie ongeveer?
4. In welk(e) land(en) is de organisatie gevestigd of actief?
5. Wat is jouw rol? (bijv. general counsel, jurist, compliance officer, management)
6. Wie is het juridisch aanspreekpunt (indien anders dan jij)?
7. Voor wie zijn de outputs primair bedoeld? (intern gebruik / extern / voor het bestuur)

## Stap 2 — Legal Counsel-specifieke vragen

1. **Juridische structuur**
   "Wat is de juridische vorm van de organisatie? (BV / NV / stichting / overheidsinstelling / anders)"

2. **Interne juridische capaciteit**
   "Heeft de organisatie een eigen juridische afdeling of vaste externe raadsman? (eigen afdeling / externe raadsman / geen / anders)"

3. **Primaire rechtsvragen**
   "Wat zijn de meest voorkomende juridische vraagstukken? (bijv. IT-contracten, AVG/privacy, aanbestedingen, arbeidsrecht, geschillen, IP, AI Act, NIS2)"

4. **Mandaat**
   "Wat is jouw mandaat? (bijv. adviesbevoegdheid, tekenbevoegdheid, escalatieniveau)"

5. **Escalatiepad**
   "Als een juridisch vraagstuk de interne capaciteit overstijgt — wie of welke partij wordt dan ingeschakeld? (bijv. externe advocaat, ICTRecht, RvB)"

Presenteer daarna een samenvatting en vraag: "Klopt dit overzicht? Wil je iets aanpassen voordat ik het opsla?"

## Stap 3 — Opslaan (gedeeld bestand, 3 lagen)

**a) Bestand**
Lees/schrijf `~/.claude/plugins/config/ictrecht/CLAUDE.md`.
- Bestaat het bestand nog niet: maak het aan met de basisvelden ingevuld en voeg de
  `### Legal Counsel`-sectie toe onder "Domeinspecifieke aanvullingen".
- Bestaat het al: VUL AAN. Overschrijf nooit basisvelden of secties van andere domeinen
  die al ingevuld zijn — voeg alleen je eigen sectie toe of werk die bij.
Maak ook aan: `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/`.

**b) Geheugen**
Sla het VOLLEDIGE actuele profiel (basisvelden + alle tot nu toe bekende domeinsecties) op
onder de titel "ICTRecht organisatieprofiel". Update de bestaande entry als die er al is;
maak geen tweede entry aan.

**c) Projectinstructies-blok**
Toon onderaan dit bericht het complete, actuele blok `## ICTRecht Profiel` (inclusief alle
tot nu toe ingevulde domeinsecties), zodat de gebruiker dit kan kopiëren naar de instructies
van een Claude Project:

```
--- KOPIEER DIT NAAR JE CLAUDE PROJECT INSTRUCTIES ---

## ICTRecht Profiel

**Organisatie:** [naam]
**Sector:** [sector]
**Omvang:** [medewerkers]
**Vestigingsland:** [land]
**Rol:** [rol]
**Juridisch contactpersoon:** [intern / extern / nvt]

### Legal Counsel
**Juridische structuur:** [vorm]
**Interne juridische functie:** [eigen/extern/geen]
**Primaire juridische vraagstukken:** [lijst]
**Mandaat:** [mandaat]
**Escalatiepad:** [escalatiepad]

Alle ICTRecht-plugins gebruiken dit gedeelde profiel als organisatiecontext.

--- EINDE BLOK ---
```

Zeg erbij: "Optioneel: plak dit blok in de instructies van een Claude Project om de
configuratie ook in nieuwe chats beschikbaar te hebben zonder opnieuw cold-start te doen."

## Stap 4 — Afsluiting

Bevestig dat alles is opgeslagen en wijs op de beschikbare skills:

> "Legal Counsel is toegevoegd aan je ICTRecht-organisatieprofiel. Je kunt nu de volgende skills gebruiken:
> - `/ictrecht-legal-counsel:juridisch-memo` — juridische memo opstellen
> - `/ictrecht-legal-counsel:risico-analyse` — juridische risico's in kaart brengen
> - `/ictrecht-legal-counsel:compliance-check` — toetsing aan wet- en regelgeving
> - `/ictrecht-legal-counsel:regelgeving-scan` — toepasselijke regelgeving bepalen
> - `/ictrecht-legal-counsel:geschil-voorbereiding` — geschilstrategie bepalen
> - `/ictrecht-legal-counsel:advies-structuur` — juridisch advies structureren
>
> Andere ICTRecht-plugins gebruiken automatisch dit gedeelde profiel — je hoeft dit
> interview niet opnieuw te doen als je een andere ICTRecht-plugin installeert."
