"""Beheerbare API-tokens voor klanten.

Veiligheidskeuzes:
- Het token is hoge-entropie en willekeurig (`secrets`).
- We slaan ALLEEN de SHA-256-hash op, nooit het token zelf -> DB-lek geeft geen werkende tokens.
- Elk token heeft een eigenaar/label, aanmaakdatum, optionele vervaldatum en intrekstatus.
- Validatie gebeurt via hash-lookup (geen plaintext-vergelijking).
"""
import sqlite3
import secrets
import hashlib
import time
from typing import Optional

import config

_TOKEN_PREFIX = "kn"  # herkenbaar prefix; helpt bij secret-scanning


def _conn() -> sqlite3.Connection:
    conn = sqlite3.connect(config.TOKEN_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tokens (
                id          TEXT PRIMARY KEY,
                token_hash  TEXT NOT NULL UNIQUE,
                label       TEXT NOT NULL,
                created_at  INTEGER NOT NULL,
                expires_at  INTEGER,
                revoked     INTEGER NOT NULL DEFAULT 0
            )
            """
        )


def _hash(raw: str) -> str:
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def issue(label: str, ttl_days: Optional[int] = None) -> str:
    """Maak een nieuw token aan. Geeft het RUWE token terug (eenmalig zichtbaar)."""
    init_db()
    token_id = secrets.token_hex(6)
    secret = secrets.token_urlsafe(32)
    raw = f"{_TOKEN_PREFIX}_{token_id}_{secret}"
    expires_at = int(time.time()) + ttl_days * 86400 if ttl_days else None
    with _conn() as conn:
        conn.execute(
            "INSERT INTO tokens (id, token_hash, label, created_at, expires_at) VALUES (?, ?, ?, ?, ?)",
            (token_id, _hash(raw), label, int(time.time()), expires_at),
        )
    return raw


def revoke(token_id: str) -> bool:
    with _conn() as conn:
        cur = conn.execute("UPDATE tokens SET revoked = 1 WHERE id = ?", (token_id,))
        return cur.rowcount > 0


def list_tokens() -> list[sqlite3.Row]:
    init_db()
    with _conn() as conn:
        return conn.execute(
            "SELECT id, label, created_at, expires_at, revoked FROM tokens ORDER BY created_at DESC"
        ).fetchall()


def validate(raw: Optional[str]) -> Optional[dict]:
    """Geef een principal terug bij een geldig, niet-ingetrokken, niet-verlopen token; anders None."""
    if not raw:
        return None
    with _conn() as conn:
        row = conn.execute(
            "SELECT id, label, expires_at, revoked FROM tokens WHERE token_hash = ?",
            (_hash(raw),),
        ).fetchone()
    if row is None or row["revoked"]:
        return None
    if row["expires_at"] is not None and row["expires_at"] < int(time.time()):
        return None
    return {"id": row["id"], "label": row["label"]}
