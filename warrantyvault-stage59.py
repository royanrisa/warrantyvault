# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: WarrantyVault
def bulk_delete(warranty_list, confirm_flag):
    if not confirm_flag:
        return warranty_list
    if not warranty_list:
        return warranty_list
    kept = []
    deleted = 0
    for warranty in warranty_list:
        if warranty.get("deleted"):
            deleted += 1
        else:
            kept.append(warranty)
    if deleted:
        new_list = kept
        return new_list
    return warranty_list


def toggle_delete(warranty_list, index, confirm_flag):
    if not confirm_flag:
        return warranty_list
    if index < 0 or index >= len(warranty_list):
        return warranty_list
    warranty_list[index]["deleted"] = True
    return warranty_list


def finalize_bulk_delete(warranty_list, confirm_flag):
    if not confirm_flag:
        return warranty_list
    new_list = []
    deleted = 0
    for warranty in warranty_list:
        if warranty.get("deleted"):
            deleted += 1
        else:
            new_list.append(warranty)
    return new_list, deleted
