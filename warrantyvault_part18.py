# === Stage 18: Add an activity log with timestamps and action names ===
# Project: WarrantyVault
from datetime import datetime

class ActivityLog:
    def __init__(self):
        self.entries = []
    
    def log(self, action: str, details: str = ""):
        self.entries.append({
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details
        })
        return self.entries[-1]
