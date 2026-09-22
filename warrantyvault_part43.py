# === Stage 43: Add CSV import for the primary record type ===
# Project: WarrantyVault
def import_csv(filepath):
    """Load Warranty records from a CSV file with columns: id, category, description, purchase_date, expiry_date, price, vendor, notes."""
    records = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                purchase_date = datetime.strptime(row["purchase_date"], "%Y-%m-%d")
                expiry_date = datetime.strptime(row["expiry_date"], "%Y-%m-%d")
                price = float(row["price"])
                record = Record(
                    id=int(row["id"]),
                    category=row["category"],
                    description=row["description"],
                    purchase_date=purchase_date,
                    expiry_date=expiry_date,
                    price=price,
                    vendor=row["vendor"],
                    notes=row.get("notes", ""),
                )
                records.append(record)
            except (ValueError, KeyError):
                continue
    return records
