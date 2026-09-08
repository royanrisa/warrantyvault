# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: WarrantyVault
def sort_warranties(warranty_list, key="title"):
    if key == "title":
        return sorted(warranty_list, key=lambda w: w["title"].lower())
    elif key == "date":
        return sorted(warranty_list, key=lambda w: w["expiry_date"], reverse=True)
    elif key == "priority":
        return sorted(warranty_list, key=lambda w: w.get("priority", 0), reverse=True)
    elif key == "last_update":
        return sorted(warranty_list, key=lambda w: w.get("last_update", w["created"]), reverse=True)
    return warranty_list
