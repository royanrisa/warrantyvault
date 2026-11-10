# === Stage 58: Add bulk update behavior for selected records ===
# Project: WarrantyVault
def bulk_update_records(records, field, mapping, ids=None):
    """Apply the same value to a field for one or all records.

    If ids is provided, only records whose id appears in ids are updated.
    Returns a list of updated record dicts.
    """
    if ids is None:
        targets = records
    else:
        targets = [r for r in records if r.get("id") in ids]

    updated = []
    for record in targets:
        record[field] = mapping.get(record.get("id"))
        updated.append(record)
    return updated


def bulk_set_expiry(records, new_expiry, ids=None):
    """Set an expiry date string across selected records."""
    return bulk_update_records(records, "expiry_date", {str(r["id"]): new_expiry for r in records}, ids)
