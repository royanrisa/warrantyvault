# === Stage 31: Add compact table rendering for long lists ===
# Project: WarrantyVault
def render_compact_table(headers, rows, max_rows=30):
    """Render a long list as a scrollable compact table."""
    if not rows:
        return f"{' | '.join(str(h) for h in headers)}\nNo data."
    visible = rows[:max_rows]
    total = len(rows)
    lines = [f"{' | '.join(str(h) for h in headers)}"]
    for r in visible:
        lines.append(' | '.join(str(cell) for cell in r))
    if total > max_rows:
        lines.append(f"\n... {total - max_rows} more rows. Increase max_rows to see all.")
    return '\n'.join(lines)
