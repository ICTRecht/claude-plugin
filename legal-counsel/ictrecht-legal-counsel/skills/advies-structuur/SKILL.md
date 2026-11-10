---
name: advies-structuur
description: >
  Structureer een juridisch advies voor bestuur, management of externe partij.
argument-hint: "[onderwerp en doelgroep van het advies]"
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

### Stap 1 — Doelgroep en doel
Bepaal voor wie het advies bedoeld is en wat het beoogde effect is:
- **Doelgroep:** Raad van Bestuur / management / externe partij / toezichthouder / juridische afdeling
- **Doel:** Welke beslissing moet worden genomen op basis van dit advies?
- **Kennisniveau:** Zijn de lezers juridisch geschoold of niet?
- **Toon:** Formeel extern / intern bestuurlijk / operationeel intern

Stel de toon en het detailniveau van het advies hierop af.

### Stap 2 — Executive summary opstellen
Schrijf een bondige samenvatting (max. 10 regels) die zelfstandig leesbaar is:
- Kern van de situatie (1-2 zinnen)
- Juridische hoofdbevinding (1-2 zinnen)
- Aanbeveling (1 zin)
- Urgentie of deadline (indien van toepassing)

### Stap 3 — Achtergrond en feiten
Beschrijf de context beknopt maar volledig:
- Aanleiding voor het advies
- Relevante feiten en omstandigheden
- Betrokken partijen
- Eerder genomen stappen of besluiten

### Stap 4 — Juridische analyse
Presenteer de juridische analyse toegankelijk voor de doelgroep:
- Toepasselijk juridisch kader (beknopt, vermijd jargon tenzij doelgroep juridisch geschoold)
- Kernbevindingen: wat zegt het recht over deze situatie?
- Eventuele onzekerheden of interpretatiemarge
- Relevante precedenten of toezichthouderstandpunten

### Stap 5 — Opties met voor- en nadelen
Presenteer de beschikbare opties als gestructureerde vergelijking:

| Optie | Voordelen | Nadelen | Risico |
|-------|-----------|---------|--------|
| Optie A | ... | ... | Laag / Middel / Hoog |
| Optie B | ... | ... | Laag / Middel / Hoog |

### Stap 6 — Aanbeveling
Geef een heldere, gemotiveerde aanbeveling:
- Welke optie wordt aanbevolen en waarom?
- Onder welke voorwaarden of voorbehouden?
- Wat zijn de risico's van niet-opvolgen?

### Stap 7 — Volgende stappen
Stel een concreet actieplan voor:
- Wie doet wat?
- Op welke termijn?
- Welke besluiten of goedkeuringen zijn nodig?
- Wanneer vindt terugkoppeling plaats?

---

## Output

Volledig gestructureerd juridisch advies inclusief executive summary, achtergrond, analyse, opties, aanbeveling en actieplan — afgestemd op de doelgroep.

Sla de output op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/advies-[onderwerp]-[datum].md`.

Sluit af met de standaard ICTRecht disclaimer.
