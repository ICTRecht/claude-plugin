---
name: dpia
description: >
  Voer een Data Protection Impact Assessment (DPIA) uit voor een nieuwe verwerking,
  product of functionaliteit. Gebruik dit als iemand vraagt om een DPIA, PIA,
  gegevensbeschermingseffectbeoordeling, of een nieuwe verwerking wil beoordelen.
argument-hint: "[omschrijving van de verwerking of productfunctionaliteit]"
---

# /ictrecht-privacy-officer:dpia

Voer een gestructureerde DPIA uit conform AVG artikel 35.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-privacy-officer:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Controleer `~/.claude/plugins/config/ictrecht-privacy-officer/outputs/` op eerdere DPIA's voor dezelfde verwerking (alleen als dat pad beschikbaar is).
3. Gebruik je kennis van DPIA-methodiek (AVG art. 35, AP-richtlijnen voor verplichte DPIA's).
4. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `6ea95c7b-0e2c-4efd-ac84-bd7a96fc9356`
   (DPIA Assistent) om je analyse te gronden in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

## Stap 1 — Is een DPIA verplicht?

Beoordeel of een DPIA verplicht is op grond van:
- AVG artikel 35 (waarschijnlijk hoog risico)
- AP-lijst verplichte DPIA's (raadpleeg je kennis van de AP-richtlijnen)
- Interne drempel van de organisatie (uit CLAUDE.md)

Meld expliciet: "DPIA verplicht" / "DPIA aanbevolen" / "DPIA niet vereist, wel gedocumenteerd".

## Stap 2 — Verwerkingsbeschrijving

Stel de volgende vragen als ze niet al zijn opgegeven:

1. Wat is het doel van de verwerking?
2. Welke categorieën persoonsgegevens worden verwerkt?
3. Van wie worden de gegevens verwerkt (betrokkenen)?
4. Wie zijn de ontvangers of verwerkers?
5. Worden gegevens doorgegeven buiten de EER?
6. Wat zijn de bewaartermijnen?
7. Welke technische en organisatorische maatregelen zijn voorzien?

## Stap 3 — Noodzakelijkheid en evenredigheid

Gebruik je kennis van AVG art. 5 en art. 6 voor:
- Verwerkingsgrondslag (art. 6 AVG)
- Doelbinding (art. 5 lid 1 sub b)
- Dataminimalisatie (art. 5 lid 1 sub c)
- Proportionaliteit

## Stap 4 — Risicoanalyse

Identificeer risico's voor betrokkenen op basis van AVG art. 35 en AP-risicocategorieën.

Voor elk risico:
| Risico | Kans | Impact | Bruto risico | Maatregel | Netto risico |
|---|---|---|---|---|---|

Schaal: Laag / Gemiddeld / Hoog

## Stap 5 — Maatregelen en conclusie

- Lijst technische maatregelen
- Lijst organisatorische maatregelen
- Conclusie: restrisico aanvaardbaar / raadpleging AP vereist (art. 36 AVG)

## Stap 6 — Output

Schrijf het DPIA-rapport naar `~/.claude/plugins/config/ictrecht-privacy-officer/outputs/dpia-[datum]-[verwerking].md`.
Als dat pad niet beschikbaar is, toon het volledige rapport in de chat.

Sluit af met de standaard ICTRecht disclaimer.
