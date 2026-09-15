# === Stage 27: Add monthly summary calculations ===
# Project: WarrantyVault
from datetime import datetime, date

def monthly_summary(warranties):
    """Return a dict: month_key -> {count, total_value, earliest_expiry, latest_expiry}."""
    summary = {}
    today = date.today()
    for w in warranties:
        if w.expiry_date is None:
            continue
        month_key = w.expiry_date.strftime("%Y-%m")
        if month_key not in summary:
            summary[month_key] = {
                "count": 0,
                "total_value": 0.0,
                "earliest_expiry": w.expiry_date,
                "latest_expiry": w.expiry_date,
            }
        entry = summary[month_key]
        entry["count"] += 1
        entry["total_value"] += w.value
        if w.expiry_date < entry["earliest_expiry"]:
            entry["earliest_expiry"] = w.expiry_date
        if w.expiry_date > entry["latest_expiry"]:
            entry["latest_expiry"] = w.expiry_date
    return summary
