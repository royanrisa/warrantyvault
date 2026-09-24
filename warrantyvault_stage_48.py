# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: WarrantyVault
import unittest

from warranty_vault.models import Warranty, Claim
from warranty_vault.helpers import create_warranty, validate_warranty, create_claim, validate_claim

class TestHelpers(unittest.TestCase):
    def test_create_warranty(self):
        w = create_warranty(
            item="Laptop",
            brand="Dell",
            expiry="2026-01-01",
            category="electronics",
            notes="Used in office"
        )
        self.assertEqual(w.item, "Laptop")
        self.assertEqual(w.brand, "Dell")
        self.assertEqual(w.expiry, "2026-01-01")

    def test_validate_warranty(self):
        w = create_warranty("TV", "Samsung", "2025-06-15", "appliances")
        self.assertTrue(validate_warranty(w))

    def test_validate_warranty_expired(self):
        w = create_warranty("Phone", "Apple", "2024-01-01", "electronics")
        self.assertFalse(validate_warranty(w))

    def test_create_claim(self):
        w = create_warranty("Refrigerator", "LG", "2027-01-01", "appliances")
        c = create_claim(w, "not cooling", "2025-04-10", "repair")
        self.assertEqual(c.warranty_id, w.id)
        self.assertEqual(c.description, "not cooling")

    def test_validate_claim(self):
        w = create_warranty("Washing Machine", "Bosch", "2026-12-31", "appliances")
        c = create_claim(w, "leaking water", "2025-05-20", "parts")
        self.assertTrue(validate_claim(c))

if __name__ == "__main__":
    unittest.main()
