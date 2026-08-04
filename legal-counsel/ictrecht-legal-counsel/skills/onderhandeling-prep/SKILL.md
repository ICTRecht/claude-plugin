---
name: onderhandeling-prep
description: Bereid een contractonderhandeling voor met strategie, prioriteiten en BATNA.
argument-hint: "[beschrijf het contract en de onderhandelingssituatie]"
---

# Onderhandelingsvoorbereiding

Bereid een contractonderhandeling grondig voor met een heldere strategie, prioriteitenmatrix, BATNA-analyse en gespreksagenda.

## Voorbereiding

Laad het organisatieprofiel via de volgende prioriteitsvolgorde:
1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` — gebruik de waarden voor context.
2. Als dat bestand niet bestaat: zoek in het Claude-geheugen naar **"ICTRecht organisatieprofiel"**.
3. Als dat ook ontbreekt: zoek in de project instructions naar het blok `## ICTRecht Profiel`.
4. Als geen van de drie bronnen beschikbaar is: ga door met generieke BW-standaardinstellingen en toon:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-legal-counsel:cold-start-interview` uit voor gepersonaliseerde analyses. Nu wordt voortgegaan met generieke Nederlandse rechtsstandaarden.*

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

### Stap 1 — Context vaststellen

Vraag (indien niet opgegeven):
- Welk type contract staat ter discussie?
- Wie zijn de partijen, en wat is de machtsverhouding? (bijv. grote leverancier vs. kleine klant)
- Wat is de aanleiding voor de onderhandeling? (nieuw contract, heronderhandeling, conflict)
- Wat zijn de voornaamste belangen van jouw organisatie?
- Wat vermoed je dat de andere partij wil bereiken?
- Wat is de tijdsdruk? (deadline, contractverlenging nadert)

### Stap 2 — Prioriteitenmatrix

Classificeer alle relevante contractpunten in drie categorieën:

**Must-have (niet onderhandelbaar):**
- [Punt 1 — bijv. aansprakelijkheidscap op jaarbedrag]
- [Punt 2 — bijv. eigendom van door ons ontwikkelde data]
- [Punt 3 — ...]

**Nice-to-have (gewenst, maar niet dealbreaker):**
- [Punt 1 — bijv. kortere opzegtermijn]
- [Punt 2 — bijv. SLA-credits bij uitval]
- [Punt 3 — ...]

**Inruilbaar (kan opgegeven worden als concessie):**
- [Punt 1 — bijv. betalingstermijn van 30 naar 45 dagen]
- [Punt 2 — bijv. exclusiviteitsclausule]
- [Punt 3 — ...]

Geef per punt een korte motivering.

### Stap 3 — Kwetsbare clausules

Analyseer waar de andere partij sterk staat en waar jij kwetsbaar bent:
- Welke standaardclausules van de andere partij zijn voor hen juridisch gunstig?
- Welke clausules in de huidige concepttekst beperken jouw bewegingsvrijheid?
- Waar heeft de andere partij marktmacht of juridische precedenten in hun voordeel?
- Welke clausules zijn in de rechtspraak al eens uitgelegd ten nadele van een vergelijkbare positie?

### Stap 4 — BATNA-analyse

Bepaal het BATNA (Best Alternative to a Negotiated Agreement):

**Jouw BATNA:**
- Wat is het beste alternatief als deze onderhandeling mislukt?
- Zijn er andere leveranciers, klanten of contractvormen beschikbaar?
- Wat zijn de kosten van het niet sluiten van dit contract?

**BATNA van de andere partij (inschatting):**
- Hebben zij alternatieven?
- Hoe afhankelijk zijn zij van dit contract?
- Wat is hun incentive om tot overeenstemming te komen?

**Conclusie:** Wie heeft de sterkste BATNA? Wat zegt dit over de onderhandelingspositie?

### Stap 5 — Openingsbod en concessiestrategie

Formuleer een onderhandelingsstrategie:

**Openingspositie:**
- Begin met iets ambitieuzer dan het doel om ruimte te laten voor concessies.
- Welke eisen stel je als eerste aan de orde?

**Concessievolgorde:**
- Welke inruilbare punten geef je als eerste prijs?
- Koppel concessies altijd: "Als jullie X accepteren, kunnen wij Y overwegen."
- Bewaar de must-haves voor het einde van de onderhandeling.

**Rode lijnen:**
- Welke punten zijn absoluut niet onderhandelbaar?
- Wat is de deal-breaker die de onderhandeling beëindigt?

### Stap 6 — Gespreksagenda en rode lijnen

Stel een concrete gespreksagenda op:

**Agenda:**
1. Introductie en doelstelling van het gesprek
2. Vaststellen gezamenlijk belang
3. Bespreking [punt 1]
4. Bespreking [punt 2]
5. [...]
6. Samenvatting afspraken en vervolgstappen

**Rode lijnen om te bewaken:**
- [Rode lijn 1]
- [Rode lijn 2]
- [Rode lijn 3]

**Afsluiting:**
Altijd schriftelijk bevestigen wat is overeengekomen, ook tussentijds.

---

## Output

Sla de output op als:
`~/.claude/plugins/config/ictrecht-legal-counsel/outputs/onderhandeling-prep-[datum]-[onderwerp].md`

Als opslaan niet mogelijk is, toon de volledige voorbereiding in de chat.

---

Sluit af met de standaard ICTRecht disclaimer.
