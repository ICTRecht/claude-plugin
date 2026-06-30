"""Beheer-CLI voor klanttokens: uitgeven, opsommen, intrekken.

Voorbeelden (in de container):
  python manage_tokens.py issue  --label "Klant Acme" --ttl-days 90
  python manage_tokens.py list
  python manage_tokens.py revoke --id 1a2b3c4d5e6f
"""
import argparse
import datetime as _dt

import tokens


def _fmt(ts):
    return _dt.datetime.fromtimestamp(ts, _dt.timezone.utc).strftime("%Y-%m-%d") if ts else "-"


def main() -> None:
    p = argparse.ArgumentParser(description="Beheer klanttokens voor de MCP-server")
    sub = p.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("issue", help="Geef een nieuw token uit")
    pi.add_argument("--label", required=True, help="Eigenaar/klantnaam")
    pi.add_argument("--ttl-days", type=int, default=None, help="Geldigheid in dagen (standaard: oneindig)")

    sub.add_parser("list", help="Toon alle tokens (zonder de geheime waarde)")

    pr = sub.add_parser("revoke", help="Trek een token in")
    pr.add_argument("--id", required=True, help="Token-id (zie 'list')")

    args = p.parse_args()

    if args.cmd == "issue":
        raw = tokens.issue(args.label, args.ttl_days)
        print("Token aangemaakt. Geef dit EENMALIG door aan de klant (wordt niet opnieuw getoond):\n")
        print(f"  {raw}\n")
        print("De klant plakt dit als Bearer-token in zijn AI-tool (zie server/README.md).")
    elif args.cmd == "list":
        rows = tokens.list_tokens()
        if not rows:
            print("Geen tokens.")
            return
        print(f"{'ID':<14} {'LABEL':<24} {'AANGEMAAKT':<12} {'VERVALT':<12} STATUS")
        for r in rows:
            status = "INGETROKKEN" if r["revoked"] else "actief"
            print(f"{r['id']:<14} {r['label'][:24]:<24} {_fmt(r['created_at']):<12} {_fmt(r['expires_at']):<12} {status}")
    elif args.cmd == "revoke":
        ok = tokens.revoke(args.id)
        print("Ingetrokken." if ok else "Token-id niet gevonden.")


if __name__ == "__main__":
    main()
