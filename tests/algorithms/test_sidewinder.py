import unittest
from shoze.algorithms.sidewinder import SideWinder

from shoze.core.grid import Grid


class SideWinderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.grid = Grid(4, 4)

    def test_alogrithm(self) -> None:
        SideWinder().on(self.grid)
        for cell in self.grid.each_cell():
            assert len(cell.neighbours) > 0
