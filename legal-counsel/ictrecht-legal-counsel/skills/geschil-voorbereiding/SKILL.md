---
name: geschil-voorbereiding
description: >
  Analyseer een juridisch geschil en bepaal strategie, positie en opties.
argument-hint: "[beschrijving van het geschil]"
---

## Voorbereiding — configuratie laden (3-laags fallback)

Laad het organisatieprofiel in deze volgorde:

1. **Bestand** — lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
2. **Memory** — zoek naar memory-entry `ICTRecht organisatieprofiel`
3. **Project instructions** — zoek naar blok `## ICTRecht Profiel` in de actieve project instructions

Als **geen van de drie** beschikbaar is:
- Ga door met generieke standaardinstellingen (Nederlands recht, algemene IT-rechtpraktijk)
- Toon bovenaan de output:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-legal-counsel:cold-start-interview` uit voor gepersonaliseerde output.*

Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

---

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `PLACEHOLDER_COLLECTION_ID`
   <!-- Nog geen kennisbank-backend beschikbaar voor dit domein --> om je analyse te
   gronden in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

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
