from typing import Tuple

Color = Tuple[int, int, int]


BLACK: Color = (0, 0, 0)
WHITE: Color = (255, 255, 255)


# color with max intensity for show distances and paths
def get_max_colors() -> Color:
    MAX_DARK = 210
    MAX_BRIGHT = round(MAX_DARK / 2)
    MAX_BRIGHT_INTENSITY = MAX_BRIGHT - 1
    return MAX_DARK, MAX_BRIGHT, MAX_BRIGHT_INTENSITY
