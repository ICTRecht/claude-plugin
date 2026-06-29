---
name: sla-review
description: Beoordeel een Service Level Agreement op volledigheid, realisme en juridische risico's.
argument-hint: "[plak SLA-tekst of geef bestandspad]"
---

# SLA Review

Beoordeel een Service Level Agreement (SLA) op volledigheid, haalbaarheid, juridische risico's en de bescherming van de belangen van de gebruiker.

## Voorbereiding

Laad het organisatieprofiel via de volgende prioriteitsvolgorde:
1. Lees `~/.claude/plugins/config/ictrecht-contracten/CLAUDE.md` — gebruik de waarden voor context.
2. Als dat bestand niet bestaat: zoek in het Claude-geheugen naar **"ICTRecht Contracten organisatieprofiel"**.
3. Als dat ook ontbreekt: zoek in de project instructions naar het blok `## ICTRecht Contracten Profiel`.
4. Als geen van de drie bronnen beschikbaar is: ga door met generieke BW-standaardinstellingen en toon:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-contracten:cold-start-interview` uit voor gepersonaliseerde analyses. Nu wordt voortgegaan met generieke Nederlandse rechtsstandaarden.*

---

## Werkwijze

### Stap 1 — Dienst en context

Vraag (indien niet opgegeven):
- Wat wordt er geleverd? (bijv. SaaS-platform, hosting, beheerd netwerk, applicatiebeheer)
- Aan wie? (intern of aan externe klanten; B2B of B2C)
- Wat is de kritikaliteit van de dienst voor de afnemer? (missiekritisch / bedrijfskritisch / niet-kritisch)
- Wat is de rol van de gebruiker: dienstverlener of afnemer?
- Is de SLA een zelfstandig document of onderdeel van een raamovereenkomst?

### Stap 2 — Kernindicatoren

Beoordeel de kern-SLA-indicatoren op aanwezigheid, duidelijkheid en haalbaarheid:

| Indicator | Aanwezig | Waarde | Realistisch? | Opmerking |
|---|---|---|---|---|
| Uptime percentage (bijv. 99,9%) | | | | |
| Beschikbaarheidsvenster (bijv. 24/7 of kantoortijden) | | | | |
| Responstijd bij incident (P1/P2/P3) | | | | |
| Oplostijd bij incident (P1/P2/P3) | | | | |
| Geplande onderhoudsvensters | | | | |
| Meetmethodiek (hoe wordt uptime gemeten?) | | | | |
| Rapportageperiode | | | | |

**Aandachtspunten bij meetmethodiek:**
- Wie meet? (leverancier zelf of onafhankelijke tool — risico op partijdigheid)
- Wat telt mee als "downtime"? (gedeeltelijke uitval, degraded performance)
- Hoe worden geplande onderhoudsmomenten behandeld?

### Stap 3 — Consequenties bij niet-nakoming

Analyseer de remedies bij het niet halen van SLA-niveaus:

**Credits:**
- Is er een creditregeling opgenomen?
- Hoe worden credits berekend? (percentage van maandfactuur, vast bedrag)
- Is er een maximum aan credits per periode?
- Is de creditregeling de enige remedy, of kan de afnemer ook andere aanspraken maken?

**Boetes:**
- Zijn er contractuele boetes naast of in plaats van credits?
- Zijn boetes proportioneel?

**Exit-rechten:**
- Geeft langdurige of herhaalde SLA-schending recht op opzegging?
- Wat zijn de drempelwaarden? (bijv. 3x overschrijding binnen 6 maanden)
- Zijn er overgangsbepalingen bij vroegtijdige beëindiging?

**Juridische grondslag:**
- Zijn credits en boetes een volledige regeling, of behoudt de afnemer wettelijke rechten (art. 6:74 BW / wanprestatie)?

### Stap 4 — Uitsluitingen en overmacht

Controleer welke situaties expliciet buiten de SLA-berekening vallen:

- Gepland onderhoud (met of zonder aankondigingstermijn)
- Overmacht (force majeure) — is de definitie redelijk begrensd?
- Storingen veroorzaakt door de afnemer zelf
- Storingen bij derde partijen (internet, DNS, cloud providers)
- Aanvallen van buitenaf (DDoS)

Beoordeel: zijn de uitsluitingen redelijk, of zijn ze zo breed dat de SLA-garanties illusoir worden?

### Stap 5 — Rapportage en monitoring

Controleer:
- Is de leverancier verplicht periodiek SLA-rapportages te leveren?
- Wat is de frequentie? (maandelijks, kwartaal)
- Heeft de afnemer toegang tot een statuspage of real-time monitoring?
- Wie initieert de creditprocedure: de leverancier automatisch, of de afnemer op verzoek?
- Zijn er escalatieprocedures voor ernstige incidenten?

### Stap 6 — Beoordeling realistisch/onrealistisch + rode vlaggen

Geef een eindoordeel:

**Realisme:**
- Zijn de SLA-niveaus technisch en operationeel haalbaar voor dit type dienst?
- Zijn respons- en oplostijden realistisch gezien de aard van de dienst en de beschikbare support?

**Rode vlaggen — opsomming:**
Gebruik het volgende format:

🔴 **[Titel rode vlag]**
Probleem: [beschrijving]
Risico: [juridisch of operationeel gevolg]
Aanbeveling: [concrete aanpassing]

**Eindoordeel:** Gebalanceerd / Leveranciersvriendelijk / Afnemersvriendelijk — met een korte toelichting.

---

## Output

Sla de output op als:
`~/.claude/plugins/config/ictrecht-contracten/outputs/sla-review-[datum]-[onderwerp].md`

Als opslaan niet mogelijk is, toon de volledige analyse in de chat.

---

Sluit af met de standaard ICTRecht disclaimer.
