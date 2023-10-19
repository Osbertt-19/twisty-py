from abc import ABCMeta
from typing import Optional
from shoze.algorithms.base import Algorithm
from shoze.algorithms.binary_tree import BinaryTree
from shoze.algorithms.sidewinder import SideWinder

from shoze.core.grid import Grid
from shoze.utils.types import Point


class Maze(metaclass=ABCMeta):
    def __init__(
        self,
        grid: Point,
        algorithm: Algorithm,
    ) -> None:
        rows, columns = grid
        self.grid = Grid(rows, columns)
        self.algorithm = algorithm
        algorithm.on(self.grid)

    @property
    def name(self) -> None:
        return self.__class__.__name__
