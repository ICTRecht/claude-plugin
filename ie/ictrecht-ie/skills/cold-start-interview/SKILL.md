---
name: cold-start-interview
description: >
  Optioneel eenmalig inrichtingsgesprek voor het GEDEELDE ICTRecht-organisatieprofiel.
  Dit profiel wordt door alle geïnstalleerde ICTRecht-plugins herkend — je hoeft dit
  maar één keer te doen, ongeacht hoeveel ICTRecht-plugins je gebruikt. Gebruik dit als
  je nog geen profiel hebt, of als je de IE-plugin verder wilt inrichten.
argument-hint: ""
---

# /ictrecht-ie:cold-start-interview

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
met de IE-skills, (b) alleen de IE-specifieke vragen beantwoorden om dit domein toe te
voegen, of (c) het volledige profiel opnieuw doorlopen?"
- (a) → sluit af, klaar.
- (b) → ga direct naar Stap 2 (sla Stap 1 over).
- (c) → ga naar Stap 1.

**"Intellectueel Eigendom"-sectie al aanwezig?** Meld dat en vraag of de gebruiker die wil
bijwerken; anders sla Stap 2 over en sluit af.

**Niets van dit alles aanwezig:** ga naar Stap 1.

## Stap 1 — Basisvragen (gelden voor alle ICTRecht-plugins)

Stel deze vragen één voor één, alleen als ze nog niet beantwoord zijn:

1. Wat is de naam van je organisatie?
2. In welke sector werk je?
3. Hoeveel medewerkers heeft de organisatie ongeveer?
4. In welk(e) land(en) is de organisatie gevestigd?
5. Wat is jouw rol? (IE-jurist / product manager / marketeer / developer / management)
6. Wie is het juridisch aanspreekpunt (indien anders dan jij)?
7. Voor wie zijn de outputs primair bedoeld? (intern / extern / bestuur)

## Stap 2 — IE-specifieke vragen

1. **Type IE-rechten**
   "Welk type intellectueel eigendom is voor u het meest relevant? (bijv. software, content/creatieve werken, merken, octrooien, bedrijfsgeheimen — meerdere antwoorden mogelijk)"

2. **Actieve markten en landen**
   "In welke landen of markten bent u actief? (relevant voor beschermingsomvang merkenrecht en toepasselijk recht)"

3. **IE-portefeuille**
   "Heeft u geregistreerde merken, domeinnamen, octrooien of andere geregistreerde IE-rechten? Zo ja, welke?"

## Stap 3 — Opslaan (gedeeld bestand, 3 lagen)

**a) Bestand**
Lees/schrijf `~/.claude/plugins/config/ictrecht/CLAUDE.md`.
- Bestaat het bestand nog niet: maak het aan met de basisvelden ingevuld en voeg de
  `### Intellectueel Eigendom`-sectie toe onder "Domeinspecifieke aanvullingen".
- Bestaat het al: VUL AAN. Overschrijf nooit basisvelden of secties van andere domeinen
  die al ingevuld zijn — voeg alleen je eigen sectie toe of werk die bij.
Maak ook aan: `~/.claude/plugins/config/ictrecht-ie/outputs/`.

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

### Intellectueel Eigendom
**Type IE-rechten:** [software / content / merken / octrooien / bedrijfsgeheimen]
**Actief in landen/markten:** [landen]
**IE-portefeuille:** [merken, domeinnamen, octrooien, auteursrechten]

Alle ICTRecht-plugins gebruiken dit gedeelde profiel als organisatiecontext.

--- EINDE BLOK ---
```

## Stap 4 — Afsluiting

Bevestig dat het profiel is opgeslagen en dat toekomstige skills dit profiel automatisch
gebruiken. Vermeld het pad `~/.claude/plugins/config/ictrecht/CLAUDE.md` en de beschikbare
commando's: `/ictrecht-ie:auteursrecht`, `/ictrecht-ie:merkenrecht`,
`/ictrecht-ie:software-licenties`, `/ictrecht-ie:ie-clausules`,
`/ictrecht-ie:handelsnaam-domeinnaam`, `/ictrecht-ie:ai-ip`.

Vermeld: "Andere ICTRecht-plugins gebruiken automatisch dit gedeelde profiel — je hoeft dit
interview niet opnieuw te doen als je een andere ICTRecht-plugin installeert."

Sluit af met de standaard ICTRecht disclaimer.
