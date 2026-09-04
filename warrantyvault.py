# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: WarrantyVault
import datetime

class Warranty:
    def __init__(self, category, purchase_date, expiry_date, product_name, vendor):
        self.category = category
        self.purchase_date = purchase_date
        self.expiry_date = expiry_date
        self.product_name = product_name
        self.vendor = vendor
        self.claimed = False

demo_warranties = [
    Warranty("Electronics", datetime.date(2023, 6, 1), datetime.date(2024, 6, 1), "Laptop X200", "TechStore"),
    Warranty("Appliances", datetime.date(2023, 3, 15), datetime.date(2024, 3, 15), "Dishwasher Pro5", "HomeGoods"),
    Warranty("Electronics", datetime.date(2024, 1, 10), datetime.date(2025, 1, 10), "Smartphone Z9", "MobileMart"),
    Warranty("Furniture", datetime.date(2023, 9, 5), datetime.date(2024, 9, 5), "Office Chair Ergo", "FurniPlus"),
]
