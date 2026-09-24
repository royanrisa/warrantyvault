# === Stage 46: Add a schema version field and migration helper ===
# Project: WarrantyVault
import json
from pathlib import Path

SCHEMA_VERSION = 2
SCHEMA_PATH = Path(__file__).parent / "schema.json"

MIGRATIONS = {
    1: lambda d: d,
    2: lambda d: {
        **d,
        "schema_version": SCHEMA_VERSION,
    },
}

def migrate(data: dict) -> dict:
    """Apply schema migrations up to the current version."""
    current = data.get("schema_version", 0)
    for version, fn in MIGRATIONS.items():
        if version > current:
            data = fn(data)
    return data

def get_schema() -> dict:
    """Load the schema with migrations applied."""
    return migrate(json.loads(SCHEMA_PATH.read_text()))
