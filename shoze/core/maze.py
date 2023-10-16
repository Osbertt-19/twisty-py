from enum import Enum
from time import gmtime, strftime
from shoze.algorithms.binary_tree import BinaryTree
from shoze.algorithms.sidewinder import SideWinder
from shoze.core.cell import Cell
from shoze.core.grid import Grid
from shoze.core.utils import Point
from shoze.exporters.ascii import Ascii
from shoze.exporters.colors import BLACK, WHITE, Color
from shoze.exporters.png import Png


class Algorithms(Enum):
    BINARY_TREE = 1
    SIDEWINDER = 2


class Maze:
    def __init__(self, rows: int, columns: int) -> None:
        self.grid = Grid(rows, columns)

    def on(self, algorithm: Algorithms) -> "Maze":
        if algorithm == Algorithms.BINARY_TREE:
            BinaryTree.on(self.grid)
        if algorithm == Algorithms.SIDEWINDER:
            SideWinder.on(self.grid)
        return self

    def show_distances(self, start: Point) -> "Maze":
        self.grid.show_distances(start)
        return self

    def display_ascii(self) -> "Maze":
        Ascii.export(self.grid)
        return self

    def save_png(
        self,
        filename: str = strftime("%Y-%m-%d-%H-%M-%S", gmtime()),
        cell_size: int = 30,
        wall_color: Color = BLACK,
        wall_width: int = 1,
        background_color: Color = WHITE,
    ) -> "Maze":
        Png.export(
            self.grid, filename, cell_size, wall_color, wall_width, background_color
        )
        return self
