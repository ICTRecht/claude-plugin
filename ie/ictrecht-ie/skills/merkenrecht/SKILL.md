---
name: merkenrecht
description: >
  Analyseer merkenrechtelijke vragen over bescherming, inbreuk, registratie en conflict.
argument-hint: "[merk of situatie]"
---

## Voorbereiding (3-laags)

1. Lees `~/.claude/plugins/config/ictrecht/CLAUDE.md` — gebruik organisatieprofiel als het bestaat en geen [PLACEHOLDER] bevat.
2. Zoek anders in geheugen naar "ICTRecht organisatieprofiel".
3. Zoek anders in projectinstructies naar het blok `## ICTRecht Profiel`.
4. Geen van deze beschikbaar: ga generiek verder en vermeld ℹ️ dat het profiel nog niet is ingevuld; adviseer `/ictrecht-ie:cold-start-interview` uit te voeren.

---

## Workflow

**Stap 1 — Is het teken beschermbaar als merk?**
Beoordeel onderscheidend vermogen (sterk/zwak/beschrijvend). Toets absolute weigeringsgronden (art. 2.1 BVIE / art. 7 UMVo): beschrijvend, gebruikelijk, gebrek aan onderscheidend vermogen, misleidend, openbare orde.

**Stap 2 — Waar is het merk geregistreerd?**
Stel vast welk register van toepassing is:
- Benelux (BOIP / BBIE)
- Europese Unie (EUIPO — Uniemerk)
- Internationaal (WIPO Madrid-systeem)
Bespreek territorial scope en prioriteitsrechten.

**Stap 3 — Beschermingsomvang**
Analyseer de beschermingsomvang: waren en diensten (Nice-classificatie), soortgelijkheid, gevaar voor verwarring (Global appreciation-test: visuele, auditieve en begripsmatige overeenstemming). Bekendheid als verzwaarde bescherming.

**Stap 4 — Inbreukanalyse**
Beoordeel gebruik in het economisch verkeer (art. 2.20 lid 2 BVIE). Toets overeenstemming teken vs. merk en soortgelijkheid waren/diensten. Weeg verwarringsgevaar of ongerechtvaardigd voordeel/afbreuk aan bekendheid.

**Stap 5 — Opties**
Bespreek beschikbare acties:
- Sommatie / cease-and-desist
- Oppositieprocedure bij BOIP/EUIPO
- Nietigheidsvordering
- Inbreukprocedure (kort geding / bodemprocedure)
- Douane-actie (verordening 608/2013)

**Stap 6 — Merkenstrategie**
Geef strategisch advies: registratie aanbevelen, klassen uitbreiden, bewijs van gebruik, monitoring, licentie- of co-existentieovereenkomst.

---

## Output

Sla uitgewerkte analyses op in `~/.claude/plugins/config/ictrecht-ie/outputs/` indien de gebruiker dit verzoekt.

Sluit af met de standaard ICTRecht disclaimer.
