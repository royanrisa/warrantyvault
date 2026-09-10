# === Stage 14: Add file load support with fallback demo data ===
# Project: WarrantyVault
def load_data(path=None):
    if path and os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
        return data
    return DEMO_DATA
