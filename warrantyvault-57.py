# === Stage 57: Add structured result objects for command handlers ===
# Project: WarrantyVault
class CommandResult:
    def __init__(self, status, data=None, message=None):
        self.status = status
        self.data = data
        self.message = message

    def to_dict(self):
        return {
            "status": self.status,
            "data": self.data,
            "message": self.message,
        }


def result_ok(data=None, message=None):
    return CommandResult("success", data=data, message=message)


def result_error(message=None):
    return CommandResult("error", data=None, message=message)


def result_created(data=None, message=None):
    return CommandResult("created", data=data, message=message)


def result_updated(data=None, message=None):
    return CommandResult("updated", data=data, message=message)


def result_deleted(message=None):
    return CommandResult("deleted", data=None, message=message)


def result_not_found(message="Resource not found"):
    return CommandResult("not_found", data=None, message=message)


def result_conflict(message="Resource already exists"):
    return CommandResult("conflict", data=None, message=message)
