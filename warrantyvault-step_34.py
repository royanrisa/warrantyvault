# === Stage 34: Add support for multiple local user profiles ===
# Project: WarrantyVault
import json
import os

PROFILE_DIR = "profiles"
DEFAULT_PROFILE = "default"

def load_profile(path):
    with open(path, "r") as f:
        return json.load(f)

def save_profile(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def get_current_profile():
    if os.path.isdir(PROFILE_DIR):
        profiles = [p for p in os.listdir(PROFILE_DIR) if p != DEFAULT_PROFILE and os.path.isfile(os.path.join(PROFILE_DIR, p))]
        if profiles:
            return profiles[-1]
    return DEFAULT_PROFILE

def list_profiles():
    if not os.path.isdir(PROFILE_DIR):
        return [DEFAULT_PROFILE]
    return [DEFAULT_PROFILE] + [p for p in os.listdir(PROFILE_DIR) if p != DEFAULT_PROFILE and os.path.isfile(os.path.join(PROFILE_DIR, p))]
