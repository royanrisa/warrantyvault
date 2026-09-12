# === Stage 19: Add undo support for the last simple mutation ===
# Project: WarrantyVault
def undo_last_mutation(self):
    """Revert the most recent add/claim/update/delete by popping from a history stack."""
    if not self._history:
        return
    entry = self._history.pop()
    item = entry['item']
    op = entry['op']
    if op == 'add':
        if item.expiry:
            self._expired.remove(item)
        else:
            self._active.remove(item)
    elif op == 'claim':
        self._claimed.remove(item)
        if item.expiry:
            self._expired.add(item)
        else:
            self._active.add(item)
    elif op == 'update':
        self._active.remove(item)
        item.expiry = entry['old_expiry']
        item.status = entry['old_status']
        if item.expiry:
            self._expired.add(item)
        else:
            self._active.add(item)
    elif op == 'delete':
        self._active.remove(item)
        self._items.append(item)
    else:
        return
    self._items.sort(key=lambda x: x.purchase_date)
    self._active = [x for x in self._items if x.status == 'active']
    self._expired = [x for x in self._items if x.status == 'expired' or (x.expiry and x.expiry < datetime.date.today())]
    self._claimed = [x for x in self._items if x.status == 'claimed']
