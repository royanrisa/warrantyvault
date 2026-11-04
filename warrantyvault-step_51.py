# === Stage 51: Add unit tests for search and filter behavior ===
# Project: WarrantyVault
def test_search_by_category():
    vault = WarrantyVault()
    vault.add_purchase(Purchase("TV", "Samsung", "Electronics", "2024-01-01", "2029-01-01"))
    vault.add_purchase(Purchase("Refrigerator", "LG", "Appliances", "2023-06-15", "2028-06-15"))
    results = vault.search(category="Electronics")
    assert len(results) == 1
    assert results[0].name == "TV"


def test_search_by_keyword():
    vault = WarrantyVault()
    vault.add_purchase(Purchase("Washing Machine", "Bosch", "Appliances", "2022-03-10", "2027-03-10"))
    results = vault.search(keyword="wash")
    assert len(results) == 1
    assert results[0].name == "Washing Machine"


def test_filter_by_expiry_status():
    vault = WarrantyVault()
    vault.add_purchase(Purchase("Laptop", "Dell", "Electronics", "2020-01-01", "2021-01-01"))
    vault.add_purchase(Purchase("Microwave", "Panasonic", "Appliances", "2024-05-01", "2029-05-01"))
    active = vault.filter(expiry_status="active")
    assert len(active) == 1
    assert active[0].name == "Microwave"
    expired = vault.filter(expiry_status="expired")
    assert len(expired) == 1
    assert expired[0].name == "Laptop"


def test_filter_by_category_multiple():
    vault = WarrantyVault()
    vault.add_purchase(Purchase("TV", "Samsung", "Electronics", "2024-01-01", "2029-01-01"))
    vault.add_purchase(Purchase("Fridge", "LG", "Appliances", "2023-06-15", "2028-06-15"))
    results = vault.filter(categories=["Electronics", "Appliances"])
    assert len(results) == 2
