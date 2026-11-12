# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: WarrantyVault
def priority_score(item):
    days_left = (item['expiry_date'] - datetime.now()).days
    if days_left < 0:
        return 100
    if days_left < 30:
        return 70 + (30 - days_left)
    if days_left < 90:
        return 40 + (90 - days_left) // 3
    if item['category'] == 'electronics':
        return 20
    if item['category'] == 'appliance':
        return 15
    return 10

def recommend_next(item, score_threshold=50):
    item['priority_score'] = priority_score(item)
    return item['priority_score'] >= score_threshold

def sort_by_priority(items):
    return sorted(items, key=lambda x: priority_score(x), reverse=True)
