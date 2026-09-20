# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: WarrantyVault
def repair_warranty_vault(db_path, table_name='warranties'):
    """Simple data integrity repair: fix common issues in the warranties table."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fix missing expiry dates
    cursor.execute(f"UPDATE {table_name} SET expiry_date = '9999-12-31' WHERE expiry_date IS NULL OR expiry_date = ''")

    # Fix missing warranty_type
    cursor.execute(f"UPDATE {table_name} SET warranty_type = 'unknown' WHERE warranty_type IS NULL OR warranty_type = ''")

    # Fix missing claim_status
    cursor.execute(f"UPDATE {table_name} SET claim_status = 'pending' WHERE claim_status IS NULL OR claim_status = ''")

    # Fix negative coverage amounts
    cursor.execute(f"UPDATE {table_name} SET coverage_amount = ABS(coverage_amount) WHERE coverage_amount < 0")

    # Fix negative repair_cost
    cursor.execute(f"UPDATE {table_name} SET repair_cost = ABS(repair_cost) WHERE repair_cost < 0")

    # Remove duplicate entries
    cursor.execute(f"DELETE FROM {table_name} WHERE rowid NOT IN (SELECT MIN(rowid) FROM {table_name} GROUP BY item, expiry_date, warranty_type, claim_status, coverage_amount, repair_cost)")

    conn.commit()
    conn.close()
    print("Warranty vault repaired successfully.")
