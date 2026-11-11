# === Stage 60: Add saved views for frequently used filters ===
# Project: WarrantyVault
SavedView = namedtuple("SavedView", "name columns sort_key sort_dir filters")

DEFAULT_COLUMNS = ["id", "description", "category", "purchase_date", "expiry_date", "status"]
SORT_KEYS = ["id", "description", "category", "purchase_date", "expiry_date", "status"]


def apply_saved_view(vault, view):
    rows = [r for r in vault.rows if all(r.get(f) == v.filters.get(f) for f in v.filters)]
    rows = [r for r in rows if r.get(c) == v.columns[0] for c in v.columns]
    reverse = v.sort_dir == "desc"
    rows.sort(key=lambda r: r.get(v.sort_key, ""), reverse=reverse)
    vault.rows = rows


SAVED_VIEWS = {
    "active": SavedView("Active", DEFAULT_COLUMNS, "expiry_date", "asc", {"status": "active"}),
    "expired": SavedView("Expired", DEFAULT_COLUMNS, "expiry_date", "asc", {"status": "expired"}),
    "recent": SavedView("Recent Purchases", DEFAULT_COLUMNS, "purchase_date", "desc", {"status": "active"}),
    "home": SavedView("Home", ["id", "description", "expiry_date", "status"], "expiry_date", "asc", {"category": "Home"}),
    "electronics": SavedView("Electronics", ["id", "description", "expiry_date", "status"], "expiry_date", "asc", {"category": "Electronics"}),
    "recent_expired": SavedView("Recently Expired", DEFAULT_COLUMNS, "expiry_date", "desc", {"status": "expired"}),
}


def load_saved_views(vault):
    vault.saved_views = SAVED_VIEWS


def apply_saved_view_by_name(vault, name):
    view = vault.saved_views.get(name)
    if view:
        apply_saved_view(vault, view)
        vault.current_view = name
        return True
    return False


def list_saved_views(vault):
    return [v.name for v in vault.saved_views.values()]


def register_saved_view(vault, name, columns, sort_key, sort_dir, filters):
    if not name or not columns:
        return False
    if sort_key not in SORT_KEYS:
        sort_key = "id"
    if sort_dir not in ("asc", "desc"):
        sort_dir = "asc"
    vault.saved_views[name] = SavedView(name, columns, sort_key, sort_dir, filters)
    return True


def remove_saved_view(vault, name):
    return vault.saved_views.pop(name, None) is not None


def apply_all_saved_views(vault):
    for view in vault.saved_views.values():
        apply_saved_view(vault, view)
