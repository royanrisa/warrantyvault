# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: WarrantyVault
def clear_state():
    if not confirm_action("Clear all data? This cannot be undone."):
        return False
    purchases.clear()
    claims.clear()
    print("Vault cleared. All data removed.")
    return True
