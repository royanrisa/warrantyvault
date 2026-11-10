# === Stage 56: Add compact error classes for domain failures ===
# Project: WarrantyVault
class WarrantyVaultError(Exception):
    pass


class PurchaseNotFoundError(WarrantyVaultError):
    def __init__(self, purchase_id):
        self.purchase_id = purchase_id
        super().__init__(f"Purchase {purchase_id} not found")


class DuplicatePurchaseError(WarrantyVaultError):
    def __init__(self, purchase_id):
        self.purchase_id = purchase_id
        super().__init__(f"Duplicate purchase {purchase_id}")


class ExpiryError(WarrantyVaultError):
    pass


class ExpiredWarrantyError(ExpiryError):
    def __init__(self, warranty_id):
        self.warranty_id = warranty_id
        super().__init__(f"Warranty {warranty_id} has expired")


class NotYetValidError(ExpiryError):
    def __init__(self, warranty_id):
        self.warranty_id = warranty_id
        super().__init__(f"Warranty {warranty_id} is not yet valid")


class ClaimNotFoundError(WarrantyVaultError):
    def __init__(self, claim_id):
        self.claim_id = claim_id
        super().__init__(f"Claim {claim_id} not found")


class AlreadyClaimedError(WarrantyVaultError):
    def __init__(self, warranty_id):
        self.warranty_id = warranty_id
        super().__init__(f"Warranty {warranty_id} has already been claimed")
