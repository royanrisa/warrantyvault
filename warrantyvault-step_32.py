# === Stage 32: Add pagination helpers for long console output ===
# Project: WarrantyVault
def paginate(lines, per_page=20):
    """Yield chunks of lines for console paging."""
    import os
    chunk = '\n'.join(lines)
    while True:
        print(chunk, end='')
        chunk = os.read(0, per_page)
        if not chunk:
            break
        if chunk.endswith('\n'):
            break
        chunk += os.read(0, per_page)
