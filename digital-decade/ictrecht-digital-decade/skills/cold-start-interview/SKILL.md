---
name: cold-start-interview
description: >
  Richt de ICTRecht Digital Decade plugin in voor jouw organisatie. Stel dit eenmalig in — alle andere commando's zijn ervan afhankelijk.
argument-hint: ""
---

## Configuratie
- **Config pad:** `~/.claude/plugins/config/ictrecht-digital-decade/CLAUDE.md`
- **Memory label:** "ICTRecht Digital Decade organisatieprofiel"
- **Prefix:** `/ictrecht-digital-decade:`

## Doel

Verzamel de essentiële organisatie-informatie om alle Digital Decade skills te personaliseren. Na afloop wordt het profiel opgeslagen zodat volgende skills automatisch de juiste context hebben.

## Instructies

### Voorbereiding
1. Controleer of `~/.claude/plugins/config/ictrecht-digital-decade/CLAUDE.md` al bestaat en ingevuld is (geen [PLACEHOLDER] meer).
2. Bestaat het en is het ingevuld: vraag of de gebruiker het profiel wil bijwerken of doorgaan met het bestaande.
3. Bestaat het niet of bevat het [PLACEHOLDER]: start het interview.

### Interview — stel de volgende vragen (één voor één, conversationeel)

1. **Organisatie & sector**
   Wat is de naam van je organisatie en in welke sector ben je actief? (bijv. tech, financiën, zorg, overheid, retail, industrie)

2. **Type organisatie**
   Hoe zou je je organisatie het best omschrijven?
   - Online platform of marktplaats
   - Producent van hardware/software/connected products
   - Dienstverlener (B2B of B2C)
   - Overheid of publieke instelling
   - Kritieke infrastructuur (energie, water, transport, gezondheidszorg)
   - Anders

3. **EU-markten**
   In welke EU-lidstaten ben je actief of ben je van plan actief te worden?

4. **Relevante producten en diensten**
   Welke producten of diensten zijn het meest relevant voor Digital Decade compliance? Denk aan:
   - AI-systemen of AI-ondersteunde producten
   - Online platforms of digitale marktplaatsen
   - Connected products (IoT, smart devices)
   - Digitale identiteitsdiensten
   - Netwerk- en informatiesystemen

5. **Huidige compliance status**
   Welke EU digitale verordeningen heb je al geïmplementeerd of ben je mee bezig? (AI Act, NIS2, DSA, DMA, eIDAS 2.0, Cyber Resilience Act — of nog niets gestart)

6. **Rol van de gebruiker**
   Wat is jouw rol binnen de organisatie?
   (bijv. compliance officer, jurist, CTO, product manager, directie/bestuur)

### Na het interview — sla op (3-save patroon)

**Stap 1 — Schrijf config-bestand:**
Schrijf het ingevulde profiel naar `~/.claude/plugins/config/ictrecht-digital-decade/CLAUDE.md` door alle [PLACEHOLDER] waarden te vervangen met de verzamelde antwoorden.

**Stap 2 — Sla op in memory:**
Sla een samenvatting op als memory met label "ICTRecht Digital Decade organisatieprofiel":
```
Organisatie: [naam], Sector: [sector], Type: [type], EU-markten: [landen], Producten/diensten: [lijst], Compliance status: [status], Rol gebruiker: [rol]
```

**Stap 3 — Bevestig aan gebruiker:**
Geef een overzicht van het opgeslagen profiel en meld welke skills nu beschikbaar zijn:
- `/ictrecht-digital-decade:ai-act-classificatie`
- `/ictrecht-digital-decade:nis2-check`
- `/ictrecht-digital-decade:dsa-verplichtingen`
- `/ictrecht-digital-decade:dma-analyse`
- `/ictrecht-digital-decade:cyberweerbaarheid-act`
- `/ictrecht-digital-decade:regulering-scan`

---

Sluit af met de standaard ICTRecht disclaimer.
