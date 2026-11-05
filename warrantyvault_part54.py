# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: WarrantyVault
def colorize(text, color):
    codes = {
        'red': '\033[91m', 'green': '\033[92m', 'yellow': '\033[93m',
        'blue': '\033[94m', 'magenta': '\033[95m', 'cyan': '\033[96m',
        'bold': '\033[1m', 'dim': '\033[2m', 'reset': '\033[0m',
    }
    return f"{codes.get(color, '')}{text}{codes['reset']}"


def use_color():
    if os.environ.get('NO_COLOR'):
        return False
    if os.environ.isatty():
        return True
    return False


class Printer:
    def __init__(self, color=True):
        self.color = color

    def _c(self, text, color):
        return colorize(text, color) if self.color else text

    def header(self, text):
        print(self._c(text, 'bold') + self._c('─' * len(text), 'dim'))

    def ok(self, text):
        print(self._c('✓ ' + text, 'green'))

    def warn(self, text):
        print(self._c('⚠ ' + text, 'yellow'))

    def error(self, text):
        print(self._c('✗ ' + text, 'red'))

    def info(self, text):
        print(self._c('• ' + text, 'cyan'))

    def section(self, text):
        print()
        self.header(text)
