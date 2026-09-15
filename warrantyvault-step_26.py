# === Stage 26: Add weekly summary calculations ===
# Project: WarrantyVault
def weekly_summary(warranties):
    """Return a dict with week-over-week stats for the last 4 weeks."""
    today = datetime.today()
    summary = {}
    for i in range(4):
        week_start = today - timedelta(weeks=i) - timedelta(days=6)
        week_end = week_start + timedelta(days=6)
        week_key = week_start.strftime("%Y-%W")
        active = [w for w in warranties if w.expiry_date > week_end]
        expiring = [w for w in warranties if week_start <= w.expiry_date <= week_end]
        summary[week_key] = {
            "active": len(active),
            "expiring": len(expiring),
            "total": len(warranties),
        }
    return summary
