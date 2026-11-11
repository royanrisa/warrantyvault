# === Stage 61: Add performance timing for core list and search operations ===
# Project: WarrantyVault
import timeit
from datetime import datetime


def time_warranty_ops(vault, n=100):
    """Benchmark core list and search operations of WarrantyVault."""
    # Ensure a non-empty vault for realistic timing
    if len(vault.items) == 0:
        vault.add_purchase("Test Item", "2024-01-01", "2025-01-01", "Electronics")

    # Time list operations
    list_time = timeit.timeit(lambda: vault.list_all(), number=n)
    print(f"list_all() took {list_time:.4f}s over {n} runs")

    # Time search operations
    search_time = timeit.timeit(lambda: vault.search("Electronics"), number=n)
    print(f"search() took {search_time:.4f}s over {n} runs")

    # Time expiry checks
    expiry_time = timeit.timeit(lambda: vault.get_expired(), number=n)
    print(f"get_expired() took {expiry_time:.4f}s over {n} runs")


if __name__ == "__main__":
    from warranty_vault import WarrantyVault

    vault = WarrantyVault()
    time_warranty_ops(vault)
