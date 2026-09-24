# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: WarrantyVault
def demo():
    vault = WarrantyVault()
    # Add a washer warranty
    w = Warranty(name="Washer", cost=500, expiry="2027-12-31", category="Appliance")
    vault.add(w, "receipt_washer.jpg")
    # Add an HVAC receipt
    r = Receipt(item="HVAC filter", cost=25, expiry="2026-06-15", category="Maintenance")
    vault.add(r, "receipt_hvac.jpg")
    # Add an LED bulb warranty
    w2 = Warranty(name="LED Bulb", cost=15, expiry="2025-03-01", category="Lighting")
    vault.add(w2, "receipt_led.jpg")
    # View all
    print("All items:")
    for item in vault.items:
        print(f"  {item.name} - {item.expiry} ({item.category})")
    # Search expired items
    expired = vault.find_expired()
    print(f"\nExpired items: {len(expired)}")
    for item in expired:
        print(f"  {item.name} expired on {item.expiry}")
    # Claim an expired item
    for item in expired:
        if isinstance(item, Warranty):
            claim = Claim(item, reason="Expired warranty")
            result = vault.claim(claim)
            print(f"\nClaim for {item.name}: {result}")
    # Summary
    print(f"\nSummary: {len(vault.items)} items, {len(expired)} expired, {len(vault.claims)} claims")
