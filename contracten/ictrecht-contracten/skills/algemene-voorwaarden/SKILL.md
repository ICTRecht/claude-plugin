---
name: algemene-voorwaarden
description: Stel algemene voorwaarden op of toets bestaande AV aan wet- en regelgeving.
argument-hint: "[plak bestaande AV-tekst, of beschrijf de dienst/het product]"
---

# Algemene Voorwaarden — Opstellen of Reviewen

Stel nieuwe algemene voorwaarden op of toets bestaande AV aan de wettelijke vereisten van het Burgerlijk Wetboek, met bijzondere aandacht voor IT-specifieke clausules.

## Voorbereiding

Laad het organisatieprofiel via de volgende prioriteitsvolgorde:
1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` — gebruik de waarden voor context.
2. Als dat bestand niet bestaat: zoek in het Claude-geheugen naar **"ICTRecht organisatieprofiel"**.
3. Als dat ook ontbreekt: zoek in de project instructions naar het blok `## ICTRecht Profiel`.
4. Als geen van de drie bronnen beschikbaar is: ga door met generieke BW-standaardinstellingen en toon:

> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-contracten:cold-start-interview` uit voor gepersonaliseerde analyses. Nu wordt voortgegaan met generieke Nederlandse rechtsstandaarden.*

---

## Werkwijze

### Stap 1 — Context vaststellen

Vraag (indien niet opgegeven):
- Is dit een B2B- of B2C-situatie (of beide)?
- Wat is het product of de dienst? (bijv. softwareontwikkeling, SaaS-abonnement, IT-consultancy, hardware, combinatie)
- In welke sector opereert de organisatie?
- Moeten de AV worden opgesteld (nieuw) of getoetst (bestaand)?
- Is er een specifiek aandachtspunt? (bijv. aansprakelijkheidsbeperking, intellectueel eigendom, opzegtermijnen)

### Stap 2 — Wettelijke vereisten

Toets of de AV voldoen aan de wettelijke minimumeisen:

**Algemene AV-regelgeving (art. 6:231–247 BW):**
- Zijn de AV tijdig ter hand gesteld of digitaal beschikbaar gesteld (art. 6:233 sub b en 6:234 BW; voor dienstverrichters ook art. 6:230c BW)?
- Is er een verwijzing naar de AV in de overeenkomst?
- Bij B2C: zijn er bedingen die op de zwarte lijst (art. 6:236 BW) of grijze lijst (art. 6:237 BW) staan?
- Zijn de precontractuele informatieplichten nageleefd (bij consumenten: art. 6:230m BW; oneerlijke handelspraktijken: art. 6:193a e.v. BW; bij digitale inhoud en digitale diensten: titel 1AA van Boek 7 BW)?

**Onredelijk bezwarende bedingen:**
- Beoordeel op onaanvaardbare beperking van rechten van de wederpartij (art. 6:233 sub a BW)
- Bij B2C: extra bescherming op grond van dwingend consumentenrecht
- Bij kleine ondernemers en zzp'ers: mogelijke reflexwerking van de zwarte en grijze lijst via de open norm van art. 6:233 sub a BW

### Stap 3 — Kernbepalingen

Beoordeel of alle kernbepalingen aanwezig, volledig en juridisch houdbaar zijn:

| Bepaling | Aanwezig | Opmerkingen |
|---|---|---|
| Toepasselijkheid en aanvaarding | | |
| Aanbod en aanvaarding | | |
| Betalingsvoorwaarden en rente | | |
| Aansprakelijkheidsbeperking | | |
| Overmacht | | |
| Intellectueel eigendom | | |
| Klachten en garantie | | |
| Opzegging en beëindiging | | |
| Geschillenbeslechting en forumkeuze | | |
| Toepasselijk recht | | |
| Wijziging AV | | |
| Privacy / gegevensverwerking | | |

### Stap 4 — Specifieke IT-clausules

Controleer of de volgende IT-specifieke bepalingen aanwezig en toereikend zijn:

- **SLA-verwijzing:** Wordt verwezen naar een aparte SLA of zijn serviceniveaus in de AV opgenomen?
- **Uptime en beschikbaarheid:** Is er een uptime-garantie of disclaimer?
- **Data en beveiliging:** Hoe wordt omgegaan met klantdata? Verwijzing naar verwerkersovereenkomst?
- **Onderhoud en updates:** Kunnen updates eenzijdig worden doorgevoerd? Wat zijn de gevolgen?
- **Gebruiksrecht software:** Wat zijn de grenzen van het gebruiksrecht?
- **Export/back-up data:** Heeft de klant recht op export van zijn eigen data?
- **Beëindiging en datateruggave:** Wat gebeurt er met klantdata bij opzegging?

### Stap 5 — Output: kant-en-klare AV of reviewrapport

**Bij opstellen:** Genereer een complete set algemene voorwaarden op basis van de verstrekte context, met alle bovenstaande bepalingen ingevuld.

**Bij reviewen:** Lever een reviewrapport met:
- Bevindingen per bepaling (aanwezig / ontbreekt / onvoldoende)
- Beoordeling per bevinding conform de ICTRecht-driedeling: 🔴 Kritiek punt (strijd met dwingend recht of ontbrekend kernonderdeel) / 🟠 Risico (vaag, onvolledig of onredelijk) / ⚡ Aandachtspunt (afwijking van best practice)
- Concrete tekstsuggesties voor ontbrekende of zwakke bepalingen
- Een samenvattende tabel (Bepaling | Bevinding | Korte samenvatting)

---

## Output

Sla de output op als:
`~/.claude/plugins/config/ictrecht-contracten/outputs/algemene-voorwaarden-[datum]-[onderwerp].md`

Als opslaan niet mogelijk is, toon de volledige tekst in de chat.

---

Sluit af met de standaard ICTRecht disclaimer.
