---
name: dma-analyse
description: >
  Analyseer DMA-verplichtingen voor poortwachters of bedrijven die met poortwachters werken.
argument-hint: "[organisatie of platform]"
---

## Metadata
- **name:** dma-analyse
- **description:** Analyseer DMA-verplichtingen voor poortwachters of bedrijven die met poortwachters werken.
- **argument-hint:** "[organisatie of platform]"

## Voorbereiding (3-laags)

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-compliance-officer:cold-start-interview` uit voor gepersonaliseerde analyse. Nu wordt generieke DMA-analyse toegepast.*

Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `PLACEHOLDER_COLLECTION_ID`
   <!-- Nog geen kennisbank-backend beschikbaar voor dit domein --> om je analyse te gronden
   in actuele ICTRecht-bronnen, naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

## Instructies

Voer de volgende stappen uit voor de opgegeven organisatie of het platform:

### Stap 1 — Is de organisatie een poortwachter? (art. 3 DMA)

**Kwantitatieve drempelwaarden (vermoeden van poortwachtersstatus):**
- Jaaromzet in de EER ≥ €7,5 miljard in elk van de laatste 3 jaar, OF marktkapitalisatie ≥ €75 miljard
- Kernplatformdienst heeft ≥ 45 miljoen maandelijkse eindgebruikers in de EU
- Kernplatformdienst heeft ≥ 10.000 jaarlijkse zakelijke gebruikers in de EU

**Kernplatformdiensten waarop DMA van toepassing is:**
- Online bemiddelingsdiensten (marktplaatsen, app stores)
- Online zoekmachines
- Online sociale netwerken
- Video-sharing platforms
- Nummeronafhankelijke interpersoonlijke communicatiediensten (messaging)
- Besturingssystemen
- Webbrowsers
- Virtuele assistenten
- Cloud computing diensten
- Online advertentiediensten

**Aangewezen poortwachters:** Alphabet, Amazon, Apple, Booking, ByteDance, Meta, Microsoft — controleer de actuele lijst van de Europese Commissie.

**Conclusie:**
- Poortwachter: ga naar Stap 2
- Niet aangewezen maar drempelwaarden genaderd: meld meldingsplicht (art. 3 lid 3)
- Geen poortwachter maar werkt met poortwachters: ga naar Stap 3

### Stap 2 — Poortwachterverplichtingen (art. 5 en 6 DMA)

**Art. 5 — Verplichtingen (direct afdwingbaar):**

| Verplichting | Omschrijving |
|---|---|
| Geen combinatie persoonsgegevens | Geen kruislingse datakoppeling kernplatformdiensten zonder toestemming |
| Geen opt-out blokkeren | Zakelijke gebruikers mogen hun diensten ook buiten het platform aanbieden |
| Geen meest-begunstigde-natieclausule | Geen verbod op lagere prijzen op andere platforms |
| App-vrijheid | Geen verplichte installatie standaard apps; sideloading toestaan |
| Interoperabiliteit messaging | Derde partijen moeten kunnen koppelen aan messaging diensten |
| Advertentietransparantie | Adverteerders toegang geven tot prestatiedata |

**Art. 6 — Verplichtingen (nader te specificeren):**

| Verplichting | Omschrijving |
|---|---|
| Geen zelfbevoordeling | Eigen diensten/producten niet hoger ranken dan vergelijkbare derde aanbieders |
| Data-toegang zakelijke gebruikers | Gegenereerde data beschikbaar stellen aan zakelijke gebruikers |
| Portabiliteit eindgebruikersdata | Effectieve dataportabiliteit voor eindgebruikers |
| Toegang app stores | Eerlijke en niet-discriminerende toegangsvoorwaarden |
| Zoekrangschikking | Transparantie over rankingcriteria |
| Bundeling verbod | Geen verplichte koppeling niet-kernplatformdiensten |

### Stap 3 — Rechten van bedrijven die met poortwachters werken (art. 6)
Als zakelijke gebruiker van een poortwachter:
- Recht op data die je zelf genereerde op het platform
- Recht om eigen producten/diensten buiten het platform aan te bieden
- Recht op eerlijke en niet-discriminerende toegang
- Recht op transparantie over ranking en promotie
- Mogelijkheid tot klacht bij Europese Commissie

### Stap 4 — Handhaving en remedies
- **Europese Commissie** is exclusief bevoegd voor handhaving DMA
- **Nationale mededingingsautoriteiten** kunnen onderzoek instellen en doorverwijzen
- **Boetes:** tot 10% van wereldwijde jaaromzet; bij recidive 20%; dwangsommen tot 5% dagomzet
- **Systeemschendingen:** bij herhaalde ernstige schendingen kan Commissie gedragsremedies opleggen (ook structureel: desinvestering)
- **Marktonderzoek:** Commissie kan nieuwe poortwachters aanwijzen of nieuwe verplichtingen opleggen

### Stap 5 — Impact op businessmodel en advies
Analyseer:
1. Directe impact van DMA-verplichtingen op het businessmodel
2. Kansen: welke rechten heeft de organisatie als zakelijke gebruiker?
3. Risico's: compliance-lacunes en handhavingsrisico
4. Aanbevelingen voor DMA-compliance of rechtspositie verbetering

### Output
Sla de DMA-analyse op naar `~/.claude/plugins/config/ictrecht-compliance-officer/outputs/dma-analyse-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
