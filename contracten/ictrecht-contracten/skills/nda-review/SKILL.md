---
name: nda-review
description: Controleer een geheimhoudingsovereenkomst (NDA) op volledigheid en eenzijdigheid.
argument-hint: "[plak NDA-tekst of geef bestandspad]"
---

# NDA Review

Voer een grondige controle uit van een geheimhoudingsovereenkomst (NDA) op volledigheid, eenzijdigheid en juridische risico's voor de gebruiker.

## Voorbereiding

Laad het organisatieprofiel via de volgende prioriteitsvolgorde:
1. Lees `~/.claude/plugins/config/ictrecht-contracten/CLAUDE.md` — gebruik de waarden voor context.
2. Als dat bestand niet bestaat: zoek in het Claude-geheugen naar **"ICTRecht Contracten organisatieprofiel"**.
3. Als dat ook ontbreekt: zoek in de project instructions naar het blok `## ICTRecht Contracten Profiel`.
4. Als geen van de drie bronnen beschikbaar is: ga door met generieke BW-standaardinstellingen en toon:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-contracten:cold-start-interview` uit voor gepersonaliseerde analyses. Nu wordt voortgegaan met generieke Nederlandse rechtsstandaarden.*

---

## Werkwijze

### Stap 1 — Type NDA en context

Vraag (indien niet opgegeven als argument):
- Is dit een eenzijdige NDA (één partij deelt) of een wederzijdse NDA (beide partijen delen)?
- Wie zijn de partijen?
- Wat is het doel van de NDA? (bijv. pre-contractuele samenwerking, M&A due diligence, pilotproject)
- Wat is de rol van de gebruiker: de partij die informatie deelt of ontvangt?

Lees vervolgens de aangeleverde NDA-tekst.

### Stap 2 — Kernbepalingen checklist

Controleer de aanwezigheid en kwaliteit van alle kernbepalingen:

| Bepaling | Aanwezig | Kwaliteit | Opmerking |
|---|---|---|---|
| Definitie vertrouwelijke informatie | | | |
| Uitzonderingen op vertrouwelijkheid | | | |
| Verplichtingen ontvangende partij | | | |
| Looptijd geheimhouding tijdens overeenkomst | | | |
| Looptijd geheimhouding na beëindiging | | | |
| Return/destroy clause (teruggave/vernietiging) | | | |
| Sancties bij schending | | | |
| Boeteclausule | | | |
| Toepasselijk recht | | | |
| Forumkeuze | | | |

**Beoordeling per bepaling:**

- **Definitie vertrouwelijke informatie:** Is de definitie voldoende breed/smal? Omvat het ook mondelinge informatie? Is er een markering vereist?
- **Uitzonderingen:** Zijn de standaarduitzonderingen opgenomen (openbaar domein, reeds bekende informatie, onafhankelijke ontwikkeling, wettelijke verplichting tot openbaarmaking)?
- **Verplichtingen:** Zijn de verplichtingen van de ontvangende partij concreet en handhaafbaar?
- **Looptijd na beëindiging:** Is er een post-contractuele geheimhoudingsperiode? Hoe lang? Is dit redelijk?
- **Return/destroy:** Is er een expliciete verplichting tot teruggave of vernietiging bij beëindiging? Geldt dit ook voor kopieën?
- **Sancties:** Zijn de sancties proportioneel en handhaafbaar?

### Stap 3 — Eenzijdigheidstoets

Analyseer wie het meeste risico draagt:
- Zijn de verplichtingen symmetrisch (wederzijdse NDA) of asymmetrisch?
- Zijn de definities en uitzonderingen gelijkwaardig voor beide partijen?
- Wie bepaalt wat vertrouwelijk is?
- Wie draagt de bewijslast bij een vermeende schending?
- Is de boeteclausule (indien aanwezig) eenzijdig?

Geef een oordeel: **Gebalanceerd / Licht nadelig voor gebruiker / Sterk nadelig voor gebruiker**

### Stap 4 — Concrete verbeterpunten

Geef per ontbrekende bepaling of onbalans een concreet voorstel:

**Punt:** [beschrijving]
**Probleem:** [wat ontbreekt of klopt niet]
**Voorstel:** [concrete tekstsuggestie of aanvulling]

---

## Output

Sla de output op als:
`~/.claude/plugins/config/ictrecht-contracten/outputs/nda-review-[datum]-[onderwerp].md`

Als opslaan niet mogelijk is, toon de volledige analyse in de chat.

---

Sluit af met de standaard ICTRecht disclaimer.
