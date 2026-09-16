# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: WarrantyVault
def get_upcoming_items(items, days_ahead=30):
    """Return items expiring within `days_ahead` days from today."""
    today = datetime.date.today()
    cutoff = today + timedelta(days=days_ahead)
    return [
        {
            "item": i,
            "days_left": (i["expiry_date"] - today).days,
            "status": "upcoming" if i["expiry_date"] <= cutoff else "far",
        }
        for i in items
        if i["expiry_date"] <= cutoff
    ]


def get_expired_items(items):
    """Return items that have already expired."""
    today = datetime.date.today()
    return [
        {"item": i, "days_left": (i["expiry_date"] - today).days}
        for i in items
        if i["expiry_date"] < today
    ]


def get_due_in_days(items, days=7):
    """Return items due within `days` days (including today)."""
    today = datetime.date.today()
    due = today + timedelta(days=days)
    return [
        {"item": i, "days_left": (i["expiry_date"] - today).days}
        for i in items
        if today <= i["expiry_date"] <= due
    ]
