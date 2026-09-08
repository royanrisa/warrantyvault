# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: WarrantyVault
class CaseInsensitiveSearch:
    def __init__(self):
        self._index = {}

    def add_entry(self, entry):
        for key in entry.keys():
            lower = str(entry[key]).lower()
            if lower not in self._index:
                self._index[lower] = []
            self._index[lower].append(entry)

    def search(self, field, query):
        return [e for e in self._index.get(query.lower(), []) if field.lower() in e.keys()]
