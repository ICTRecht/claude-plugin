---
name: cold-start-interview
description: >
  Richt de ICTRecht Privacy plugin in voor jouw organisatie. Stel dit eenmalig in —
  alle andere commando's zijn ervan afhankelijk. Gebruik dit als je de plugin voor
  het eerst installeert, of als de organisatiegegevens zijn gewijzigd.
argument-hint: "[--check-integraties]"
---

# /ictrecht-privacy-basis:cold-start-interview

Richt de plugin in voor deze organisatie. Duurt 10-15 minuten.

## Stap 1 — Configuratiepad voorbereiden

Maak de volgende map aan als die niet bestaat:
`~/.claude/plugins/config/ictrecht-privacy-basis/`
`~/.claude/plugins/config/ictrecht-privacy-basis/outputs/`

Kopieer het CLAUDE.md template van de plugin-installatiemap naar:
`~/.claude/plugins/config/ictrecht-privacy-basis/CLAUDE.md`

## Stap 2 — Organisatieprofiel

Stel de volgende vragen één voor één. Wacht op antwoord voordat je verder gaat:

1. **Organisatienaam en sector**
   "Wat is de naam van uw organisatie en in welke sector is u actief? (bijv. zorg, onderwijs, SaaS, overheid, financiën)"

2. **Omvang en rol**
   "Hoeveel medewerkers heeft de organisatie? En wat is uw primaire rol t.o.v. persoonsgegevens: verwerkingsverantwoordelijke, verwerker, of beide?"

3. **Vestiging en toepasselijk recht**
   "In welk(e) land(en) is de organisatie gevestigd en welke privacywetgeving is van toepassing? (AVG is standaard voor Nederland/EU; zijn er sectorspecifieke regels zoals WPG, UAVG-uitzonderingen, HIPAA?)"

4. **FG / privacy officer**
   "Is er een Functionaris Gegevensbescherming (FG) of privacy officer aangesteld? Zo ja, naam en contactgegevens?"

5. **Juridisch contact**
   "Wie is het juridisch aanspreekpunt? (interne jurist, extern advocaat, of is de gebruiker zelf jurist?)"

6. **Rol gebruiker**
   "Wat is uw eigen rol? (jurist / privacy officer / compliance / management / anders)"

7. **Open toezichtszaken**
   "Zijn er lopende onderzoeken of handhavingszaken van de Autoriteit Persoonsgegevens of andere toezichthouders?"

8. **Huisstijl documenten**
   "Heeft u een voorbeelddocument (DPIA, verwerkersovereenkomst, datalekrapportage) dat ik als huisstijlreferentie kan gebruiken? Zo ja, deel het bestand of plak de structuur."

## Stap 3 — Configuratie opslaan

Sla de ingevulde antwoorden op via drie kanalen (in volgorde):

**3a. Bestand** (voor Claude Code gebruikers)
Schrijf weg naar `~/.claude/plugins/config/ictrecht-privacy-basis/CLAUDE.md`.
Vervang alle [PLACEHOLDER] markers. Behoud de koppenstructuur.
Als het pad niet beschikbaar is, sla deze stap over.

**3b. Geheugen** (voor alle omgevingen)
Sla het organisatieprofiel op in Claude-geheugen onder de naam "ICTRecht Privacy organisatieprofiel".
Formaat: compacte samenvatting van naam, sector, omvang, rol, FG, wetgeving en gebruikersrol.

**3c. Projectinstructies-blok genereren**
Toon onderaan dit bericht een kant-en-klaar tekstblok dat de gebruiker kan kopiëren naar de instructies van een Claude Project:

```
--- KOPIEER DIT NAAR JE CLAUDE PROJECT INSTRUCTIES ---

## ICTRecht Privacy Profiel

**Organisatie:** [ingevulde naam]
**Sector:** [sector]
**Omvang:** [medewerkers]
**Rol t.o.v. persoonsgegevens:** [verwerkingsverantwoordelijke / verwerker / beide]
**Vestigingsland:** [land]
**Toepasselijke wetgeving:** [AVG / WPG / etc.]
**FG:** [naam of 'geen']
**Rol gebruiker:** [jurist / privacy officer / etc.]
**Juridisch contact:** [intern / extern / nvt]

Alle ICTRecht privacy-commando's gebruiken dit profiel als organisatiecontext.

--- EINDE BLOK ---
```

Zeg erbij: "Optioneel: plak dit blok in de instructies van een Claude Project om de configuratie ook in nieuwe chats beschikbaar te hebben zonder opnieuw de cold-start te hoeven doen."

## Stap 4 — Bevestiging

Meld: "✅ ICTRecht Privacy plugin is ingericht voor [organisatienaam]. U kunt nu alle commando's gebruiken:
- `/ictrecht-privacy-basis:dpia` — DPIA uitvoeren
- `/ictrecht-privacy-basis:datalek` — datalek beoordelen
- `/ictrecht-privacy-basis:avg-rechten` — betrokkene verzoek behandelen
- `/ictrecht-privacy-basis:doorgifte` — internationale doorgifte controleren
- `/ictrecht-privacy-basis:grondslag` — verwerkingsgrondslag bepalen
- `/ictrecht-privacy-basis:vok-review` — verwerkersovereenkomst controleren"
