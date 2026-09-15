# === Stage 25: Add daily summary calculations ===
# Project: WarrantyVault
def daily_summary(vault):
    """Print a one-line daily summary of active warranties and expiry stats."""
    today = datetime.date.today()
    active = [p for p in vault['purchases'] if p['expiry'] > today]
    expiring_soon = [p for p in active if (p['expiry'] - today).days <= 30]
    total_value = sum(p['amount'] for p in active)
    print(f"Daily Summary: {len(active)} active warranty(s) | {len(expiring_soon)} expiring within 30 days | Total value: ${total_value:.2f}")
