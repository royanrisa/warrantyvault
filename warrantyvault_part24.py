# === Stage 24: Add grouped summaries by category or status ===
# Project: WarrantyVault
def grouped_summaries(self, group_by='category'):
    groups = {}
    for item in self.items:
        if group_by == 'category':
            key = item.category
        elif group_by == 'status':
            key = 'expired' if item.expired else 'active'
        else:
            key = item.category
        groups.setdefault(key, []).append(item)
    return groups
