---
name: cold-start-interview
description: >
  Optioneel eenmalig inrichtingsgesprek voor het GEDEELDE ICTRecht-organisatieprofiel.
  Dit profiel wordt door alle geïnstalleerde ICTRecht-plugins herkend — je hoeft dit
  maar één keer te doen, ongeacht hoeveel ICTRecht-plugins je gebruikt. Gebruik dit als
  je nog geen profiel hebt, of als je de Contracten-plugin verder wilt inrichten.
argument-hint: ""
---

# /ictrecht-contracten:cold-start-interview

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
met de Contracten-skills, (b) alleen de contractenrecht-specifieke vragen beantwoorden om
dit domein toe te voegen, of (c) het volledige profiel opnieuw doorlopen?"
- (a) → sluit af, klaar.
- (b) → ga direct naar Stap 2 (sla Stap 1 over).
- (c) → ga naar Stap 1.

**"Contractenrecht"-sectie al aanwezig?** Meld dat en vraag of de gebruiker die wil
bijwerken; anders sla Stap 2 over en sluit af.

**Niets van dit alles aanwezig:** ga naar Stap 1.

## Stap 1 — Basisvragen (gelden voor alle ICTRecht-plugins)

Stel deze vragen één voor één, alleen als ze nog niet beantwoord zijn. Wacht op antwoord
voordat je verder gaat. Gebruik een vriendelijke, professionele toon.

Zeg vooraf:
> "Welkom bij de ICTRecht Contracten plugin. Ik ga je een aantal vragen stellen om het
> gedeelde ICTRecht-organisatieprofiel in te stellen. Dit duurt ongeveer 3-5 minuten."

1. Wat is de naam van je organisatie?
2. In welke sector werk je? (zorg / onderwijs / overheid / SaaS / anders)
3. Hoeveel medewerkers heeft de organisatie ongeveer?
4. In welk(e) land(en) is de organisatie gevestigd?
5. Wat is jouw rol? (jurist / inkoper / contractmanager / management / anders)
6. Wie is het juridisch aanspreekpunt (indien anders dan jij)?
7. Voor wie zijn de outputs primair bedoeld? (intern gebruik / extern / voor het bestuur)

## Stap 2 — Contractenrecht-specifieke vragen

1. **Rol in contracten**
   "Wat is de gebruikelijke rol van jouw organisatie in contracten — opdrachtgever, opdrachtnemer, of beide?"

2. **Toepasselijk recht**
   "Welk recht is doorgaans van toepassing op jullie contracten? (Standaard: Nederlands recht)"

3. **Vaste contractpartijen**
   "Zijn er vaste contractpartijen of leveranciers waarmee jullie regelmatig samenwerken en waarbij contracten een terugkerende rol spelen? (Namen of type partijen)"

4. **Tekenbevoegdheid**
   "Wie is bevoegd om namens jouw organisatie contracten te tekenen?"

## Stap 3 — Opslaan (gedeeld bestand, 3 lagen)

**a) Bestand**
Lees/schrijf `~/.claude/plugins/config/ictrecht/CLAUDE.md`.
- Bestaat het bestand nog niet: maak het aan met de basisvelden ingevuld en voeg de
  `### Contractenrecht`-sectie toe onder "Domeinspecifieke aanvullingen".
- Bestaat het al: VUL AAN. Overschrijf nooit basisvelden of secties van andere domeinen
  die al ingevuld zijn — voeg alleen je eigen sectie toe of werk die bij.
Maak ook aan: `~/.claude/plugins/config/ictrecht-contracten/outputs/`.

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

### Contractenrecht
**Rol in contracten:** [opdrachtgever/nemer/beide]
**Toepasselijk recht:** [recht]
**Vaste contractpartijen:** [partijen]
**Tekenbevoegdheid:** [wie]

Alle ICTRecht-plugins gebruiken dit gedeelde profiel als organisatiecontext.

--- EINDE BLOK ---
```

Zeg erbij: "Optioneel: plak dit blok in de instructies van een Claude Project om de
configuratie ook in nieuwe chats beschikbaar te hebben zonder opnieuw cold-start te doen."

## Stap 4 — Afsluiting

Sluit af met:

> "Contractenrecht is toegevoegd aan je ICTRecht-organisatieprofiel. Je kunt nu:
>
> - `/ictrecht-contracten:contract-review` — volledig contract doorlichten op risico's
> - `/ictrecht-contracten:nda-review` — geheimhoudingsovereenkomst controleren
> - `/ictrecht-contracten:algemene-voorwaarden` — AV opstellen of reviewen
> - `/ictrecht-contracten:aansprakelijkheid` — aansprakelijkheidsanalyse
> - `/ictrecht-contracten:onderhandeling-prep` — onderhandeling voorbereiden
> - `/ictrecht-contracten:sla-review` — SLA beoordelen
>
> Andere ICTRecht-plugins gebruiken automatisch dit gedeelde profiel — je hoeft dit
> interview niet opnieuw te doen als je een andere ICTRecht-plugin installeert."

> ℹ️ *Je gebruikt de gratis versie van de ICTRecht Contracten plugin. Wil je toegang tot de volledige ICTRecht kennisbank voor nog nauwkeurigere analyses? Neem contact op via [support@ictrecht.nl](mailto:support@ictrecht.nl).*
