# === Stage 35: Add active user switching and user-specific records ===
# Project: WarrantyVault
def add_user_switching():
    class User:
        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.warranties = []

        def add_warranty(self, warranty):
            self.warranties.append(warranty)

        def remove_warranty(self, warranty):
            self.warranties.remove(warranty)

        def get_active_warranties(self):
            return [w for w in self.warranties if w.is_active()]

    def switch_user(users, current_user):
        if not users:
            return None
        active_users = [u for u in users if current_user in u.name or current_user in u.email]
        return active_users[0] if active_users else None

    def get_user_records(users, current_user):
        user = switch_user(users, current_user)
        if user:
            return user.warranties
        return []
