# === Stage 55: Add a setting to disable colorized output ===
# Project: WarrantyVault
USE_COLOR = os.environ.get("WARRANTYVAULT_COLOR", "auto").lower() == "1"

def _colorize(text, color):
    if not USE_COLOR:
        return text
    return "\033[1;{}m{}\033[0m".format(color_codes.get(color, 39), text)

color_codes = {
    "red": 31, "green": 32, "yellow": 33, "blue": 34,
    "magenta": 35, "cyan": 36, "white": 37,
}

def print_warranty_header(item):
    if not USE_COLOR:
        print("WARRANTY: {} (expires {})".format(item.name, item.expires))
        return
    print(_colorize("WARRANTY:", "cyan") + " " + item.name)
    print("Expires: " + _colorize(item.expires, "green"))

def print_claim_result(claim):
    if not USE_COLOR:
        status = "Approved" if claim.status == "approved" else claim.status
        print("Claim for {}: {}".format(claim.item, status))
        return
    status = "Approved" if claim.status == "approved" else claim.status
    if claim.status == "approved":
        print(_colorize("Claim for {}: {}".format(claim.item, status), "green"))
    else:
        print(_colorize("Claim for {}: {}".format(claim.item, status), "red"))
