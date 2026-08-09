---
name: datalek-toets
description: >
  Geef als FG een oordeel over een (mogelijk) datalek en de door de organisatie
  genomen of voorgenomen melding, conform AVG artikel 39. Gebruik dit als de FG
  wordt geraadpleegd over een beveiligingsincident, of als een gedane melding
  achteraf getoetst moet worden.
argument-hint: "[omschrijving van het incident of de gedane melding]"
---

# /ictrecht-fg:datalek-toets

Beoordeel als FG een datalek en de afhandeling daarvan conform AVG artikel 33, 34 en 39.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Controleer op eerdere beoordelingen van hetzelfde incident (alleen als outputs-pad beschikbaar is).
3. Gebruik je kennis van datalekwetgeving (AVG art. 33/34, AP-beleidsregels meldplicht).
4. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

**Rolkader:** de melding bij de AP en aan betrokkenen wordt gedaan door de
verwerkingsverantwoordelijke, niet door de FG (art. 33/34 AVG). De FG toetst of dat correct
gebeurt en fungeert als eerste aanspreekpunt voor de toezichthouder over het incident (art.
39 lid 1 sub e). De FG heeft geen corrigerende bevoegdheid — als de organisatie het
FG-oordeel niet volgt, kaart de FG dit aan bij de hoogste leidinggevende (art. 38 lid 3) in
plaats van het besluit zelf te overrulen.

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `e89f6432-124c-421f-ac93-6b83c3ce37b4`
   (Beoordelingsassistent Datalekken) om je oordeel te gronden in actuele ICTRecht-bronnen,
   naast je eigen kennis.
3. **Niet beschikbaar:** ga gewoon door met je eigen juridische kennis. Vermeld dit NIET
   als fout, waarschuwing of gemis — geen connector is een volwaardige, ondersteunde manier
   om deze skill te gebruiken.

## Stap 1 — Is er sprake van een datalek?

Stel vast of het incident valt onder de definitie (AVG art. 4 lid 12):
"Een inbreuk op de beveiliging die leidt tot vernietiging, verlies, wijziging of ongeoorloofde verstrekking van persoonsgegevens."

Vraag als niet duidelijk:
- Wat is er precies gebeurd?
- Welke persoonsgegevens zijn betrokken?
- Zijn de gegevens ingezien, gelekt of verloren?

Oordeel: **Datalek: ja / nee / waarschijnlijk**

## Stap 2 — Risicobeoordeling voor betrokkenen

Beoordeel op basis van AVG art. 33/34 en AP-risicocriteria.

Beoordeel:
- Aard van de gegevens (gewoon / bijzonder / strafrechtelijk)
- Omvang (aantal betrokkenen)
- Gevolgen (identiteitsfraude / discriminatie / reputatieschade / financieel)
- Herstelbaarheid

Risicoclassificatie: **Geen risico / Beperkt risico / Hoog risico**

## Stap 3 — Toets meldplicht AP (art. 33 AVG)

Meldplicht bij de AP als:
- Er sprake is van een datalek (stap 1 = ja), EN
- Het niet onwaarschijnlijk is dat de inbreuk een risico inhoudt voor de rechten en vrijheden van betrokkenen (art. 33 lid 1 AVG: melden, tenzij dat risico onwaarschijnlijk is)

**Termijn: 72 uur nadat de organisatie er kennis van heeft genomen.** Is die termijn al verstreken of dreigt dat te gebeuren? Signaleer dit expliciet — een late melding moet gemotiveerd worden (art. 33 lid 1).

Oordeel: **AP-melding verplicht / niet verplicht / aanbevolen** — en of de organisatie hier (tijdig) aan voldoet of heeft voldaan.

## Stap 4 — Toets melding aan betrokkenen (art. 34 AVG)

Verplicht bij hoog risico, met twee wettelijke uitzonderingen (art. 34 lid 3 AVG) die de meldplicht wegnemen ondanks een hoog-risico-inschatting:
- De getroffen gegevens waren versleuteld of anderszins onbegrijpelijk voor onbevoegden.
- De gevolgen zijn direct na het incident tot nul gereduceerd.

Toets of de organisatie deze uitzonderingen terecht heeft toegepast (of ten onrechte niet heeft overwogen). Bij twijfel of een maatregel de gevolgen daadwerkelijk tot nul reduceert: geen uitzondering aannemen.

Oordeel: **Melding betrokkenen verplicht / niet verplicht (uitzondering: [encryptie / gevolgen genomen tot nul])**

## Stap 5 — FG-oordeel en aanbeveling

Vat samen:
- **Oordeel over de afhandeling**: is de kwalificatie, meldplicht-inschatting en termijn correct toegepast?
- **Openstaande punten**: wat moet de organisatie nog doen of alsnog motiveren?
- **Als de organisatie afwijkt van het FG-oordeel**: kaart dit aan bij de hoogste leidinggevende (art. 38 lid 3) — de FG legt dit niet zelf op.

## Stap 6 — Output

Schrijf het FG-oordeel naar `~/.claude/plugins/config/ictrecht-fg/outputs/datalek-toets-[datum]-[incident].md`.
Als dat pad niet beschikbaar is, toon het volledige oordeel in de chat.

Sluit af met de standaard ICTRecht disclaimer.
