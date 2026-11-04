# === Stage 50: Add unit tests for import and export behavior ===
# Project: WarrantyVault
import json
import os
from datetime import date
from unittest import TestCase


class TestWarrantyVault(TestCase):

    def test_import_from_json_roundtrip(self):
        from warranty_vault import WarrantyVault
        v = WarrantyVault()
        v.add_purchase("Fridge", "LG", "2024-01-01", "2029-01-01", "Appliances")
        v.export_to_json("test_export.json")
        with open("test_export.json") as f:
            data = json.load(f)
        self.assertEqual(len(data["purchases"]), 1)
        self.assertEqual(data["purchases"][0]["product"], "Fridge")
        os.remove("test_export.json")

    def test_export_import_cycle_preserves_data(self):
        from warranty_vault import WarrantyVault
        v1 = WarrantyVault()
        v1.add_purchase("Washer", "Samsung", "2023-05-10", "2028-05-10", "Appliances")
        v1.add_claim("Fridge", "2024-06-01", "Broken compressor")
        v1.export_to_json("test_cycle.json")
        with open("test_cycle.json") as f:
            data = json.load(f)
        v2 = WarrantyVault()
        v2.import_from_json(data)
        self.assertEqual(len(v2.get_purchases()), 1)
        self.assertEqual(len(v2.get_claims()), 1)
        self.assertEqual(v2.get_claims()[0]["product"], "Fridge")
        os.remove("test_cycle.json")

    def test_export_nonexistent_file_raises(self):
        from warranty_vault import WarrantyVault
        v = WarrantyVault()
        with self.assertRaises(FileNotFoundError):
            v.export_to_json("does_not_exist.json")
