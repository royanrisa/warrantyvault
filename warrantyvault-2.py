# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: WarrantyVault
from dataclasses import dataclass
from datetime import date

@dataclass
class Purchase:
    item_name: str
    purchase_date: date
    expiry_date: date
    category: str

@dataclass
class Claim:
    purchase: Purchase
    claim_date: date
    reason: str
    status: str
