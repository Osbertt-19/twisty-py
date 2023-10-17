from abc import ABCMeta
from typing import Optional
from shoze.algorithms.base import Algorithm
from shoze.algorithms.binary_tree import BinaryTree
from shoze.algorithms.sidewinder import SideWinder

from shoze.core.grid import Grid


class Maze(metaclass=ABCMeta):
    def __init__(
        self,
        grid: Grid,
        algorithm: Algorithm,
    ) -> None:
        self.grid = grid
        self.algorithm = algorithm

        if isinstance(self.algorithm, BinaryTree):
            BinaryTree.on(self.grid)
        elif isinstance(self.algorithm, SideWinder):
            SideWinder.on(self.grid)

    @property
    def name(self) -> None:
        return self.__class__.__name__
