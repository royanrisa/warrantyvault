# === Stage 37: Add recommendations for the next useful action ===
# Project: WarrantyVault
def generate_monthly_report(vault):
    """Summarize all warranties active in the current month."""
    today = datetime.date.today()
    active = []
    for w in vault.warranties:
        if today <= w.expiry_date:
            active.append(w)
    if not active:
        return None
    by_cat = {}
    for w in active:
        by_cat.setdefault(w.category, []).append(w)
    lines = ["Monthly Warranty Report", "========================"]
    for cat, items in by_cat.items():
        lines.append(f"\n{cat}: {len(items)}")
        for item in items:
            lines.append(f"  - {item.product_name} (expires {item.expiry_date})")
    return "\n".join(lines)
