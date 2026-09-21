# === Stage 41: Add plain text import for a simple line-based format ===
# Project: WarrantyVault
def load_plain_lines(path):
    """Load a simple line-based plain-text format:
       line 1: category
       line 2: purchase_date (YYYY-MM-DD)
       line 3: expiry_date (YYYY-MM-DD)
       line 4: amount
       line 5: claim_status (active/expired/claimed)
       Returns list of dicts."""
    records = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append({
                'category': line[0:15],
                'purchase_date': line[16:26],
                'expiry_date': line[27:37],
                'amount': float(line[38:46]),
                'claim_status': line[47:57],
            })
    return records
