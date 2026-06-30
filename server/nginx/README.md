# TLS-certificaten

Plaats hier `fullchain.pem` en `privkey.pem` in `nginx/certs/`.

**Productie:** gebruik een echt certificaat (Let's Encrypt / interne CA).

**Lokaal testen (self-signed):**
```bash
mkdir -p certs
openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout certs/privkey.pem -out certs/fullchain.pem \
  -subj "/CN=localhost"
```
> `certs/` staat in `.gitignore` — commit nooit private keys.
