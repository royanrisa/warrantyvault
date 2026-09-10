# === Stage 16: Add argparse support for the most common commands ===
# Project: WarrantyVault
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="WarrantyVault CLI")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("list", help="list all warranties")
    p.add_argument("--category", "-c", choices=["electronics", "appliances", "tools", "all"], default="all")

    p = sub.add_parser("add", help="add a warranty")
    p.add_argument("--name", "-n", required=True)
    p.add_argument("--vendor", "-v", required=True)
    p.add_argument("--expiry", "-e", required=True)
    p.add_argument("--category", "-c", default="all")
    p.add_argument("--receipt", "-r", help="path to receipt image")

    p = sub.add_parser("claim", help="file a claim")
    p.add_argument("--warranty", "-w", required=True)
    p.add_argument("--reason", "-R", required=True)
    p.add_argument("--evidence", "-E", help="path to evidence")

    p = sub.add_parser("status", help="check warranty status")
    p.add_argument("--warranty", "-w", required=True)

    p = sub.add_parser("export", help="export to JSON")
    p.add_argument("--output", "-o", default="warranty_vault.json")

    return parser.parse_args()
