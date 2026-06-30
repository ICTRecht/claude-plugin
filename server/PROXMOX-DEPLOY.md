# Proxmox-deploy — runbook

Doel: de OAuth-stack (gateway + Keycloak + eigen MCP-server) betrouwbaar en veilig hosten op
Proxmox VE, bereikbaar voor cloud-AI-clients (Claude/ChatGPT/Copilot Studio).

## ⚠️ Belangrijkste randvoorwaarde
Claude.ai, ChatGPT en Copilot Studio draaien in de **cloud** en moeten je endpoint over
**publiek HTTPS met een vertrouwd certificaat** kunnen bereiken. Dus nodig:
- een **publieke domeinnaam** (`mcp.jouwbedrijf.nl`, `idp.jouwbedrijf.nl`);
- een **trusted TLS-certificaat** (Let's Encrypt) — *self-signed werkt niet* met cloud-clients;
- inkomend **80/443** open naar je reverse proxy.

## Edge = je bestaande nginx (geen Cloudflare)
Je hebt al nginx als reverse proxy op Proxmox; die wordt de edge en termineert TLS. De stack
levert daarom **geen** eigen proxy (die staat op opt-in) en publiceert alleen de gateway en
Keycloak voor jouw nginx:
- `gateway` op `:4444`, `keycloak` op `:8080` — gebonden aan `PUBLISH_BIND` (zie `.env`).
- Draait je nginx op een **andere** VM: zet `PUBLISH_BIND` op het LAN-IP van de stack-VM en
  sta die poorten in de firewall **alleen** toe vanaf de nginx-host. Zelfde host: laat `127.0.0.1`.
- Voeg de twee vhosts toe uit
  [`reverse-proxy/external-nginx.conf.example`](reverse-proxy/external-nginx.conf.example)
  (incl. SSE-instellingen voor MCP en de juiste `X-Forwarded-*` headers voor Keycloak).
- TLS-cert via je bestaande certbot/Let's Encrypt op die nginx.

## 1. VM of LXC?
**Aanrader: een VM** (KVM), niet LXC. Docker draait schoner en veiliger geïsoleerd in een VM;
LXC kan met `nesting=1` maar geeft met Docker/Keycloak meer gedoe.

- OS: **Debian 12** of **Ubuntu 24.04 LTS**.
- QEMU guest agent aanzetten.

## 2. Resources (sizing voor de hele stack)
De stack = nginx + eigen MCP-server + ContextForge + 2× Postgres + Redis + Keycloak (JVM = zwaarste).

| | Minimum | Aanbevolen |
|---|---|---|
| vCPU | 2 | 4 |
| RAM | 4 GB | 8 GB |
| Disk | 32 GB | 50 GB (SSD/NVMe) |

> Keycloak (~1 GB) en de twee Postgres-instanties zijn de grootste verbruikers. Onder 4 GB
> wordt het krap.

## 3. VM klaarmaken
```bash
# In de VM (Debian/Ubuntu):
sudo apt update && sudo apt -y upgrade
# Docker Engine + compose-plugin
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER          # opnieuw inloggen
docker compose version                  # check
# Project erop zetten (git clone of scp van de map MCP-server/)
```

## 4. Netwerk & TLS (via je eigen nginx)
1. **DNS**: `mcp.jouwbedrijf.nl` en `idp.jouwbedrijf.nl` → het publieke IP van je nginx-edge.
2. **TLS**: op je bestaande nginx met certbot/Let's Encrypt (bv. `certbot --nginx -d
   mcp.jouwbedrijf.nl -d idp.jouwbedrijf.nl`). Voeg de vhosts uit
   [`reverse-proxy/external-nginx.conf.example`](reverse-proxy/external-nginx.conf.example) toe.
3. **Firewall**:
   - Op de **nginx-host**: alleen **80/443** inkomend vanaf internet.
   - Op de **stack-VM**: poorten **4444/8080** alleen toelaten vanaf het nginx-host-IP
     (en `PUBLISH_BIND` op het LAN-IP). Verder dicht.
4. **Egress**: de stack-VM moet je **OpenWebUI** en **Entra** (indien gebruikt) kunnen bereiken.

## 5. Stack starten
Volg [OAUTH-SETUP.md](OAUTH-SETUP.md): `.env` vullen, domein/secret in `keycloak/realm-mcp.json`,
dan:
```bash
docker compose up -d
docker compose ps        # alles healthy?
```

## 6. Hardening (host + VM)
- SSH: alleen sleutels, geen root-login, evt. `fail2ban`.
- `unattended-upgrades` voor security-patches.
- Proxmox-firewall op datacenter/VM-niveau; plaats de VM bij voorkeur in een **apart VLAN**.
- `.env` met strikte rechten (`chmod 600`); nooit committen.
- Container-isolatie staat al in de compose (eigen MCP-server niet-publiek, `cap_drop`,
  interne netwerken, `no-new-privileges`).
- Loop [SECURITY-CHECKLIST.md](SECURITY-CHECKLIST.md) af.

## 7. Backups & herstel (betrouwbaarheid)
- **Proxmox vzdump**: plan dagelijkse VM-backups (Proxmox Backup Server of NFS).
- **Kritieke data zit in Docker-volumes**: `kcdata` (Keycloak realm/klanten), `pgdata`
  (gateway-state/RBAC), `tokendata`. Backup deze apart of zorg dat ze in de VM-backup zitten.
  ```bash
  docker run --rm -v mcp-server_kcdata:/v -v $PWD:/b alpine tar czf /b/kcdata.tgz -C /v .
  ```
- **Test een restore** vóór productie (DR-runbook).

## 8. Beschikbaarheid
- Zet de VM op **start-on-boot**; containers hebben al `restart: unless-stopped`.
- Eén node = single point of failure. Voor HA: Proxmox-cluster (≥3 nodes) + gedeelde storage,
  of accepteer korte downtime + snelle restore uit backup.
- Monitor: `docker compose ps`/healthchecks, schijf- en RAM-gebruik, certificaatverloop.

## Samengevat: wat je nodig hebt
1. Proxmox-host met capaciteit voor een VM van 4 vCPU / 8 GB / 50 GB.
2. Een VM (Debian/Ubuntu) met Docker + compose.
3. Een publiek domein + trusted TLS op je **bestaande nginx** (certbot/Let's Encrypt).
4. Firewall: 80/443 op de nginx-host; 4444/8080 op de stack-VM alleen vanaf de nginx-host; egress naar OpenWebUI.
5. Backups van de VM én de Docker-volumes, met geteste restore.
