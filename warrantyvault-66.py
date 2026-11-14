# === Stage 66: Add export of a short status dashboard ===
# Project: WarrantyVault
def export_status_dashboard(items, claims=None):
    if claims is None:
        claims = {}
    total_value = sum(item.get("value", 0) for item in items)
    active = [i for i in items if i.get("expiry_date", "") > "1970-01-01"]
    expiring = [i for i in items if i.get("expiry_date", "") <= "1970-01-01"]
    expired = [i for i in items if i.get("expiry_date", "") <= "1970-01-01"]
    print("WarrantyVault Status Dashboard")
    print("Total items tracked: {}".format(len(items)))
    print("Total value: ${}".format(total_value))
    print("Active warranties: {}".format(len(active)))
    print("Expired warranties: {}".format(len(expired)))
    print("Expiring soon (<= 2025-12-31): {}".format(len(expiring)))
    print("Active claims: {}".format(len(claims)))
    print("Total claim amount: ${}".format(sum(v for v in claims.values())))
