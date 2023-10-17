from time import gmtime, strftime
from shoze.exporters.ascii import Ascii
from shoze.exporters.colors import BLACK, WHITE, Color
from shoze.exporters.png import Png


class Exportable:
    def display_ascii(self):
        Ascii.export(self)
        return self

    def save_png(
        self,
        filename: str = strftime("%Y-%m-%d-%H-%M-%S", gmtime()),
        cell_size: int = 30,
        wall_color: Color = BLACK,
        wall_width: int = 1,
        background_color: Color = WHITE,
    ):
        Png.export(self, filename, cell_size, wall_color, wall_width, background_color)
        return self
