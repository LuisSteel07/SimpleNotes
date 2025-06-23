from enum import Enum


class Colors(Enum):
    RED = "#8B0000"
    BLUE = "#00008B"
    YELLOW = "#CCCC00"  # Una versión más opaca, ya que el amarillo puro es difícil de oscurecer
    GREEN = "#006400"
    VIOLET = "#4B0082"
    ORANGE = "#CC8400"
    PINK = "#C71585"

list_colors_code = [Colors.RED, Colors.BLUE, Colors.YELLOW, Colors.GREEN, Colors.VIOLET, Colors.ORANGE, Colors.PINK]