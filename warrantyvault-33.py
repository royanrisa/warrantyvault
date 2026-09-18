# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: WarrantyVault
def get_settings():
    return {
        "default_category": "Home",
        "expiry_threshold_days": 30,
        "claims_enabled": True,
        "receipt_format": "plain",
        "backup_enabled": False,
        "backup_path": "./backups",
        "notifications_enabled": False,
        "notification_email": "",
        "log_level": "INFO",
        "max_history_days": 365,
        "currency": "USD",
        "language": "en",
        "theme": "light",
        "font_size": 12,
        "last_updated": None,
    }


def update_settings(settings_dict, updates):
    if not isinstance(updates, dict):
        raise ValueError("updates must be a dictionary")
    for key, value in updates.items():
        if key not in settings_dict:
            raise KeyError(f"Unknown setting: {key}")
        if not isinstance(value, (str, int, float, bool, type(None))):
            raise TypeError(f"Invalid type for {key}: {type(value)}")
        settings_dict[key] = value
    settings_dict["last_updated"] = _current_timestamp()


def _current_timestamp():
    import datetime
    return datetime.datetime.now().isoformat()
