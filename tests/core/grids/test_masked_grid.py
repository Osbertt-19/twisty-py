import unittest

from twisty.core.grids.masked_grid import MaskedGrid
from twisty.core.masks.mask import Mask

ROWS = 4
COLUMNS = 4


class MaskedGridTestCase(unittest.TestCase):
    def setUp(self) -> None:
        mask = Mask(ROWS, COLUMNS)
        mask[0, 0] = False
        mask[0, 1] = False
        self.grid = MaskedGrid(mask)

    def test_constructor(self) -> None:
        assert self.grid.rows == ROWS
        assert self.grid.columns == COLUMNS

    def test_configure_cells(self) -> None:
        assert self.grid[0, 2].west is None
        assert self.grid[1, 0].north is None
        assert self.grid[1, 1].north is None

    def test_random_cell(self) -> None:
        assert self.grid.random_cell() is not None
