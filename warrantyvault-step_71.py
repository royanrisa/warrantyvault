# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: WarrantyVault
def seed_demo_data(vault, seed=42):
    rng = random.Random(seed)
    categories = ["Appliance", "Electronics", "Plumbing", "HVAC", "Warranty"]
    items = [
        ("Refrigerator", "Samsung", "2022-05-15", "2027-05-15"),
        ("Washing Machine", "LG", "2023-02-20", "2028-02-20"),
        ("Dryer", "Whirlpool", "2021-11-03", "2026-11-03"),
        ("Dishwasher", "Bosch", "2024-07-10", "2029-07-10"),
        ("Air Conditioner", "Carrier", "2020-06-30", "2025-06-30"),
        ("Microwave", "Panasonic", "2023-09-12", "2028-09-12"),
        ("Toaster", "Cuisinart", "2025-01-05", "2030-01-05"),
        ("Television", "Sony", "2022-12-25", "2027-12-25"),
        ("Water Heater", "Rheem", "2021-08-18", "2026-08-18"),
        ("Range/Oven", "GE", "2024-03-01", "2029-03-01"),
    ]
    for name, brand, start, end in items:
        category = rng.choice(categories)
        vault.add_purchase(brand, name, start, end, category)
        claims = rng.randint(0, 2)
        for i in range(claims):
            vault.add_claim(name, f"Service visit {i+1}", rng.randint(80, 400))
