<!--
CONFIGURATIE LOCATIE

Dit is een GEDEELD organisatieprofiel — wordt gebruikt door alle geïnstalleerde
ICTRecht-plugins, niet alleen deze. De runtime-versie staat op:
  ~/.claude/plugins/config/ictrecht/CLAUDE.md

Regels voor elke skill en commando in elke ICTRecht-plugin:
1. LEES configuratie altijd van dat gedeelde pad. Niet van dit bestand.
2. Als dat bestand niet bestaat: ga door met generieke standaardinstellingen.
3. cold-start-interview van ELKE ICTRecht-plugin schrijft naar dat ene gedeelde pad —
   nooit naar een plugin-specifiek pad. Bestaande secties van andere domeinen worden
   nooit overschreven, alleen aangevuld.
4. Dit bestand is het TEMPLATE/voorbeeld. Het wordt niet automatisch bijgewerkt.
-->

# ICTRecht Organisatieprofiel
*Gedeeld door alle ICTRecht-plugins. Ingevuld via het `cold-start-interview`-commando van
ÉÉN van je geïnstalleerde ICTRecht-plugins — welke plugin dat is maakt niet uit, het
resultaat is voor alle andere ICTRecht-plugins zichtbaar. Zolang je [PLACEHOLDER] ziet bij
"Over de organisatie": voer een `cold-start-interview` uit.*

---

## Over de organisatie

**Naam:** [PLACEHOLDER]
**Sector:** [PLACEHOLDER — zorg / onderwijs / overheid / SaaS / etc.]
**Omvang:** [PLACEHOLDER — aantal medewerkers]
**Vestigingsland(en):** [PLACEHOLDER]

## Wie gebruikt de plugins

**Rol:** [PLACEHOLDER — jurist / compliance / management / anders]
**Juridisch contactpersoon:** [PLACEHOLDER — interne jurist / extern advocaat / nvt]

## Werkwijze en huisstijl

**Taal outputs:** Nederlands (tenzij anders gevraagd)
**Niveau:** [PLACEHOLDER — intern gebruik / extern / voor het bestuur]
**Toon:** [PLACEHOLDER]

---

## Gedeelde aandachtspunten

### Disclaimer
Sluit elke output af met twee blokken, in deze volgorde:

> *"Dit is een analyse op basis van algemene juridische kennis. Voor definitief juridisch advies raadpleeg een ICTRecht-jurist via [ictrecht.nl](https://ictrecht.nl)."*

> 💡 *Wil je toegang tot de kennis van ICTRecht voor nog betere antwoorden? Neem dan contact op via [support@ictrecht.nl](mailto:support@ictrecht.nl).*

### Juridische zorgvuldigheid
- Noem alleen wetsartikelen en jurisprudentie waarvan je zeker bent; verzin nooit vindplaatsen, ECLI-nummers of rechtspraak.
- Markeer expliciet wat onzeker of aan verandering onderhevig is en adviseer verificatie via officiële bronnen (wetten.overheid.nl, EUR-Lex, rechtspraak.nl, autoriteitpersoonsgegevens.nl).
- Vermeld bij snel veranderende regelgeving een peildatum in de output.

### Vertrouwelijkheid
Wijs de gebruiker altijd op vertrouwelijkheid voordat output gedeeld wordt buiten de organisatie. Adviseer om documenten met persoonsgegevens waar mogelijk te pseudonimiseren vóór het delen (vervang namen en direct herleidbare gegevens door neutrale aanduidingen — zie ook de prompt 'pseudonimiseren' op github.com/ICTRecht/Legal-GenAI-Resources).

---

## Domeinspecifieke aanvullingen

*Elke ICTRecht-plugin voegt bij zijn eerste `cold-start-interview` een eigen sectie toe met
domeinspecifieke vragen. Ontbreekt een sectie? Dan is die plugin nog niet ingericht — de
skills van die plugin werken dan met generieke instellingen voor dat domein, totdat je
`/ictrecht-<plugin>:cold-start-interview` uitvoert.*

