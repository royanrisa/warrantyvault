# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: WarrantyVault
def test_update_preserves_missing_expiry():
    vault = WarrantyVault()
    vault.add_purchase("ref", "TV", "Electronics", "2025-01-01", "365")
    old = vault.update("ref", "Electronics", "2026-01-01", "730")
    assert old.expiry_date == "2025-01-01"


def test_update_invalid_expiry_ignored():
    vault = WarrantyVault()
    vault.add_purchase("ref", "TV", "Electronics", "2025-01-01", "365")
    changed = vault.update("ref", "Electronics", "not-a-date", "365")
    assert changed is None
    assert len(vault.purchases) == 1


def test_update_missing_reference_ignored():
    vault = WarrantyVault()
    changed = vault.update("nope", "TV", "Electronics", "2026-01-01", "365")
    assert changed is None


def test_delete_missing_reference_ignored():
    vault = WarrantyVault()
    result = vault.delete("nope")
    assert result is False
    assert len(vault.purchases) == 0


def test_delete_returns_existing_reference():
    vault = WarrantyVault()
    vault.add_purchase("ref", "TV", "Electronics", "2025-01-01", "365")
    assert vault.delete("ref") is True
    assert vault.delete("ref") is False
    assert len(vault.purchases) == 0
