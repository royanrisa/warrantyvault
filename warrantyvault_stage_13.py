# === Stage 13: Add file save support using a configurable path ===
# Project: WarrantyVault
def save(self, path: str | None = None):
        path = path or self._default_path
        if not path:
            raise ValueError("No save path configured")
        with open(path, "w") as f:
            for item in self.items:
                f.write(f"{item.category},{item.purchase_date},{item.expiry_date},{item.claimed}\n")
