---
name: ai-ip
description: >
  Analyseer IE-vraagstukken rondom AI-gegenereerde content, training data en AI-tools.
argument-hint: "[AI-situatie of product]"
---

## Voorbereiding (3-laags)

1. Lees `~/.claude/plugins/config/ictrecht-ie/CLAUDE.md` — gebruik organisatieprofiel als het bestaat en geen [PLACEHOLDER] bevat.
2. Zoek anders in geheugen naar "ICTRecht IE organisatieprofiel".
3. Geen van beide beschikbaar: ga generiek verder en vermeld ℹ️ dat het profiel nog niet is ingevuld; adviseer `/ictrecht-ie:cold-start-interview` uit te voeren.

---

## Workflow

**Stap 1 — Wie/wat heeft de content gegenereerd?**
Stel vast hoe de content tot stand is gekomen:
- Mens + AI (collaboratief): menselijke creatieve input gecombineerd met AI-uitvoer
- Volledig AI: autonoom gegenereerd zonder substantiële menselijke creatieve keuzes
Bespreek de mate van menselijke sturing (prompts, selectie, bewerkingen).

**Stap 2 — Auteursrecht op AI-output**
Analyseer de auteursrechtelijke beschermbaarheid volgens de HvJ EU-lijn: menselijke creatieve keuze is vereist voor auteursrechtelijke bescherming (Infopaq, Painer, Cofemel). Volledig autonome AI-output ontbeert auteursrechtelijke bescherming in de EU. Bespreek de implicaties voor eigendom en commercieel gebruik. Verwijs naar relevante nationale ontwikkelingen.

**Stap 3 — Training data**
Beoordeel of de trainingsdata rechtmatig zijn gebruikt:
- Text and Data Mining (TDM)-exceptie art. 4 DSM-richtlijn (2019/790): toegestaan tenzij opt-out
- Art. 3 DSM-richtlijn: TDM voor wetenschappelijk onderzoek (beperktere toepassing)
- Auteursrechtelijke toestemming bij commerciële trainingsdata buiten TDM-exceptie
- Lopende rechtszaken (Getty Images, New York Times, etc.) als jurisprudentiële context

**Stap 4 — Eigendom AI-output in contracten**
Analyseer de contractuele eigendomsregeling voor AI-gegenereerde output:
- Gebruiksvoorwaarden AI-aanbieder: wat zijn de rechten van de gebruiker vs. aanbieder?
- Werkt de organisatie met eigen AI-modellen: wie is rechthebbende op de output?
- Zijn er afspraken gemaakt met klanten over eigendom van AI-gegenereerde deliverables?
- Risico: niemand is rechthebbende — content valt in het publieke domein

**Stap 5 — Openbaarmaking AI-gebruik**
Bespreek transparantieverplichtingen:
- AI Act (EU) art. 50: transparantieverplichting bij deepfakes en chatbots
- Auteursrechtelijke naamsvermelding bij menselijke bijdrage
- Sectorspecifieke verplichtingen (reclame, journalistiek, wetenschappelijk werk)
- Interne beleidsoverwegingen rondom AI-disclosure

**Stap 6 — Praktisch advies**
Geef concrete aanbevelingen:
- Documenteer menselijke creatieve bijdragen aan AI-output
- Leg eigendomsregelingen contractueel vast (met klanten en opdrachtgevers)
- Controleer gebruiksvoorwaarden van ingezette AI-tools
- Stel intern AI-gebruik beleid op
- Monitor jurisprudentie en regelgeving (snel evoluerend rechtsgebied)

---

## Output

Sla uitgewerkte analyses op in `~/.claude/plugins/config/ictrecht-ie/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
