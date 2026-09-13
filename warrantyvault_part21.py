# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: WarrantyVault
def archive_records(records, days_old=365):
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=days_old)
    archived = []
    for r in records:
        if r.status in ("completed", "expired", "claimed") and r.last_updated < cutoff:
            archived.append(r)
    return archived

def restore_records(records, days_old=365):
    from datetime import datetime, timedelta
    cutoff = datetime.now() - timedelta(days=days_old)
    restored = []
    for r in records:
        if r.status in ("archived",) and r.last_updated < cutoff:
            restored.append(r)
    return restored
