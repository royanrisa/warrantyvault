# === Stage 28: Add overdue item detection based on due dates ===
# Project: WarrantyVault
def find_overdue_items(vault, today=None):
    if today is None:
        today = datetime.date.today()
    overdue = []
    for item in vault:
        if item.get("expired", True):
            continue
        due = item.get("due_date")
        if due and isinstance(due, datetime.date):
            if due < today:
                overdue.append({
                    "item": item,
                    "days_overdue": (today - due).days,
                })
    return overdue
