# === Stage 44: Add backup creation for the data file ===
# Project: WarrantyVault
def create_backup(data_file):
    """Create a timestamped backup of the warranty data file."""
    import shutil
    import os
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(os.path.dirname(data_file), f"warranty_backup_{timestamp}.json")
    if os.path.exists(backup_path):
        os.remove(backup_path)
    shutil.copy2(data_file, backup_path)
    print(f"Backup created: {backup_path}")
