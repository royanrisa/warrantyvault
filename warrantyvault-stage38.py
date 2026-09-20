# === Stage 38: Add data integrity checks for broken references ===
# Project: WarrantyVault
def validate_references(warranty_db):
    """Check for broken references in warranty database."""
    errors = []
    for w in warranty_db:
        if w['purchase_id'] not in warranty_db:
            errors.append(f"Broken purchase reference: {w['purchase_id']}")
        if w['category_id'] not in warranty_db:
            errors.append(f"Broken category reference: {w['category_id']}")
        if w['receipt_id'] and w['receipt_id'] not in warranty_db:
            errors.append(f"Broken receipt reference: {w['receipt_id']}")
    return errors
