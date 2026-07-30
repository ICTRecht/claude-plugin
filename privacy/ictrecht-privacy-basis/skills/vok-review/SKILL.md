---
name: vok-review
description: >
  Controleer een verwerkersovereenkomst (VOK) op volledigheid en AVG-conformiteit.
  Gebruik dit als iemand een VOK wil beoordelen, opstellen of controleren voor
  een leverancier of klant.
argument-hint: "[VOK document of naam leverancier]"
---

# /ictrecht-privacy-basis:vok-review

Beoordeel een verwerkersovereenkomst conform AVG artikel 28.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy-basis:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik je kennis van AVG art. 28 vereisten voor verwerkersovereenkomsten.
3. Vraag het document op als nog niet gedeeld en voer de analyse pas uit zodra de volledige tekst beschikbaar is.

## Checklist AVG artikel 28

Controleer elk verplicht element:

### Verplichte inhoud (art. 28 lid 3)

| Element | Aanwezig? | Opmerking |
|---|---|---|
| Onderwerp, duur, aard en doel van de verwerking, soort persoonsgegevens en categorieën betrokkenen (art. 28 lid 3, aanhef) | | |
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

Kwalificeer elke bevinding volgens de ICTRecht-driedeling:
- 🔴 **Kritiek punt** — in strijd met dwingende AVG-bepalingen (m.n. art. 28) of een verplicht kernonderdeel ontbreekt
- 🟠 **Risico** — niet direct onrechtmatig, maar vaag, onvolledig of een onredelijk verschoven verantwoordelijkheid
- ⚡ **Aandachtspunt** — afwijking van best practice; verbetering aanbevolen

Geef per bevinding:
- **Beoordeling**: 🔴 / 🟠 / ⚡
- **Probleem**: wat ontbreekt of klopt niet
- **Risico**: wat dit betekent voor de organisatie
- **Aanbeveling**: hoe het te herstellen

Sluit af met een samenvattende tabel (Onderdeel | Bevinding | Korte samenvatting). Toon alleen onderdelen met een bevinding.

## Output

Schrijf beoordeling naar `~/.claude/plugins/config/ictrecht-privacy-basis/outputs/vok-review-[datum]-[leverancier].md`.
Als dat pad niet beschikbaar is, toon de volledige beoordeling in de chat.

Sluit af met de standaard ICTRecht disclaimer.
