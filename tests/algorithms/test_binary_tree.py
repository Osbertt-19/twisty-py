import unittest
from shoze.algorithms.binary_tree import BinaryTree

from shoze.core.grid import Grid


class BinaryTreeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.grid = Grid(4, 4)

    def test_alogrithm(self) -> None:
        BinaryTree().on(self.grid)
        for cell in self.grid.each_cell():
            assert len(cell.links) > 0
