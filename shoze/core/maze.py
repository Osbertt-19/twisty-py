from time import gmtime, strftime
from shoze.algorithms.binary_tree import BinaryTree
from shoze.algorithms.sidewinder import SideWinder
from shoze.core.exportable import Exportable
from shoze.core.grid import Grid
from shoze.core.types import Algorithms, Point
from shoze.exporters.ascii import Ascii
from shoze.exporters.colors import BLACK, WHITE, Color
from shoze.exporters.png import Png


class Maze(Grid, Exportable):
    def __init__(self, rows: int, columns: int) -> None:
        super().__init__(rows, columns)

    def on(self, algorithm: Algorithms) -> "Maze":
        if algorithm == Algorithms.BINARY_TREE:
            BinaryTree.on(self)
        if algorithm == Algorithms.SIDEWINDER:
            SideWinder.on(self)
        return self
