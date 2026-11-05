# === Stage 53: Add command help text and usage examples ===
# Project: WarrantyVault
HELP = """
WarrantyVault - Home Warranty and Receipt Vault

USAGE:
  python WarrantyVault.py <command> [options]

COMMANDS:
  add       Add a new purchase with optional category and expiry
  list      List all warranties, optionally filtered by category
  show      Show details of a single warranty by id
  claim     Open a claim against a warranty
  status    Show expiry status (active/expiring/sold) for all items
  help      Show this help message and usage examples
  clear     Remove all stored data

EXAMPLES:
  python WarrantyVault.py add "Toaster" "Kitchen" --expiry 2027-01-01
  python WarrantyVault.py add "Washing Machine" --category Appliances --expiry 2026-06-15
  python WarrantyVault.py list
  python WarrantyVault.py list --category Kitchen
  python WarrantyVault.py show 1
  python WarrantyVault.py claim 1 --reason "Stopped heating"
  python WarrantyVault.py status
  python WarrantyVault.py help
"""

if __name__ == "__main__":
    print(HELP)
