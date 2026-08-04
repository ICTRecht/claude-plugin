---
name: dsa-verplichtingen
description: >
  Bepaal DSA-verplichtingen voor een online platform of tussenpersoon.
argument-hint: "[platform of dienst]"
---

## Metadata
- **name:** dsa-verplichtingen
- **description:** Bepaal DSA-verplichtingen voor een online platform of tussenpersoon.
- **argument-hint:** "[platform of dienst]"

## Voorbereiding (3-laags)

1. **Config-bestand:** Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` voor organisatiecontext.
2. **Memory:** Zoek naar memory met label "ICTRecht organisatieprofiel".
3. **Project instructions:** Zoek naar sectie `## ICTRecht Profiel` in de projectinstructies.

Geen van de drie beschikbaar: ga door generiek en toon:
> ℹ️ *Geen organisatieprofiel gevonden. Voer `/ictrecht-compliance-officer:cold-start-interview` uit voor gepersonaliseerde analyse. Nu worden generieke DSA-verplichtingen bepaald.*

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

Voer de volgende stappen uit voor het opgegeven platform of de opgegeven dienst:

### Stap 1 — Kwalificatie (art. 2 DSA)
Bepaal het type tussenpersoon:

| Type | Omschrijving | Voorbeeld |
|---|---|---|
| **Mere conduit** | Doorgifte van informatie, geen opslag | ISP, telecomoperator |
| **Caching** | Tijdelijke automatische opslag | CDN, proxy |
| **Hosting** | Opslag van door gebruikers verstrekte informatie | Webhosting, cloud opslag |
| **Online platform** | Hosting + verspreiding aan publiek | Sociale media, marktplaats, app store |
| **VLOP** | Online platform met ≥45M maandelijkse gebruikers in EU | Facebook, TikTok, Amazon Marketplace |
| **VLOSE** | Online zoekmachine met ≥45M maandelijkse gebruikers in EU | Google Search, Bing |

**Conclusie:** Welk type is de dienst? (meerdere lagen mogelijk)

### Stap 2 — Basisverplichtingen alle tussenpersonen (art. 11-15)
Van toepassing op alle categorieën:

| Verplichting | Artikel | Status |
|---|---|---|
| Aanwijzen contactpunt voor autoriteiten | Art. 11 | |
| Aanwijzen contactpunt voor afnemers van de dienst | Art. 12 | |
| Aanwijzen wettelijk vertegenwoordiger in EU (indien buiten EU) | Art. 13 | |
| Transparantierapportage | Art. 15 | |
| Samenwerking met toezichthoudende autoriteiten | Art. 11 | |
| Algemene gebruiksvoorwaarden (helder, begrijpelijk) | Art. 14 | |

### Stap 3 — Hostingprovider verplichtingen
Extra bij hosting (inclusief online platforms):

| Verplichting | Artikel | Status |
|---|---|---|
| Notice-and-action mechanisme (meldingen illegale inhoud) | Art. 16 | |
| Verwerking meldingen tijdig en zorgvuldig | Art. 17 | |
| Motivering bij verwijdering of beperking | Art. 17 | |
| Waarschuwing bij misbruik (repeterend misbruik) | Art. 23 | |

### Stap 4 — Online platform verplichtingen (art. 20-28)
Extra bij online platforms:

| Verplichting | Artikel | Status |
|---|---|---|
| Intern klachtenbehandelingssysteem | Art. 20 | |
| Buitengerechtelijke geschillenbeslechting | Art. 21 | |
| Vertrouwde melders (trusted flaggers) erkennen | Art. 22 | |
| Transparantie over reclame (duidelijk gelabeld) | Art. 26 | |
| Verbod op targeting minderjarigen voor reclame | Art. 28 | |
| Verbod op targeting op basis van gevoelige gegevens | Art. 26 | |
| Transparantie aanbevelingssystemen | Art. 27 | |
| Verbod op dark patterns | Art. 25 | |
| Online marktplaatsen: traceerbaarheid handelaren | Art. 30 | |

**Uitzondering micro- en kleine ondernemingen (art. 19 en 29):** de meeste platformverplichtingen (art. 20-28) gelden niet voor micro- en kleine ondernemingen, tenzij het platform is aangewezen als VLOP.

### Stap 5 — VLOP/VLOSE extra verplichtingen
Bij aanwijzing als Very Large Online Platform of Search Engine:

| Verplichting | Artikel | Status |
|---|---|---|
| Systeemrisicoanalyse (jaarlijks) | Art. 34 | |
| Risicobeperkende maatregelen | Art. 35 | |
| Onafhankelijke audit (jaarlijks) | Art. 37 | |
| Data-toegang voor onderzoekers | Art. 40 | |
| Crisisprotocol | Art. 48 | |
| Aanbevelingssysteem zonder profiling optie | Art. 38 | |
| Verhoogde transparantie reclame-archief | Art. 39 | |
| Toezicht door Europese Commissie | Art. 33 | |

### Stap 6 — Actieplan
Overzicht van:
1. Verplichtingen die direct gelden
2. Verplichtingen die nog niet zijn geïmplementeerd
3. Prioritering op basis van handhavingsrisico (boetes tot 6% wereldwijde jaaromzet; in Nederland is de ACM digitaledienstencoördinator en handhaaft de AP de bepalingen over profilering)
4. Aanbevolen volgorde van implementatie

### Output
Sla de DSA-analyse op naar `~/.claude/plugins/config/ictrecht-compliance-officer/outputs/dsa-verplichtingen-[datum].md`.

---

Sluit af met de standaard ICTRecht disclaimer.
