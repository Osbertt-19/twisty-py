from typing import Tuple

from twisty.core.cell import Cell

Color = Tuple[int, int, int]


BLACK: Color = (0, 0, 0)
WHITE: Color = (255, 255, 255)


def get_max_colors():
    MAX_DARK = 210
    MAX_BRIGHT = round(MAX_DARK / 2)
    MAX_BRIGHT_INTENSITY = MAX_BRIGHT - 1
    return MAX_DARK, MAX_BRIGHT, MAX_BRIGHT_INTENSITY
