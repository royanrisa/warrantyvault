# === Stage 11: Add JSON export for the current application state ===
# Project: WarrantyVault
def export_state(app, path="warranty_vault.json"):
    """Export the current application state to a JSON file."""
    state = {
        "purchases": [p.to_dict() for p in app.purchases],
        "categories": list(app.categories),
        "claims": [c.to_dict() for c in app.claims],
        "last_updated": datetime.now().isoformat(),
    }
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
