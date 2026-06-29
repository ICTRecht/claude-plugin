---
name: onderhandeling-prep
description: Bereid een contractonderhandeling voor met strategie, prioriteiten en BATNA.
argument-hint: "[beschrijf het contract en de onderhandelingssituatie]"
---

# Onderhandelingsvoorbereiding

Bereid een contractonderhandeling grondig voor met een heldere strategie, prioriteitenmatrix, BATNA-analyse en gespreksagenda.

## Voorbereiding

Laad het organisatieprofiel via de volgende prioriteitsvolgorde:
1. Lees `~/.claude/plugins/config/ictrecht-contracten/CLAUDE.md` — gebruik de waarden voor context.
2. Als dat bestand niet bestaat: zoek in het Claude-geheugen naar **"ICTRecht Contracten organisatieprofiel"**.
3. Als dat ook ontbreekt: zoek in de project instructions naar het blok `## ICTRecht Contracten Profiel`.
4. Als geen van de drie bronnen beschikbaar is: ga door met generieke BW-standaardinstellingen en toon:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-contracten:cold-start-interview` uit voor gepersonaliseerde analyses. Nu wordt voortgegaan met generieke Nederlandse rechtsstandaarden.*

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
`~/.claude/plugins/config/ictrecht-contracten/outputs/onderhandeling-prep-[datum]-[onderwerp].md`

Als opslaan niet mogelijk is, toon de volledige voorbereiding in de chat.

---

Sluit af met de standaard ICTRecht disclaimer.
