import unittest
from twisty.algorithms.sidewinder import SideWinder

from twisty.core.grids.grid import Grid


class SideWinderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.grid = Grid(4, 4)

    def test_alogrithm(self) -> None:
        SideWinder().on(self.grid)
        for cell in self.grid.each_cell():
            assert len(cell.links) > 0
