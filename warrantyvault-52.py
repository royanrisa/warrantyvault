# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: WarrantyVault
def format_expiry(date_str, days=365):
    """Return a human-readable expiry date given a purchase date string.

    Args:
        date_str: Purchase date in 'YYYY-MM-DD' format.
        days: Warranty length in days. Defaults to one year.

    Returns:
        The expiry date formatted as 'YYYY-MM-DD'.

    Raises:
        ValueError: If date_str is not a valid ISO date.
    """
    from datetime import datetime, timedelta
    purchase = datetime.strptime(date_str, "%Y-%m-%d").date()
    expiry = purchase + timedelta(days=days)
    return expiry.strftime("%Y-%m-%d")


def is_expired(purchase_date, days=365, today=None):
    """Check whether a warranty has expired by its purchase date.

    Args:
        purchase_date: Purchase date in 'YYYY-MM-DD' format.
        days: Warranty length in days. Defaults to one year.
        today: Reference date for the comparison. Defaults to today.

    Returns:
        True if the warranty has expired, False otherwise.
    """
    from datetime import datetime, timedelta
    if today is None:
        today = datetime.now().date()
    expiry = format_expiry(purchase_date, days)
    return today >= datetime.strptime(expiry, "%Y-%m-%d").date()


def group_by_category(items):
    """Group warranty items into a dictionary keyed by category.

    Args:
        items: An iterable of items, each with a 'category' attribute.

    Returns:
        A dictionary mapping each category to the list of items in it.
    """
    grouped = {}
    for item in items:
        category = item.category
        grouped.setdefault(category, []).append(item)
    return grouped


def active_warranties(items, today=None):
    """Return only the warranties that are still valid on a given day.

    Args:
        items: An iterable of items with 'purchase_date', 'days', and
            'category' attributes.
        today: Reference date for the comparison. Defaults to today.

    Returns:
        A list of items whose warranties have not yet expired.
    """
    from datetime import datetime
    if today is None:
        today = datetime.now().date()
    return [item for item in items if not is_expired(item.purchase_date, item.days, today)]
