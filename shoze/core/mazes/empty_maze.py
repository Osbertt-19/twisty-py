from time import gmtime, strftime
from shoze.algorithms.base import Algorithm
from shoze.algorithms.binary_tree import BinaryTree
from shoze.algorithms.sidewinder import SideWinder
from shoze.core.grid import Grid
from shoze.core.mazes.base import Maze


class EmptyMaze(Maze):
    def __init__(self, grid: Grid, algorithm: Algorithm = BinaryTree()) -> None:
        super().__init__(grid, algorithm)
