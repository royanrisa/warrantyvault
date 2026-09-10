# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: WarrantyVault
def dispatch(command: str):
    command = command.strip().lower()
    if command == "help":
        print("Available commands: help, add, show, claim, exit")
    elif command.startswith("add "):
        _add_item(command)
    elif command == "show":
        _show_items()
    elif command == "claim":
        _claim_item()
    elif command == "exit" or command == "quit":
        print("Goodbye!")
        return False
    else:
        print(f"Unknown command: {command}")
    return True
