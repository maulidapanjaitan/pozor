# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: ProjectRadar
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"
    DARK_GRAY = "\033[90m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_CYAN = "\033[96m"
    LIGHT_GRAY = "\033[97m"

    @staticmethod
    def set_enabled(enabled):
        Color._enabled = enabled

    @staticmethod
    def is_enabled():
        return Color._enabled if hasattr(Color, '_enabled') else True

    @staticmethod
    def text(text, color=None, bold=False, dim=False, underline=False):
        if not Color.is_enabled():
            return text
        prefix = ""
        if color:
            prefix += getattr(Color, color, "")
        if bold:
            prefix += Color.BOLD
        if dim:
            prefix += Color.DIM
        if underline:
            prefix += Color.UNDERLINE
        return prefix + text + Color.RESET
