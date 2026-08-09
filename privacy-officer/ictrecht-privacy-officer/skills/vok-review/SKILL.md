---
name: vok-review
description: >
  Controleer een verwerkersovereenkomst (VOK) op volledigheid en AVG-conformiteit.
  Gebruik dit als iemand een VOK wil beoordelen, opstellen of controleren voor
  een leverancier of klant.
argument-hint: "[VOK document of naam leverancier]"
---

# /ictrecht-privacy-officer:vok-review

Beoordeel een verwerkersovereenkomst conform AVG artikel 28.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy-officer:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Gebruik je kennis van AVG art. 28 vereisten voor verwerkersovereenkomsten.
3. Vraag het document op als nog niet gedeeld en voer de analyse pas uit zodra de volledige tekst beschikbaar is.
4. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `b1c44172-86ba-4504-8b1a-6c58c8ea9120`
   (Privacy Guide V2) om je analyse te gronden in actuele ICTRecht-bronnen, naast je eigen
   kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

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
- 🟡 **Aandachtspunt** — afwijking van best practice; verbetering aanbevolen

Geef per bevinding:
- **Beoordeling**: 🔴 / 🟠 / 🟡
- **Probleem**: wat ontbreekt of klopt niet
- **Risico**: wat dit betekent voor de organisatie
- **Aanbeveling**: hoe het te herstellen

Sluit af met een samenvattende tabel (Onderdeel | Bevinding | Korte samenvatting). Toon alleen onderdelen met een bevinding.

## Output

Schrijf beoordeling naar `~/.claude/plugins/config/ictrecht-privacy-officer/outputs/vok-review-[datum]-[leverancier].md`.
Als dat pad niet beschikbaar is, toon de volledige beoordeling in de chat.

Sluit af met de standaard ICTRecht disclaimer.
