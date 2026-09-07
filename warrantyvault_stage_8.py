# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: WarrantyVault
def filter_vault(vault, status=None, category=None, owner=None, tag=None):
    filtered = vault
    if status is not None:
        filtered = [item for item in filtered if item.get("status") == status]
    if category is not None:
        filtered = [item for item in filtered if item.get("category") == category]
    if owner is not None:
        filtered = [item for item in filtered if item.get("owner") == owner]
    if tag is not None:
        filtered = [item for item in filtered if tag in item.get("tags", [])]
    return filtered
