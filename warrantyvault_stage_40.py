# === Stage 40: Add plain text report export ===
# Project: WarrantyVault
def export_report(self, filepath="warranty_vault_report.txt"):
    """Export a plain text report of all warranties and claims."""
    lines = []
    lines.append("=" * 50)
    lines.append("WARRANTY VAULT REPORT")
    lines.append("=" * 50)
    for w in self.warranties:
        lines.append(f"\nWarranty: {w.product}")
        lines.append(f"  Category: {w.category}")
        lines.append(f"  Purchase Date: {w.purchase_date}")
        lines.append(f"  Expiry Date: {w.expiry_date}")
        lines.append(f"  Status: {w.status}")
        if w.claimed:
            lines.append(f"  Claim Status: {w.claim_status}")
            lines.append(f"  Claim Date: {w.claim_date}")
            lines.append(f"  Claim Amount: ${w.claim_amount}")
    lines.append("\n" + "=" * 50)
    lines.append("END OF REPORT")
    lines.append("=" * 50)
    with open(filepath, "w") as f:
        f.write("\n".join(lines))
    return filepath
