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
   <!-- Nog geen kennisbank-backend beschikbaar voor dit domein --> om eventuele vragen
   over de inrichting te gronden in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen kennis. Vermeld dit NIET als fout,
   waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier om deze
   skill te gebruiken.

---

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

**Juridische structuur en interne organisatie**

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

**Contracten**

6. **Rol in contracten**
   "Wat is de gebruikelijke rol van jouw organisatie in contracten — opdrachtgever, opdrachtnemer, of beide?"

7. **Toepasselijk recht**
   "Welk recht is doorgaans van toepassing op jullie contracten? (Standaard: Nederlands recht)"

8. **Vaste contractpartijen**
   "Zijn er vaste contractpartijen of leveranciers waarmee jullie regelmatig samenwerken en waarbij contracten een terugkerende rol spelen? (Namen of type partijen)"

9. **Tekenbevoegdheid**
   "Wie is bevoegd om namens jouw organisatie contracten te tekenen?"

**Intellectueel eigendom**

10. **Type IE-rechten**
    "Welk type intellectueel eigendom is voor u het meest relevant? (bijv. software, content/creatieve werken, merken, octrooien, bedrijfsgeheimen — meerdere antwoorden mogelijk)"

11. **Actieve markten en landen**
    "In welke landen of markten bent u actief? (relevant voor beschermingsomvang merkenrecht en toepasselijk recht)"

12. **IE-portefeuille**
    "Heeft u geregistreerde merken, domeinnamen, octrooien of andere geregistreerde IE-rechten? Zo ja, welke?"

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
**Rol in contracten:** [opdrachtgever/nemer/beide]
**Toepasselijk recht:** [recht]
**Vaste contractpartijen:** [partijen]
**Tekenbevoegdheid:** [wie]
**Type IE-rechten:** [software / content / merken / octrooien / bedrijfsgeheimen]
**Actief in landen/markten:** [landen]
**IE-portefeuille:** [merken, domeinnamen, octrooien, auteursrechten]

Alle ICTRecht-plugins gebruiken dit gedeelde profiel als organisatiecontext.

--- EINDE BLOK ---
```

Zeg erbij: "Optioneel: plak dit blok in de instructies van een Claude Project om de
configuratie ook in nieuwe chats beschikbaar te hebben zonder opnieuw cold-start te doen."

## Stap 4 — Afsluiting

Bevestig dat alles is opgeslagen en wijs op de beschikbare skills:

> "Legal Counsel is toegevoegd aan je ICTRecht-organisatieprofiel. Je kunt nu de volgende skills gebruiken:
>
> **Contracten**
> - `/ictrecht-legal-counsel:contract-review` — volledig contract doorlichten op risico's
> - `/ictrecht-legal-counsel:nda-review` — geheimhoudingsovereenkomst controleren
> - `/ictrecht-legal-counsel:algemene-voorwaarden` — AV opstellen of reviewen
> - `/ictrecht-legal-counsel:aansprakelijkheid` — aansprakelijkheidsanalyse
> - `/ictrecht-legal-counsel:onderhandeling-prep` — onderhandeling voorbereiden
> - `/ictrecht-legal-counsel:sla-review` — SLA beoordelen
>
> **Juridisch advies en geschillen**
> - `/ictrecht-legal-counsel:juridisch-memo` — juridische memo opstellen
> - `/ictrecht-legal-counsel:risico-analyse` — juridische risico's in kaart brengen
> - `/ictrecht-legal-counsel:geschil-voorbereiding` — geschilstrategie bepalen
> - `/ictrecht-legal-counsel:advies-structuur` — juridisch advies structureren
>
> **Privacy**
> - `/ictrecht-legal-counsel:vok-review` — verwerkersovereenkomst controleren
>
> **Intellectueel eigendom**
> - `/ictrecht-legal-counsel:ie-clausules` — IP-clausules in contracten beoordelen of opstellen
> - `/ictrecht-legal-counsel:auteursrecht` — auteursrechtelijke vragen
> - `/ictrecht-legal-counsel:merkenrecht` — merkenrechtelijke vragen
> - `/ictrecht-legal-counsel:software-licenties` — software- en open source-licenties beoordelen
> - `/ictrecht-legal-counsel:handelsnaam-domeinnaam` — handelsnaam- en domeinnaamconflicten
> - `/ictrecht-legal-counsel:ai-ip` — IE-vraagstukken rondom AI
>
> Andere ICTRecht-plugins gebruiken automatisch dit gedeelde profiel — je hoeft dit
> interview niet opnieuw te doen als je een andere ICTRecht-plugin installeert."
