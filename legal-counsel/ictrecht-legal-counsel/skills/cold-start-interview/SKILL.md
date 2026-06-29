# Skill: cold-start-interview

**name:** cold-start-interview
**description:** Stel vragen om het organisatieprofiel voor ICTRecht Legal Counsel in te vullen en sla dit op als gebruikersconfiguratie.
**argument-hint:** *(geen argument nodig)*

---

## Doel

Verzamel informatie over de organisatie en de gebruiker zodat alle andere skills van `ictrecht-legal-counsel` contextueel en relevant advies kunnen geven. Sla het resultaat op in:

`~/.claude/plugins/config/ictrecht-legal-counsel/CLAUDE.md`

---

## Werkwijze

### Stap 1 — Welkom en uitleg

Leg uit wat je gaat doen:

> "Ik stel je een aantal vragen om jouw organisatieprofiel in te stellen voor de ICTRecht Legal Counsel plugin. Dit duurt ongeveer 5 minuten. Je kunt vragen overslaan door 'overslaan' te typen."

### Stap 2 — Vragen (stel één voor één)

1. **Organisatie en sector**
   Wat is de naam van jouw organisatie, en in welke sector is zij actief? *(bijv. SaaS, zorg, overheid, retail, financiën)*

2. **Juridische structuur**
   Wat is de juridische vorm? *(BV / NV / stichting / overheidsinstelling / anders)*
   Hoeveel medewerkers heeft de organisatie (globaal)?
   In welk(e) land(en) is de organisatie gevestigd of actief?

3. **Interne juridische capaciteit**
   Heeft de organisatie een eigen juridische afdeling of vaste externe raadsman? *(eigen afdeling / externe raadsman / geen / anders)*

4. **Primaire rechtsvragen**
   Wat zijn de meest voorkomende juridische vraagstukken? *(bijv. IT-contracten, AVG/privacy, aanbestedingen, arbeidsrecht, geschillen, IP, AI Act, NIS2)*

5. **Mandaat van de gebruiker**
   Wat is jouw rol? *(bijv. general counsel, jurist, compliance officer, management)*
   Wat is jouw mandaat? *(bijv. adviesbevoegdheid, tekenbevoegdheid, escalatieniveau)*

6. **Escalatiepad**
   Als een juridisch vraagstuk de interne capaciteit overstijgt — wie of welke partij wordt dan ingeschakeld? *(bijv. externe advocaat, ICTRecht, RvB)*

### Stap 3 — Samenvatting ter bevestiging

Presenteer een samenvatting van de antwoorden en vraag:

> "Klopt dit overzicht? Wil je iets aanpassen voordat ik het opsla?"

### Stap 4 — Opslaan op 3 plekken

Sla het profiel op als volgt:

**1. Bestand**
Schrijf naar `~/.claude/plugins/config/ictrecht-legal-counsel/CLAUDE.md` — gebruik het template uit `CLAUDE.md` van de plugin, vul alle `[PLACEHOLDER]`-velden in met de verzamelde antwoorden.

**2. Memory**
Sla een beknopte samenvatting op in project memory onder de naam:
`ICTRecht Legal Counsel organisatieprofiel`

Formaat:
```
Organisatie: [naam] | Sector: [sector] | Structuur: [juridische vorm] | Medewerkers: [aantal] | Vestiging: [land(en)] | Juridische capaciteit: [eigen/extern/geen] | Primaire rechtsvragen: [lijst] | Rol gebruiker: [rol] | Mandaat: [mandaat] | Escalatiepad: [escalatiepad]
```

**3. Project instructions block**
Voeg toe aan de actieve project instructions (CLAUDE.md van het project):

```markdown
## ICTRecht Legal Counsel Profiel

**Organisatie:** [naam]
**Sector:** [sector]
**Juridische structuur:** [vorm]
**Omvang:** [medewerkers]
**Vestiging:** [land(en)]
**Toepasselijk recht:** Nederlands recht
**Juridische capaciteit:** [eigen/extern/geen]
**Primaire rechtsvragen:** [lijst]
**Rol gebruiker:** [rol]
**Mandaat:** [mandaat]
**Escalatiepad:** [escalatiepad]
```

### Stap 5 — Afsluiting

Bevestig dat alles is opgeslagen en wijs op de beschikbare skills:

> "Je profiel is opgeslagen. Je kunt nu de volgende skills gebruiken:
> - `/ictrecht-legal-counsel:juridisch-memo` — juridische memo opstellen
> - `/ictrecht-legal-counsel:risico-analyse` — juridische risico's in kaart brengen
> - `/ictrecht-legal-counsel:compliance-check` — toetsing aan wet- en regelgeving
> - `/ictrecht-legal-counsel:regelgeving-scan` — toepasselijke regelgeving bepalen
> - `/ictrecht-legal-counsel:geschil-voorbereiding` — geschilstrategie bepalen
> - `/ictrecht-legal-counsel:advies-structuur` — juridisch advies structureren"
