# === Stage 36: Add templates for quickly creating common records ===
# Project: WarrantyVault
def create_record_template(record_type, name, details):
    """Create a record of the given type with a name and details dictionary.

    Args:
        record_type (str): The type of record to create (e.g., 'Purchase', 'Warranty', 'Receipt', 'Claim').
        name (str): The name of the record.
        details (dict): Additional details specific to the record type.

    Returns:
        dict: A dictionary representing the created record.
    """
    if record_type == 'Purchase':
        return {
            'type': 'Purchase',
            'name': name,
            'details': details,
            'created_at': details.get('created_at', '2024-01-01'),
        }
    elif record_type == 'Warranty':
        return {
            'type': 'Warranty',
            'name': name,
            'expiry_date': details.get('expiry_date', '2025-01-01'),
            'created_at': details.get('created_at', '2024-01-01'),
        }
    elif record_type == 'Receipt':
        return {
            'type': 'Receipt',
            'name': name,
            'amount': details.get('amount', 0.0),
            'created_at': details.get('created_at', '2024-01-01'),
        }
    elif record_type == 'Claim':
        return {
            'type': 'Claim',
            'name': name,
            'status': details.get('status', 'pending'),
            'created_at': details.get('created_at', '2024-01-01'),
        }
    else:
        raise ValueError(f"Unknown record type: {record_type}")
