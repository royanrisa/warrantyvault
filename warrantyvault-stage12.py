# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: WarrantyVault
import json

def load_warranty_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{file_path}': {e}")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{file_path}'.")
        return None
    return data
