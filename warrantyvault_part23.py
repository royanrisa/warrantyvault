# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: WarrantyVault
def add_tag(record, tag):
    if record.get("tags") is None:
        record["tags"] = []
    if tag not in record["tags"]:
        record["tags"].append(tag)
    return record

def remove_tag(record, tag):
    if record.get("tags") and tag in record["tags"]:
        record["tags"].remove(tag)
    return record

def tag_summary(records, tag):
    from collections import Counter
    counts = Counter(rec.get("tags", []) for rec in records if rec.get("tags"))
    return dict(counts)
