# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: WarrantyVault
def generate_changelog(activity_log):
    """Return a compact multi-line changelog derived from the activity log."""
    lines = []
    for entry in activity_log:
        date = entry.get('date', entry.get('timestamp', ''))
        action = entry.get('action', entry.get('type', ''))
        item = entry.get('item', entry.get('description', ''))
        if not date:
            continue
        lines.append(f"{date} - {action}: {item}")
    return "\n".join(lines)
