---
name: cold-start-interview
description: >
  Optioneel eenmalig inrichtingsgesprek voor het GEDEELDE ICTRecht-organisatieprofiel.
  Dit profiel wordt door alle geïnstalleerde ICTRecht-plugins herkend — je hoeft dit
  maar één keer te doen, ongeacht hoeveel ICTRecht-plugins je gebruikt. Gebruik dit als
  je nog geen profiel hebt, of als je de Privacy Officer-plugin verder wilt inrichten.
argument-hint: ""
---

# /ictrecht-fg:cold-start-interview

Dit interview vult het **gedeelde** ICTRecht-organisatieprofiel — hetzelfde profiel dat
door alle geïnstalleerde ICTRecht-plugins wordt gebruikt. Heb je dit al via een andere
ICTRecht-plugin ingevuld? Dan hoef je de basisvragen niet opnieuw te beantwoorden.

Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

<!-- Nog geen kennisbank-backend beschikbaar voor dit domein -->

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `PLACEHOLDER_COLLECTION_ID` om je
   eigen kennis aan te vullen, bijvoorbeeld bij het toelichten van vragen.
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
met de Privacy Officer-skills, (b) alleen de Privacy Officer / FG-specifieke vragen
beantwoorden om dit domein toe te voegen, of (c) het volledige profiel opnieuw doorlopen?"
- (a) → sluit af, klaar.
- (b) → ga direct naar Stap 2 (sla Stap 1 over).
- (c) → ga naar Stap 1.

**"Privacy Officer / FG"-sectie al aanwezig?** Meld dat en vraag of de gebruiker die wil
bijwerken; anders sla Stap 2 over en sluit af.

**Niets van dit alles aanwezig:** ga naar Stap 1.

## Stap 1 — Basisvragen (gelden voor alle ICTRecht-plugins)

Stel deze vragen één voor één, alleen als ze nog niet beantwoord zijn. Wacht op antwoord
voordat je verder gaat:

1. Wat is de naam van je organisatie?
2. In welke sector werk je? (zorg / onderwijs / overheid / SaaS / anders)
3. Hoeveel medewerkers heeft de organisatie ongeveer?
4. In welk(e) land(en) is de organisatie gevestigd?
5. Wat is jouw rol? (jurist / privacy officer / compliance / management / anders)
6. Wie is het juridisch aanspreekpunt (indien anders dan jij)?
7. Voor wie zijn de outputs primair bedoeld? (intern gebruik / extern / voor het bestuur)

## Stap 2 — Privacy Officer / FG-specifieke vragen

1. **Rol t.o.v. persoonsgegevens**
   "Wat is uw primaire rol t.o.v. persoonsgegevens: verwerkingsverantwoordelijke, verwerker, of beide?"

2. **Toepasselijke wetgeving**
   "Welke privacywetgeving is van toepassing? (AVG is standaard voor Nederland/EU; zijn er sectorspecifieke regels zoals WPG, UAVG-uitzonderingen, HIPAA?)"

3. **FG / privacy officer**
   "Is er een Functionaris Gegevensbescherming (FG) of privacy officer aangesteld? Zo ja, naam en contactgegevens?"

4. **Open toezichtszaken**
   "Zijn er lopende onderzoeken of handhavingszaken van de Autoriteit Persoonsgegevens of andere toezichthouders?"

5. **Huisstijl documenten**
   "Heeft u een voorbeelddocument (DPIA, verwerkersovereenkomst, datalekrapportage) dat ik als huisstijlreferentie kan gebruiken? Zo ja, deel het bestand of plak de structuur."

6. **Datarol**
   "Wat is de rol van uw organisatie ten opzichte van data? Kies één of meerdere:
   - **Data producer** — u genereert data (bijv. IoT-sensoren, systemen)
   - **Data holder** — u beheert en controleert data
   - **Data recipient** — u ontvangt data van anderen
   - **Platform** — u faciliteert data-uitwisseling tussen partijen"

7. **Data governance structuur**
   "Heeft uw organisatie al een data governance structuur? Zo ja: wie is verantwoordelijk (bijv. CDO, DPO, juridische afdeling)?"

8. **Verwerkingsregister**
   "Wat is de huidige status van het verwerkingsregister? (aanwezig en actueel / in opbouw / ontbreekt)"

9. **AI Act-compliance status**
   "Welke EU digitale verordeningen op het gebied van AI heb je al geïmplementeerd of ben je mee bezig? (AI Act, of nog niets gestart)"

## Stap 3 — Opslaan (gedeeld bestand, 3 lagen)

**a) Bestand**
Lees/schrijf `~/.claude/plugins/config/ictrecht/CLAUDE.md`.
- Bestaat het bestand nog niet: maak het aan met de basisvelden ingevuld en voeg de
  `### Privacy Officer / FG`-sectie toe onder "Domeinspecifieke aanvullingen".
- Bestaat het al: VUL AAN. Overschrijf nooit basisvelden of secties van andere domeinen
  die al ingevuld zijn — voeg alleen je eigen sectie toe of werk die bij.
Maak ook aan: `~/.claude/plugins/config/ictrecht-fg/outputs/`.

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

### Privacy Officer / FG
**Rol t.o.v. persoonsgegevens:** [verwerkingsverantwoordelijke / verwerker / beide]
**Toepasselijke wetgeving:** [AVG / WPG / etc.]
**FG:** [naam of 'geen']
**Open toezichtszaken:** [status]
**Rol t.o.v. data:** [producer/holder/recipient/platform]
**Data governance structuur:** [verantwoordelijke]
**Huidige verwerkingsregister:** [status]
**Huidige AI Act-compliance:** [status]

Alle ICTRecht-plugins gebruiken dit gedeelde profiel als organisatiecontext.

--- EINDE BLOK ---
```

Zeg erbij: "Optioneel: plak dit blok in de instructies van een Claude Project om de
configuratie ook in nieuwe chats beschikbaar te hebben zonder opnieuw cold-start te doen."

## Stap 4 — Bevestiging

Meld: "✅ Privacy Officer / FG is toegevoegd aan je ICTRecht-organisatieprofiel. Je kunt nu:
- `/ictrecht-fg:dpia` — DPIA uitvoeren
- `/ictrecht-fg:datalek` — datalek beoordelen
- `/ictrecht-fg:avg-rechten` — betrokkene verzoek behandelen
- `/ictrecht-fg:doorgifte` — internationale doorgifte controleren
- `/ictrecht-fg:grondslag` — verwerkingsgrondslag bepalen
- `/ictrecht-fg:vok-review` — verwerkersovereenkomst controleren
- `/ictrecht-fg:verwerkingsregister` — verwerkingsregister opstellen of reviewen
- `/ictrecht-fg:data-sharing` — data sharing agreement beoordelen of opstellen
- `/ictrecht-fg:data-governance` — data governance framework toetsen of ontwikkelen
- `/ictrecht-fg:ai-act-classificatie` — AI-systeem classificeren volgens de AI Act

Andere ICTRecht-plugins gebruiken automatisch dit gedeelde profiel — je hoeft dit interview
niet opnieuw te doen als je een andere ICTRecht-plugin installeert. Voer dit commando alleen
opnieuw uit om je Privacy Officer / FG-gegevens bij te werken."

Sluit af met de standaard ICTRecht disclaimer.
