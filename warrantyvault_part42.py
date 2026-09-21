# === Stage 42: Add CSV export without external dependencies ===
# Project: WarrantyVault
import csv
from datetime import date
from pathlib import Path

def export_to_csv(vault, filename="warranty_vault.csv"):
    """Export the entire WarrantyVault to a CSV file without external dependencies."""
    path = Path(filename)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["warranty_id", "product", "purchase_date", "expiry_date",
                         "category", "value", "location", "status", "claim_date", "claim_amount"])
        for item in vault.items.values():
            writer.writerow([
                item.warranty_id, item.product, item.purchase_date, item.expiry_date,
                item.category, item.value, item.location, item.status,
                item.claim_date, item.claim_amount
            ])
    print(f"Exported {len(vault.items)} warranties to {path}")
