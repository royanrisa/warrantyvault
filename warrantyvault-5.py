# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: WarrantyVault
def update_item(self, item_id, **fields):
    """Update an existing warranty or receipt; raise KeyError if not found."""
    if item_id not in self._items:
        raise KeyError(f"No item with id={item_id}")
    entry = self._items[item_id]
    for k, v in fields.items():
        if k not in entry:
            raise ValueError(f"Unknown field '{k}' for type {entry.get('kind')}")
        entry[k] = v
    return entry
