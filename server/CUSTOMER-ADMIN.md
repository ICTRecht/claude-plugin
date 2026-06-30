# Klantbeheer — toevoegen & intrekken vanuit je dashboard

Je dashboard is de **Keycloak-adminconsole**: `https://idp.jouwbedrijf.nl` → realm **`mcp`**.
Hier voeg je klanten toe en trek je toegang in. Geen code, geen herstart.

> Geldt voor klanten die jij beheert (Keycloak-accounts). Klanten die met hun eigen
> Microsoft-organisatie inloggen (Entra) worden door hun eigen IT beheerd — voor die groep
> regel je toegang via Entra of via de RBAC in de gateway.

---

## ➕ Klant toevoegen  (~30 seconden)
1. Console → realm **mcp** → **Users → Add user**.
2. Vul **Email** in (= gebruikersnaam) en zet **Email verified** desgewenst aan → **Create**.
3. Tab **Credentials → Set password** → kies "Temporary" zodat de klant bij eerste login zelf
   een wachtwoord kiest. (Of gebruik **Credential Reset → Send email** voor een instel-link.)
4. Klaar. De klant zit automatisch in de groep **mcp-klanten** en heeft dus toegang.

De klant koppelt vervolgens eenmalig de connector (zie [OAUTH-SETUP.md](OAUTH-SETUP.md) §6):
in Claude/ChatGPT/Copilot Studio → connector toevoegen → **Connect** → **Inloggen met Keycloak**.

---

## ⛔ Toegang intrekken  (direct)
Kies één van de twee — beide werken binnen ~5 min (de access-token-TTL):

**A. Volledig blokkeren (aanrader):**
1. **Users** → open de klant → zet **Enabled** uit → **Save**.
2. Tab **Sessions → Sign out** (of **Users → Sessions** → de klant uitloggen) voor *onmiddellijk* effect.

**B. Alleen kennisbank-toegang weghalen (account blijft bestaan):**
1. **Users** → klant → tab **Groups** → verwijder uit **mcp-klanten**.

Weer toegang geven = **Enabled** aan, of opnieuw aan **mcp-klanten** toevoegen.

---

## Handig
- **Wie heeft toegang?** Console → **Groups → mcp-klanten → Members**.
- **Actieve sessies / wie is ingelogd?** **Sessions** (realm-niveau) of per gebruiker.
- **Wachtwoord vergeten?** De klant kan zelf resetten (self-service staat aan), of jij stuurt
  via **Credential Reset → Send email**.
- **Tijdelijke toegang?** Zet later self-registration of accountverloop aan; vraag me gerust.

> Wil je liever één dashboard zónder Keycloak? De **gateway-admin-UI** (ContextForge) kan ook
> gebruikers/rollen beheren en tokens/sessies intrekken. Keycloak is gekozen omdat het de
> nettste klant-login + selfservice geeft; zeg het als je het in de gateway wilt centraliseren.
