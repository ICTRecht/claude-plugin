---
name: vok-review
description: >
  Controleer een verwerkersovereenkomst (VOK) op volledigheid en AVG-conformiteit.
  Gebruik dit als iemand een VOK wil beoordelen, opstellen of controleren voor
  een leverancier of klant.
argument-hint: "[VOK document of naam leverancier]"
---

# /ictrecht-privacy:vok-review

Beoordeel een verwerkersovereenkomst conform AVG artikel 28.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht-privacy/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht Privacy organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Privacy Profiel`
   - Geen van deze beschikbaar → meld: "Organisatieprofiel niet gevonden. Voer eerst `/ictrecht-privacy:cold-start-interview` uit." en stop.
2. Gebruik `search_privacy_guide` voor AVG art. 28 vereisten.
3. Vraag het document op als nog niet gedeeld.

## Checklist AVG artikel 28

Controleer elk verplicht element:

### Verplichte inhoud (art. 28 lid 3)

| Element | Aanwezig? | Opmerking |
|---|---|---|
| Verwerking alleen op instructie | | |
| Geheimhouding medewerkers | | |
| Technische en organisatorische maatregelen (art. 32) | | |
| Toestemming voor inschakelen subverwerkers | | |
| Bijstand bij rechten van betrokkenen | | |
| Bijstand bij beveiliging, datalekken, DPIA | | |
| Verwijdering/teruggave na afloop | | |
| Auditrecht en medewerking | | |
| Informatieplicht subverwerkers | | |

### Aanvullende aandachtspunten

- **Subverwerkers**: Is er een lijst? Is toestemming specifiek of algemeen?
- **Doorgifte buiten EER**: Is dit geregeld? Welke grondslag (SCCs, adequaatheidsbesluit)?
- **Bewaartermijnen**: Zijn die specifiek genoeg?
- **Beveiligingsniveau**: Is art. 32-niveau beschreven of verwezen?

## Beoordeling

Geef per ontbrekend of zwak element:
- **Probleem**: wat ontbreekt of klopt niet
- **Risico**: wat dit betekent voor de organisatie
- **Aanbeveling**: hoe het te herstellen

## Output

Schrijf beoordeling naar `~/.claude/plugins/config/ictrecht-privacy/outputs/vok-review-[datum]-[leverancier].md`.
Als dat pad niet beschikbaar is, toon de volledige beoordeling in de chat.

Sluit af met de standaard ICTRecht disclaimer.
