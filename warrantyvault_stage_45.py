# === Stage 45: Add restore from backup with validation ===
# Project: WarrantyVault
def restore_from_backup(backup_path, vault=None):
    if not backup_path or not os.path.exists(backup_path):
        return False, "Backup file not found."
    try:
        with open(backup_path, "r") as f:
            data = json.load(f)
        if not data.get("version") == 1:
            return False, "Unsupported backup version."
        if vault:
            vault.items = data.get("items", [])
            vault.categories = data.get("categories", [])
            vault.claims = data.get("claims", [])
        return True, "Restore successful."
    except Exception as e:
        return False, f"Restore failed: {str(e)}"
