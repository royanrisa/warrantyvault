# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: WarrantyVault
def parse_date(date_str, date_format=None):
    """Parse a date string into a datetime.date object with clear error messages.
    
    Args:
        date_str: The date string to parse.
        date_format: Optional format string. If None, attempts common formats.
        
    Returns:
        datetime.date object on success.
        
    Raises:
        ValueError: With a descriptive message if parsing fails.
    """
    if not date_str or not isinstance(date_str, str):
        raise ValueError("Invalid date string: must be a non-empty string")
    
    date_str = date_str.strip()
    if not date_str:
        raise ValueError("Invalid date string: empty string")
    
    if date_format is None:
        date_format = "%Y-%m-%d"
    
    import datetime
    try:
        return datetime.datetime.strptime(date_str, date_format).date()
    except ValueError:
        pass
    
    common_formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%m-%d-%Y",
        "%d/%m/%Y",
    ]
    
    for fmt in common_formats:
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse date: '{date_str}'. Supported formats: {', '.join(common_formats)}")
