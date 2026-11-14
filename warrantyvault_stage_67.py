# === Stage 67: Add a function that returns key project metrics ===
# Project: WarrantyVault
def get_project_metrics(vault):
    total_items = len(vault.items)
    total_value = sum(item.purchase_price for item in vault.items)
    active_items = [item for item in vault.items if not item.is_expired()]
    expired_items = [item for item in vault.items if item.is_expired()]
    claims_resolved = sum(1 for claim in vault.claims if claim.status == "resolved")
    claims_pending = sum(1 for claim in vault.claims if claim.status == "pending")
    category_counts = {}
    for item in vault.items:
        category_counts[item.category] = category_counts.get(item.category, 0) + 1
    return {
        "total_items": total_items,
        "total_value": total_value,
        "active_items": len(active_items),
        "expired_items": len(expired_items),
        "claims_resolved": claims_resolved,
        "claims_pending": claims_pending,
        "category_counts": category_counts,
    }
