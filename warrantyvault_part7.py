# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: WarrantyVault
def format_warranty(warranty):
    lines = [f"Warranty: {warranty.name}"]
    lines.append(f"  ID: {warranty.warranty_id}")
    lines.append(f"  Product: {warranty.product}")
    lines.append(f"  Purchased: {warranty.purchase_date}")
    lines.append(f"  Expires: {warranty.expiration_date}")
    lines.append(f"  Status: {warranty.status}")
    if warranty.claimed:
        lines.append(f"  Claim: {warranty.claim}")
    return "\n".join(lines)

def format_receipt(receipt):
    lines = [f"Receipt: {receipt.receipt_id}"]
    lines.append(f"  Date: {receipt.purchase_date}")
    lines.append(f"  Vendor: {receipt.vendor}")
    lines.append(f"  Amount: {receipt.amount}")
    lines.append(f"  Warranty: {receipt.warranty_id}")
    return "\n".join(lines)

def print_warranties(warranties):
    for w in warranties:
        print(format_warranty(w))

def print_receipts(receipts):
    for r in receipts:
        print(format_receipt(r))
