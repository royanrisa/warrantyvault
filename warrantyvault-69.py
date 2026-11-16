# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: WarrantyVault
import json
import os
import shutil


def reset_demo_data(vault_path="warranty_vault.json"):
    """Reset the warranty vault to a fresh demo dataset for manual testing."""
    demo = {
        "purchases": [
            {"id": "P001", "item": "Kitchen Appliance", "category": "Appliances",
             "store": "BigMart", "purchase_date": "2023-01-15", "warranty_months": 24,
             "expiry_date": "2025-01-15", "receipt_url": "https://example.com/receipt/P001",
             "paid": True, "notes": "Covers motor and heating element"},
            {"id": "P002", "item": "Plumber Service", "category": "Services",
             "store": "QuickFix", "purchase_date": "2023-06-01", "warranty_months": 12,
             "expiry_date": "2024-06-01", "receipt_url": "https://example.com/receipt/P002",
             "paid": False, "notes": "Emergency callout only"},
            {"id": "P003", "item": "Roof Shingles", "category": "Structural",
             "store": "HomeBuild", "purchase_date": "2022-11-20", "warranty_months": 60,
             "expiry_date": "2032-11-20", "receipt_url": "https://example.com/receipt/P003",
             "paid": True, "notes": "Weather resistant coating"},
        ],
        "claims": [
            {"id": "C001", "purchase_id": "P001", "description": "Motor overheating",
             "status": "open", "filed_date": "2024-02-10", "amount": 150.0},
            {"id": "C002", "purchase_id": "P003", "description": "Leaking seal",
             "status": "approved", "filed_date": "2024-01-05", "amount": 80.0},
        ],
    }
    tmp = vault_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(demo, f, indent=2)
    if os.path.exists(vault_path):
        shutil.move(tmp, vault_path)
    print(f"Demo data reset at {os.path.abspath(vault_path)}")
