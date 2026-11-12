# === Stage 63: Add relationships between records where useful ===
# Project: WarrantyVault
class Warranty:
    def __init__(self, receipt, item, category, purchase_date, warranty_length_years):
        self.receipt = receipt
        self.item = item
        self.category = category
        self.purchase_date = purchase_date
        self.warranty_length_years = warranty_length_years
        self.claimed = False

    def expiry_date(self, today=None):
        if today is None:
            today = date.today()
        delta = timedelta(days=365 * self.warranty_length_years)
        return today + delta

    def valid(self, today=None):
        return not self.claimed and today <= self.expiry_date(today)


class Receipt:
    def __init__(self, store, total, date):
        self.store = store
        self.total = total
        self.date = date

    def attach(self, warranty):
        warranty.receipt = self
        self.items.append(warranty)
