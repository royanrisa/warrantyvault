# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: WarrantyVault
def dry_run(self):
    """Simulate a mutating command without changing state.
    Returns a dict describing what would happen and the original state."""
    original = {
        'purchases': list(self._purchases),
        'claims': list(self._claims),
        'categories': list(self._categories),
        'expiry_map': dict(self._expiry_map),
    }
    try:
        if self.command == 'add':
            pur = self._parse_purchase()
            self._purchases.append(pur)
            self._expiry_map[pur['id']] = pur['expiry']
            self._categories[pur['category']] = pur['category']
            result = {'action': 'add', 'purchase': pur}
        elif self.command == 'claim':
            pur = self._purchases[0]
            self._claims.append({'purchase_id': pur['id'], 'date': self._now})
            result = {'action': 'claim', 'claim': self._claims[-1]}
        elif self.command == 'category':
            pur = self._purchases[0]
            pur['category'] = self._cat_name
            self._categories[pur['category']] = pur['category']
            result = {'action': 'category', 'purchase': pur}
        elif self.command == 'expiry':
            pur = self._purchases[0]
            pur['expiry'] = self._exp_date
            self._expiry_map[pur['id']] = pur['expiry']
            result = {'action': 'expiry', 'purchase': pur}
        else:
            result = {'error': 'unknown command'}
    except Exception:
        result = {'error': 'validation failed'}
    result['original'] = original
    return result
