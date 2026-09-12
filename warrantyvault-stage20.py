# === Stage 20: Add duplicate detection for newly created records ===
# Project: WarrantyVault
import hashlib
from datetime import datetime, timezone

def _normalize(text):
    return text.strip().lower().replace(" ", "")

def _fingerprint(record):
    """Produce a 64-bit hash for a record dict (ignoring id and created_at)."""
    parts = []
    for key in ("item", "category", "purchase_date", "expiry_date", "amount", "warranty_type", "vendor", "notes"):
        if key in record:
            parts.append(_normalize(record[key]))
    raw = "|".join(parts)
    return int(hashlib.md5(raw.encode()).hexdigest(), 16)

def find_duplicates(records, new_record):
    """Return list of existing records whose fingerprint matches the new one."""
    fp_new = _fingerprint(new_record)
    return [
        r for r in records
        if r.get("id") != new_record.get("id")
        and _fingerprint(r) == fp_new
    ]
