---
name: cold-start-interview
description: >
  Optioneel eenmalig inrichtingsgesprek voor het GEDEELDE ICTRecht-organisatieprofiel.
  Dit profiel wordt door alle geïnstalleerde ICTRecht-plugins herkend — je hoeft dit
  maar één keer te doen, ongeacht hoeveel ICTRecht-plugins je gebruikt. Gebruik dit als
  je nog geen profiel hebt, of als je de Digital Decade-plugin verder wilt inrichten.
argument-hint: ""
---

# /ictrecht-digital-decade:cold-start-interview

Dit interview vult het **gedeelde** ICTRecht-organisatieprofiel — hetzelfde profiel dat
door alle geïnstalleerde ICTRecht-plugins wordt gebruikt. Heb je dit al via een andere
ICTRecht-plugin ingevuld? Dan hoef je de basisvragen niet opnieuw te beantwoorden.

## Stap 0 — Bestaand profiel checken

Probeer in volgorde:
1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
2. Of zoek in geheugen naar "ICTRecht organisatieprofiel"
3. Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`

**Basisprofiel al aanwezig** (geen [PLACEHOLDER] meer bij "Over de organisatie")?
Toon een korte samenvatting en vraag of de gebruiker (a) niets wil doen en direct verder
wil met de Digital Decade-skills, (b) alleen de Digital Decade-specifieke vragen wil
beantwoorden om dit domein toe te voegen, of (c) het volledige profiel opnieuw wil doorlopen.
- (a) → sluit af, klaar.
- (b) → ga direct naar het Interview hieronder (sla de basisvragen over).
- (c) → ga naar de basisvragen.

**"Digital Decade"-sectie al aanwezig?** Meld dat en vraag of de gebruiker die wil
bijwerken; anders sla het interview over en sluit af.

**Niets van dit alles aanwezig:** ga naar de basisvragen.

## Basisvragen (gelden voor alle ICTRecht-plugins)

Stel deze vragen één voor één (conversationeel), alleen als ze nog niet beantwoord zijn:

1. Wat is de naam van je organisatie en in welke sector ben je actief? (bijv. tech, financiën, zorg, overheid, retail, industrie)
2. In welk(e) land(en) is de organisatie gevestigd?
3. Hoeveel medewerkers heeft de organisatie ongeveer?
4. Wat is jouw rol binnen de organisatie? (bijv. compliance officer, jurist, CTO, product manager, directie/bestuur)
5. Wie is het juridisch aanspreekpunt (indien anders dan jij)?
6. Voor wie zijn de outputs primair bedoeld? (intern / extern / bestuur)

## Interview — Digital Decade-specifieke vragen

1. **Type organisatie**
   Hoe zou je je organisatie het best omschrijven?
   - Online platform of marktplaats
   - Producent van hardware/software/connected products
   - Dienstverlener (B2B of B2C)
   - Overheid of publieke instelling
   - Kritieke infrastructuur (energie, water, transport, gezondheidszorg)
   - Anders

2. **EU-markten**
   In welke EU-lidstaten ben je actief of ben je van plan actief te worden?

3. **Relevante producten en diensten**
   Welke producten of diensten zijn het meest relevant voor Digital Decade compliance? Denk aan:
   - AI-systemen of AI-ondersteunde producten
   - Online platforms of digitale marktplaatsen
   - Connected products (IoT, smart devices)
   - Digitale identiteitsdiensten
   - Netwerk- en informatiesystemen

4. **Huidige compliance status**
   Welke EU digitale verordeningen heb je al geïmplementeerd of ben je mee bezig? (AI Act, NIS2, DSA, DMA, eIDAS 2.0, Cyber Resilience Act — of nog niets gestart)

## Opslaan (gedeeld bestand, 3 lagen)

**a) Bestand**
Lees/schrijf `~/.claude/plugins/config/ictrecht/CLAUDE.md`.
- Bestaat het bestand nog niet: maak het aan met de basisvelden ingevuld en voeg de
  `### Digital Decade`-sectie toe onder "Domeinspecifieke aanvullingen".
- Bestaat het al: VUL AAN. Overschrijf nooit basisvelden of secties van andere domeinen
  die al ingevuld zijn — voeg alleen je eigen sectie toe of werk die bij.
Maak ook aan: `~/.claude/plugins/config/ictrecht-digital-decade/outputs/`.

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

### Digital Decade
**Type organisatie:** [platform/producent/dienstverlener/overheid/kritieke infra]
**Actief in EU-markten:** [landen]
**Relevante producten/diensten:** [lijst]
**Huidige Digital Decade compliance:** [status]

Alle ICTRecht-plugins gebruiken dit gedeelde profiel als organisatiecontext.

--- EINDE BLOK ---
```

## Afsluiting

Geef een overzicht van het opgeslagen profiel en meld welke skills nu beschikbaar zijn:
- `/ictrecht-digital-decade:ai-act-classificatie`
- `/ictrecht-digital-decade:nis2-check`
- `/ictrecht-digital-decade:dsa-verplichtingen`
- `/ictrecht-digital-decade:dma-analyse`
- `/ictrecht-digital-decade:cyberweerbaarheid-act`
- `/ictrecht-digital-decade:regulering-scan`

Vermeld: "Andere ICTRecht-plugins gebruiken automatisch dit gedeelde profiel — je hoeft dit
interview niet opnieuw te doen als je een andere ICTRecht-plugin installeert."

---

Sluit af met de standaard ICTRecht disclaimer.
