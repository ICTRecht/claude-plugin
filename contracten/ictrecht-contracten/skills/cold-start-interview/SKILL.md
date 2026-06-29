---
name: cold-start-interview
description: Stel het ICTRecht Contracten organisatieprofiel in via een interviewgesprek. Voer dit eenmalig uit om alle skills optimaal te personaliseren.
argument-hint: "[optioneel: naam van de organisatie]"
---

# Cold-start interview — ICTRecht Contracten

Dit interview legt het organisatieprofiel vast zodat alle contractenrecht-skills contextbewust werken.

## Voorbereiding

Controleer of er al een profiel bestaat:
1. Lees `~/.claude/plugins/config/ictrecht-contracten/CLAUDE.md` — als dat bestand bestaat, toon de huidige waarden als startsuggesties.
2. Anders: start met lege velden.

Maak de map aan als die nog niet bestaat: `~/.claude/plugins/config/ictrecht-contracten/`.

---

## Interview — stap voor stap

Stel de vragen één voor één. Wacht op antwoord voordat je doorgaat. Gebruik een vriendelijke, professionele toon.

**Stap 1 — Introductie**

Zeg:
> "Welkom bij de ICTRecht Contracten plugin. Ik ga je een aantal vragen stellen om de plugin in te stellen op jouw organisatie. Dit duurt ongeveer 3 minuten. Je kunt het interview later opnieuw uitvoeren om het profiel bij te werken."

**Stap 2 — Organisatienaam**
Vraag: "Wat is de naam van jouw organisatie?"

**Stap 3 — Sector**
Vraag: "In welke sector is jouw organisatie actief? (Bijv. zorg, onderwijs, overheid, SaaS, retail, industrie, financieel, anders)"

**Stap 4 — Omvang**
Vraag: "Hoeveel medewerkers heeft jouw organisatie (bij benadering)?"

**Stap 5 — Rol in contracten**
Vraag: "Wat is de gebruikelijke rol van jouw organisatie in contracten — opdrachtgever, opdrachtnemer, of beide?"

**Stap 6 — Vestigingsland en toepasselijk recht**
Vraag: "In welk(e) land(en) is jouw organisatie gevestigd, en welk recht is doorgaans van toepassing op jullie contracten? (Standaard: Nederlands recht)"

**Stap 7 — Juridisch contactpersoon**
Vraag: "Is er een interne jurist of een vaste externe advocaat/adviseur die betrokken is bij contracten? Zo ja, wie of welk kantoor?"

**Stap 8 — Vaste contractpartijen**
Vraag: "Zijn er vaste contractpartijen of leveranciers waarmee jullie regelmatig samenwerken en waarbij contracten een terugkerende rol spelen? (Namen of type partijen)"

**Stap 9 — Gebruikersrol**
Vraag: "Wat is jouw eigen rol binnen de organisatie ten aanzien van contracten? (Bijv. jurist, inkoper, contractmanager, management, directeur)"

**Stap 10 — Tekenbevoegdheid**
Vraag: "Wie is bevoegd om namens jouw organisatie contracten te tekenen?"

**Stap 11 — Niveau van outputs**
Vraag: "Voor wie zijn de outputs van deze plugin primair bedoeld? (Bijv. intern gebruik door juristen, ter goedkeuring aan bestuur, extern naar contractpartijen)"

---

## Opslaan — drielaagse save

Na het interview sla je het profiel op via drie stappen:

### Stap A — Bestand opslaan
Schrijf het ingevulde profiel naar:
`~/.claude/plugins/config/ictrecht-contracten/CLAUDE.md`

Gebruik de template-structuur uit het plugin-CLAUDE.md maar vervang alle [PLACEHOLDER]-waarden door de gegeven antwoorden.

Maak ook de outputs-map aan:
`~/.claude/plugins/config/ictrecht-contracten/outputs/`

### Stap B — Memory opslaan
Sla een samenvatting op in Claude-geheugen onder de naam **"ICTRecht Contracten organisatieprofiel"** met de kerngegevens:
- Organisatienaam
- Sector
- Rol in contracten
- Toepasselijk recht
- Gebruikersrol
- Tekenbevoegdheid

### Stap C — Project instructions block
Voeg een blok toe aan de project instructions (of CLAUDE.md op projectniveau) met de volgende structuur:

```
## ICTRecht Contracten Profiel
- Organisatie: [naam]
- Sector: [sector]
- Rol: [opdrachtgever/nemer/beide]
- Recht: [toepasselijk recht]
- Gebruikersrol: [rol]
- Tekenbevoegdheid: [wie]
```

---

## Afsluiting

Sluit het interview af met:

> "Profiel opgeslagen. Je kunt nu alle ICTRecht Contracten-skills gebruiken:"
>
> - `/ictrecht-contracten:contract-review` — volledig contract doorlichten op risico's
> - `/ictrecht-contracten:nda-review` — geheimhoudingsovereenkomst controleren
> - `/ictrecht-contracten:algemene-voorwaarden` — AV opstellen of reviewen
> - `/ictrecht-contracten:aansprakelijkheid` — aansprakelijkheidsanalyse
> - `/ictrecht-contracten:onderhandeling-prep` — onderhandeling voorbereiden
> - `/ictrecht-contracten:sla-review` — SLA beoordelen

> ℹ️ *Je gebruikt de basis versie van de ICTRecht Contracten plugin. Wil je toegang tot de volledige ICTRecht kennisbank voor nog nauwkeurigere analyses? Neem contact op via [support@ictrecht.nl](mailto:support@ictrecht.nl).*