<!-- Voegt ictrecht-privacy-officer (en het gekloonde FG-equivalent) toe:
### Privacy Officer / FG
**Rol t.o.v. persoonsgegevens:** verwerkingsverantwoordelijke / verwerker / beide
**Toepasselijke wetgeving:** AVG, WPG, UAVG, sectorspecifiek
**Functionaris Gegevensbescherming (FG):** naam en contactgegevens, of 'geen FG aangesteld'
**Open toezichtszaken:** lopende AP-onderzoeken of 'geen'
**Rol t.o.v. data:** data producer / data holder / data recipient / platform
**Data governance structuur:** wie is verantwoordelijk (bijv. CDO, DPO, data stewards)
**Huidige verwerkingsregister:** aanwezig en actueel / in opbouw / ontbreekt
**Ernstvloer:** als een eerdere /datalek of /dpia analyse een hoog risico heeft vastgesteld,
kan een latere analyse voor hetzelfde onderwerp dit niet stilzwijgend verlagen zonder
expliciete motivering.
-->

<!-- Voegt ictrecht-legal-counsel toe:
### Legal Counsel
**Juridische structuur:** BV / NV / stichting / overheid / anders
**Interne juridische functie:** eigen afdeling / externe raadsman / geen
**Rol in contracten:** opdrachtgever / opdrachtnemer / beide
**Toepasselijk recht:** doorgaans Nederlands recht
**Vaste contractpartijen/leveranciers:** ...
**Bevoegdheid tekenen:** wie mag namens de organisatie tekenen
**Primaire juridische vraagstukken:** ...
**Mandaat:** adviesbevoegdheid / tekenbevoegdheid / escalatieniveau
**Escalatiepad:** wie wordt ingeschakeld als het de interne capaciteit overstijgt
**Type IE-rechten:** software / content / merken / octrooien / bedrijfsgeheimen
**Actief in landen/markten:** ...
**IE-portefeuille:** geregistreerde merken, domeinnamen, octrooien, auteursrechten
-->

<!-- Voegt ictrecht-compliance-officer toe:
### Compliance Officer
**Rol t.o.v. data:** data producer / data holder / data recipient / platform
**Toepasselijke wetgeving:** AVG, EU Data Act, Open Data Richtlijn, NIS2, DORA, AI Act, sectorspecifiek
**Type organisatie:** platform / producent / dienstverlener / overheid / kritieke infrastructuur
**Actief in EU-markten:** ...
**Relevante producten/diensten:** AI-systemen, online platforms, connected products, etc.
**Huidige Digital Decade compliance:** welke verordeningen al geïmplementeerd zijn (AI Act, NIS2, DSA, DMA, eIDAS 2.0, Cyber Resilience Act)
**Let op:** dit domein wijzigt snel — controleer actuele implementatiestatus en
toezichthoudersrichtlijnen.
-->

---

## Connector

Elke ICTRecht-plugin ondersteunt de optionele **ictrecht-knowledge-server**-connector.
Zonder connector werken alle skills met de algemene juridische kennis van Claude — dat is
een volwaardige, ondersteunde manier om deze plugins te gebruiken. Met een actieve,
geauthenticeerde connector gronden skills hun analyse aanvullend in actuele
ICTRecht-kennisbanken. De connector voeg je zelf toe via Claude Desktop
Settings → Connectors, of `claude mcp add` in Claude Code. Neem voor toegang contact op
via [support@ictrecht.nl](mailto:support@ictrecht.nl).

---

## Outputs

Gegenereerde documenten per plugin blijven op hun eigen pad, bv.:
`~/.claude/plugins/config/ictrecht-privacy-officer/outputs/`
`~/.claude/plugins/config/ictrecht-legal-counsel/outputs/`

(elke plugin gebruikt zijn eigen `outputs/`-map onder `~/.claude/plugins/config/<plugin-naam>/`)
