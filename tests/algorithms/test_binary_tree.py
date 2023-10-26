import unittest
from twisty.algorithms.binary_tree import BinaryTree

from twisty.core.grids.grid import Grid


class BinaryTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.grid = Grid(4, 4)

    def test_alogrithm(self) -> None:
        BinaryTree().on(self.grid)
        for cell in self.grid.each_cell():
            assert len(cell.links) > 0
