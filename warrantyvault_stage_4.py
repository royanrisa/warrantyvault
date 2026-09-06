# === Stage 4: Implement create operations for the primary records ===
# Project: WarrantyVault
def create_purchase(self, name, cost, purchase_date, expires, category, notes=None):
    """Create a new Purchase record."""
    if not isinstance(name, str) or not name:
        raise ValueError("Purchase name must be a non-empty string")
    if cost < 0:
        raise ValueError("Cost cannot be negative")
    if purchase_date is None or expires is None:
        raise ValueError("purchase_date and expires are required")
    self._validate_date(purchase_date)
    self._validate_date(expires)
    if expires <= purchase_date:
        raise ValueError("Expiration date must be after purchase date")
    if category is None:
        category = "General"
    record = {"name": name, "cost": cost, "purchase_date": purchase_date, "expires": expires, "category": category, "notes": notes or ""}
    self._records["purchases"].append(record)
    return record.copy()

def create_receipt(self, name, cost, purchase_date, receipt_date, category, notes=None):
    """Create a new Receipt record."""
    if not isinstance(name, str) or not name:
        raise ValueError("Receipt name must be a non-empty string")
    if cost < 0:
        raise ValueError("Cost cannot be negative")
    if purchase_date is None or receipt_date is None:
        raise ValueError("purchase_date and receipt_date are required")
    self._validate_date(purchase_date)
    self._validate_date(receipt_date)
    if category is None:
        category = "General"
    record = {"name": name, "cost": cost, "purchase_date": purchase_date, "receipt_date": receipt_date, "category": category, "notes": notes or ""}
    self._records["receipts"].append(record)
    return record.copy()
