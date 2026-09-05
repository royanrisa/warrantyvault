# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: WarrantyVault
def validate_required(value, field_name):
    if value is None or (isinstance(value, str) and value.strip() == ''):
        raise ValueError(f"Field '{field_name}' is required")
    return value

def validate_positive_integer(value, field_name):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"Field '{field_name}' must be a positive integer")
    return value

def validate_positive_float(value, field_name):
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"Field '{field_name}' must be a positive number")
    return float(value)

def validate_date_value(value, field_name):
    try:
        from datetime import datetime
        datetime.strptime(value, '%Y-%m-%d')
        return value
    except ValueError:
        raise ValueError(f"Field '{field_name}' must be a valid date (YYYY-MM-DD)")

def validate_short_text(value, field_name, max_length=50):
    if not isinstance(value, str):
        raise ValueError(f"Field '{field_name}' must be a string")
    if len(value) > max_length:
        raise ValueError(f"Field '{field_name}' exceeds max length of {max_length} characters")
    return value
