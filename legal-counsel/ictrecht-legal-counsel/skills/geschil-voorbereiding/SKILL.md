# Skill: geschil-voorbereiding

**name:** geschil-voorbereiding
**description:** Analyseer een juridisch geschil en bepaal strategie, positie en opties.
**argument-hint:** "[beschrijving van het geschil]"

---

## Voorbereiding — configuratie laden (3-laags fallback)

Laad het organisatieprofiel in deze volgorde:

1. **Bestand** — lees `~/.claude/plugins/config/ictrecht-legal-counsel/CLAUDE.md`
2. **Memory** — zoek naar memory-entry `ICTRecht Legal Counsel organisatieprofiel`
3. **Project instructions** — zoek naar blok `## ICTRecht Legal Counsel Profiel` in de actieve project instructions

Als **geen van de drie** beschikbaar is:
- Ga door met generieke standaardinstellingen (Nederlands recht, algemene IT-rechtpraktijk)
- Toon bovenaan de output:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-legal-counsel:cold-start-interview` uit voor gepersonaliseerde output.*

---

## Werkwijze

### Stap 1 — Feiten en tijdlijn
Zet de feitelijke gang van zaken chronologisch op een rij:
- Wat is er feitelijk gebeurd?
- Wanneer (tijdlijn met datums)?
- Wie zijn de betrokken partijen en wat is hun rol?
- Welke documenten, correspondentie of bewijsstukken zijn beschikbaar?
- Welke feiten zijn vaststaand, welke zijn betwist?

### Stap 2 — Juridische grondslag
Identificeer de juridische basis van het geschil:
- **Contractbreuk** — welke contractuele verplichtingen zijn geschonden?
- **Onrechtmatige daad** — art. 6:162 BW, welke norm is geschonden?
- **Garantie of vrijwaring** — welke garanties zijn gegeven of geschonden?
- **Wettelijke verplichting** — overtreding van welke wettelijke norm?
- **Ongegronde verrijking** — art. 6:212 BW

### Stap 3 — Eigen positie vs. wederpartij
Analyseer de sterkte van de eigen positie:

**Sterktes eigen positie:**
- [Contractuele grondslag, bewijs, etc.]

**Zwaktes eigen positie:**
- [Risico's, tegenargumenten, bewijsproblemen]

**Sterktes wederpartij:**
- [Tegenargumenten, bewijsstukken, etc.]

**Zwaktes wederpartij:**
- [Juridische kwetsbaarheden]

Geef een inschatting van de kans van slagen (hoog / middel / laag) met onderbouwing.

### Stap 4 — Opties
Beschrijf de beschikbare routes voor geschiloplossing:
- **Schikking** — onderhandelen over minnelijke oplossing; voor- en nadelen
- **Mediation** — neutrale derde partij; geschikt als relatie behoud gewenst
- **Arbitrage** — bindende beslissing buiten rechtbank; sneller, vertrouwelijker
- **Rechtbank** — bodemprocedure of kort geding; tijdlijn en kosteninschatting
- **Klachtprocedure** — toezichthouder of brancheorganisatie

### Stap 5 — BATNA
Bepaal de Best Alternative To a Negotiated Agreement:
- Wat is het beste alternatief als geen overeenstemming wordt bereikt?
- Wat is de bodemprijs / minimumacceptabele uitkomst?
- Welke concessies zijn acceptabel?

### Stap 6 — Strategie en first steps
Formuleer een concrete strategie:
- Aanbevolen route (met motivering)
- Communicatiestrategie richting wederpartij
- Bewijsveiligstelling (welke documenten direct veiligstellen?)
- First steps: concreet actieplan voor de komende 2 weken
- Wie moet erbij worden betrokken (intern / extern)?

---

## Output

Volledig geschilanalyserapport met tijdlijn, juridische grondslag, positie-analyse, opties, BATNA en strategie met first steps.

Sla de output op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/geschil-[onderwerp]-[datum].md`.

Sluit af met de standaard ICTRecht disclaimer.
