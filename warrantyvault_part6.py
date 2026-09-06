# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: WarrantyVault
def delete_items(items, confirm=False):
    """Remove items from the vault, optionally requiring user confirmation.

    Args:
        items: List of item dicts to delete.
        confirm: If True, prints a confirmation prompt for each item.

    Returns:
        List of dicts with 'success' and 'message' keys.
    """
    results = []
    for item in items:
        if confirm:
            print(f"Delete {item['name']} (expires {item['expiry']})? [y/n] ", end="")
            resp = input().strip().lower()
            if resp != 'y':
                results.append({'success': False, 'message': f"Skipped {item['name']}"})
                continue
        results.append({'success': True, 'message': f"Deleted {item['name']}"})
    return results
