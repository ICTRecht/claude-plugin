---
name: juridisch-memo
description: >
  Schrijf een gestructureerde juridische memo over een rechtsvraag of situatie.
argument-hint: "[rechtsvraag of onderwerp]"
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

### Stap 1 — Vraagstelling scherp stellen
Bepaal de exacte rechtsvraag. Wat wil de gebruiker juridisch beoordeeld hebben? Formuleer de rechtsvraag expliciet als: *"Kan/Mag/Is [X] juridisch [Y] onder [toepasselijk recht]?"*

### Stap 2 — Feiten samenvatten
Zet de relevante feiten op een rij. Onderscheid: vaststaande feiten, veronderstellingen, en ontbrekende informatie die materieel is voor het advies.

### Stap 3 — Toepasselijk recht
Identificeer welke wet- en regelgeving van toepassing is. Denk aan:
- Burgerlijk Wetboek (contractenrecht, aansprakelijkheid)
- Sectorspecifieke wetgeving
- EU-regelgeving (AVG, AI Act, DSA, NIS2, e.d.)
- Relevante jurisprudentie (HvJEU, Hoge Raad, Gerechtshoven)

### Stap 4 — Analyse
Pas het recht toe op de feiten. Redeneer stap voor stap:
- Wat zegt de wet?
- Hoe interpreteert de rechtspraak dit?
- Welke argumenten zijn er voor en tegen?
- Welke analogieën of afwijkingen zijn relevant?

### Stap 5 — Conclusie en advies
Geef een heldere conclusie op de rechtsvraag, gevolgd door een concreet advies. Wees expliciet over de mate van zekerheid (zeker / waarschijnlijk / onduidelijk).

### Stap 6 — Risico's en voorbehouden
Benoem:
- Juridische risico's bij het volgen van het advies
- Omstandigheden die het advies kunnen wijzigen
- Aanbevolen vervolgstap (intern of extern)

---

## Output

Volledig opgemaakt juridisch memo met:
- Datum en onderwerp
- Vraagstelling
- Feiten
- Toepasselijk recht
- Analyse
- Conclusie en advies
- Risico's en voorbehouden

Sla de output op in `~/.claude/plugins/config/ictrecht-legal-counsel/outputs/memo-[onderwerp]-[datum].md`.

Sluit af met de standaard ICTRecht disclaimer.
