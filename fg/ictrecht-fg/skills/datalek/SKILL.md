---
name: datalek
description: >
  Beoordeel een (mogelijk) datalek en bepaal of melding bij de AP en/of betrokkenen
  verplicht is. Gebruik dit als iemand een beveiligingsincident meldt, vraagt of
  iets een datalek is, of wil weten wat de meldplicht inhoudt.
argument-hint: "[omschrijving van het incident]"
---

# /ictrecht-fg:datalek

Beoordeel een datalek conform AVG artikel 33 en 34.

## Voorbereiding

1. **Organisatiecontext laden** — probeer in volgorde:
   - Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md`
   - Of zoek in geheugen naar "ICTRecht organisatieprofiel"
   - Of zoek in projectinstructies naar het blok `## ICTRecht Profiel`
   - Geen van deze beschikbaar → ga door met generieke AVG-standaardinstellingen en vermeld bovenaan de output: "ℹ️ Geen organisatieprofiel gevonden — output is generiek. Voer `/ictrecht-fg:cold-start-interview` uit voor gepersonaliseerde analyses."
2. Controleer op eerdere beoordelingen van hetzelfde incident (alleen als outputs-pad beschikbaar is).
3. Gebruik je kennis van datalekwetgeving (AVG art. 33/34, AP-beleidsregels meldplicht).
4. Volg voor toon, structuur en opmaak de schrijfwijzer in deze plugin (`SCHRIJFWIJZER.md` in de plugin-root).

## Connector (optioneel)

Deze skill kan gebruikmaken van de **ictrecht-knowledge-server**-connector voor actuele
ICTRecht-kennisbanken. Dit is volledig optioneel — de gebruiker voegt de connector zelf
toe (via Claude Desktop Settings → Connectors, of `claude mcp add` in Claude Code) als hij
dat wil. Deze skill werkt identiek goed met of zonder.

1. Check of er een MCP-tool beschikbaar is die bij de `ictrecht-knowledge-server`-
   connector hoort (bijv. een tool genaamd `search_knowledge`, `search_<naam>` of
   vergelijkbaar, aangeboden door een MCP-server met 'ictrecht' in de naam of omschrijving).
2. **Wel beschikbaar:** gebruik de tool met kennisbank-ID `e89f6432-124c-421f-ac93-6b83c3ce37b4`
   (Beoordelingsassistent Datalekken) om je analyse te gronden in actuele ICTRecht-bronnen,
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

## Stap 3 — Meldplicht AP (art. 33 AVG)

Meldplicht bij de AP als:
- Er sprake is van een datalek (stap 1 = ja), EN
- Het niet onwaarschijnlijk is dat de inbreuk een risico inhoudt voor de rechten en vrijheden van betrokkenen (art. 33 lid 1 AVG: melden, tenzij dat risico onwaarschijnlijk is)

**Termijn: 72 uur nadat de organisatie er kennis van heeft genomen.** Een latere melding moet gemotiveerd worden (art. 33 lid 1).

Zijn de feiten nog niet compleet? Doe dan een voorlopige melding via het AP-meldloket datalekken; die kan later worden aangevuld of ingetrokken. Bij twijfel is melden verstandiger dan afwachten.

Oordeel: **AP-melding verplicht / niet verplicht / aanbevolen**

## Stap 4 — Melding aan betrokkenen (art. 34 AVG)

Verplicht bij hoog risico. Beoordeel op basis van AVG art. 34 drempelcriteria.

Oordeel: **Melding betrokkenen verplicht / niet verplicht**

## Stap 5 — Documentatieplicht (art. 33 lid 5 AVG)

Altijd documenteren, ook als geen melding vereist is.

## Stap 6 — Actielijst

Geef een genummerde actielijst:
1. Incident beëindigen / schade beperken
2. [AP melden voor [datum]] of [niet vereist]
3. [Betrokkenen informeren] of [niet vereist]
4. Documenteren in datalekregister
5. Nazorg en preventieve maatregelen

## Stap 7 — Output

Schrijf beoordeling naar `~/.claude/plugins/config/ictrecht-fg/outputs/datalek-[datum]-[incident].md`.
Als dat pad niet beschikbaar is, toon de volledige beoordeling in de chat.

Sluit af met de standaard ICTRecht disclaimer.
