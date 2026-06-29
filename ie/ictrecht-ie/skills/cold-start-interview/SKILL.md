---
name: cold-start-interview
description: >
  Richt de ICTRecht IE plugin in voor jouw organisatie. Stel dit eenmalig in — alle andere commando's zijn ervan afhankelijk.
argument-hint: ""
---

## Configuratie

- **Config pad:** `~/.claude/plugins/config/ictrecht-ie/`
- **Memory label:** "ICTRecht IE organisatieprofiel"
- **Prefix:** `/ictrecht-ie:`

---

## Voorbereiding (3-laags)

1. Lees `~/.claude/plugins/config/ictrecht-ie/CLAUDE.md` — gebruik dat profiel als het bestaat en geen [PLACEHOLDER] bevat.
2. Zoek anders in geheugen naar "ICTRecht IE organisatieprofiel".
3. Geen van beide beschikbaar: ga generiek verder en vermeld ℹ️ dat het profiel nog niet is ingevuld.

---

## Workflow

Stel de volgende vragen één voor één (wacht op antwoord per vraag):

**Stap 1 — Organisatie & sector**
"Wat is de naam van uw organisatie en in welke sector bent u actief?"

**Stap 2 — Type IE-rechten**
"Welk type intellectueel eigendom is voor u het meest relevant? (bijv. software, content/creatieve werken, merken, octrooien, bedrijfsgeheimen — meerdere antwoorden mogelijk)"

**Stap 3 — Actieve markten en landen**
"In welke landen of markten bent u actief? (relevant voor beschermingsomvang merkenrecht en toepasselijk recht)"

**Stap 4 — IE-portefeuille**
"Heeft u geregistreerde merken, domeinnamen, octrooien of andere geregistreerde IE-rechten? Zo ja, welke?"

**Stap 5 — Rol gebruiker**
"Wat is uw rol binnen de organisatie? (bijv. IE-jurist, product manager, marketeer, developer, management)"

**Stap 6 — Juridisch contactpersoon**
"Wie is het juridisch aanspreekpunt binnen uw organisatie voor IE-zaken?"

---

## Opslaan (standaard 3-save patroon)

Na het verzamelen van alle antwoorden:

1. **Sla op in geheugen** als "ICTRecht IE organisatieprofiel" met de ingevulde gegevens.
2. **Schrijf naar bestand** `~/.claude/plugins/config/ictrecht-ie/CLAUDE.md` — vervang alle [PLACEHOLDER]-velden met de verkregen antwoorden. Behoud de volledige structuur van het template.
3. **Bevestig aan de gebruiker** dat het profiel is opgeslagen en dat toekomstige skills dit profiel automatisch gebruiken. Vermeld het pad `~/.claude/plugins/config/ictrecht-ie/CLAUDE.md`.

---

## Afsluiting

Sluit af met de standaard ICTRecht disclaimer.
