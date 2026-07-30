---
name: aansprakelijkheid
description: Analyseer aansprakelijkheidsclausules en beperkingen in een contract of situatie.
argument-hint: "[beschrijf de situatie of plak de relevante contractclausules]"
---

# Aansprakelijkheidsanalyse

Analyseer aansprakelijkheidsclausules en -beperkingen in een contract of concrete situatie, inclusief het wettelijk kader en de maximale blootstelling.

## Voorbereiding

Laad het organisatieprofiel via de volgende prioriteitsvolgorde:
1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` — gebruik de waarden voor context.
2. Als dat bestand niet bestaat: zoek in het Claude-geheugen naar **"ICTRecht organisatieprofiel"**.
3. Als dat ook ontbreekt: zoek in de project instructions naar het blok `## ICTRecht Profiel`.
4. Als geen van de drie bronnen beschikbaar is: ga door met generieke BW-standaardinstellingen en toon:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-contracten:cold-start-interview` uit voor gepersonaliseerde analyses. Nu wordt voortgegaan met generieke Nederlandse rechtsstandaarden.*

---

## Werkwijze

### Stap 1 — Feitelijke situatie

Vraag (indien niet opgegeven):
- Wat is er (dreigt te) gebeuren? (schade, wanprestatie, een incident, of een contractreview)
- Welke partijen zijn betrokken?
- Gaat het om een bestaand contract? Zo ja, deel de relevante clausules.
- Wat is de aard van de schade? (vermogensschade, gevolgschade, immateriële schade, reputatieschade)
- Wat is de geschatte omvang van de schade?

### Stap 2 — Contractuele aansprakelijkheidsbeperkingen

Analyseer de relevante contractclausules:
- Is er een aansprakelijkheidsbeperking (cap) opgenomen?
- Op welk bedrag of welke maatstaf is de cap gebaseerd? (bijv. contractwaarde per jaar, vast bedrag)
- Welke schadesoorten zijn uitgesloten? (gevolgschade, gederfde winst, indirecte schade)
- Zijn er uitzonderingen op de beperking? (bijv. opzet, grove schuld, inbreuk op IP, datalekken)
- Gelden de beperkingen wederzijds of alleen voor één partij?

### Stap 3 — Wettelijk kader

Bespreek het toepasselijke wettelijk kader:

**Wanprestatie (art. 6:74 BW):**
- Is er een toerekenbare tekortkoming?
- Wat zijn de vereisten voor schadevergoeding (schade, causaal verband, toerekenbaarheid)?
- Is ingebrekestelling vereist?

**Onrechtmatige daad (art. 6:162 BW):**
- Is er een onrechtmatige gedraging, schade en causaal verband?
- Welke schadevergoedingsregels gelden?

**Relativiteit (art. 6:163 BW):**
- Strekt de geschonden norm tot bescherming van de benadeelde?

**Eigen schuld (art. 6:101 BW):**
- Is er sprake van eigen schuld aan de zijde van de benadeelde?

### Stap 4 — Geldigheid van de beperking

Beoordeel of de aansprakelijkheidsbeperking standhoudt:

- **Opzet / bewuste roekeloosheid:** Een beroep op een beding dat aansprakelijkheid uitsluit voor opzet of bewuste roekeloosheid van de schuldenaar zelf of van tot de bedrijfsleiding behorende personen, is naar maatstaven van redelijkheid en billijkheid onaanvaardbaar (art. 6:248 lid 2 BW; vaste rechtspraak van de Hoge Raad). Het beding is dus niet automatisch nietig, maar kan in zoverre niet worden ingeroepen.
- **B2C-context:** Is het beding onredelijk bezwarend voor een consument? (zwarte/grijze lijst BW)
- **Specifieke wetgeving:** Gelden er bijzondere regels? (bijv. productaansprakelijkheid, AVG-boetes)
- **Derogerende werking van redelijkheid en billijkheid:** Kan de beperking naar maatstaven van redelijkheid en billijkheid onaanvaardbaar zijn?

Oordeel: **Geldig / Mogelijk aantastbaar / Waarschijnlijk nietig** (met motivering)

### Stap 5 — Blootstelling berekenen

Bereken of schat de maximale aansprakelijkheid:
- Contractuele cap: [bedrag of formule]
- Uitgesloten schadesoorten: [overzicht]
- Resterende blootstelling: [schatting]
- Vergelijk met de werkelijke of verwachte schade

Geef een overzicht:
| Scenario | Contractuele aansprakelijkheid | Wettelijke aansprakelijkheid (zonder beperking) |
|---|---|---|
| Minimaal | | |
| Verwacht | | |
| Maximaal | | |

### Stap 6 — Advies

Geef concrete aanbevelingen:
- Is de huidige aansprakelijkheidsbeperking toereikend?
- Welke aanpassingen zijn gewenst?
- Zijn er verzekeringen relevant? (bijv. beroepsaansprakelijkheidsverzekering, cyber-verzekering)
- Wat is het procesrisico als het tot een procedure komt?

---

## Output

Sla de output op als:
`~/.claude/plugins/config/ictrecht-contracten/outputs/aansprakelijkheid-[datum]-[onderwerp].md`

Als opslaan niet mogelijk is, toon de volledige analyse in de chat.

---

Sluit af met de standaard ICTRecht disclaimer.
