# === Stage 64: Add validation for relationship references ===
# Project: WarrantyVault
def validate_references(items, categories, claims):
    category_ids = {c['id'] for c in categories}
    valid_item_ids = {i['id'] for i in items}
    valid_claim_ids = {c['id'] for c in claims}

    for item in items:
        if item.get('category_id') is not None:
            if item['category_id'] not in category_ids:
                raise ValueError(f"Item {item['id']} references unknown category {item['category_id']}")

    for claim in claims:
        if claim.get('item_id') is not None:
            if claim['item_id'] not in valid_item_ids:
                raise ValueError(f"Claim {claim['id']} references unknown item {claim['item_id']}")

    return len(items), len(categories), len(claims)
