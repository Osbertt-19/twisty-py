from typing import cast
import unittest
from twisty.core.cell import Cell
from twisty.core.grids.grid import Grid

ROW = 4
COLUMN = 5


class GridTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.grid = Grid(ROW, COLUMN)

    def test_constructor_invalid_args(self) -> None:
        with self.assertRaises(ValueError) as e:
            grid = Grid(-1, 2)
            assert str(e.exception) == "rows must be a positive integer"

        with self.assertRaises(ValueError) as e:
            grid = Grid(None, 2)
            assert str(e.exception) == "rows must be a positive integer"

        with self.assertRaises(ValueError) as e:
            grid = Grid(1, -2)
            assert str(e.exception) == "columns must be a positive integer"

        with self.assertRaises(ValueError) as e:
            grid = Grid(1, None)
            assert str(e.exception) == "columns must be a positive integer"

    def test_constructor_valid_args(self) -> None:
        assert self.grid.rows == ROW
        assert self.grid.columns == COLUMN

    def test_cell_at(self) -> None:
        cell = cast(Cell, self.grid.cell_at((1, 2)))
        assert cell == Cell(1, 2)

    def test_cell_at_invalid_args(self) -> None:
        cell = self.grid.cell_at((-1, 2))
        assert cell == None
        cell = self.grid.cell_at((1, -2))
        assert cell == None
        cell = self.grid.cell_at((ROW, 2))
        assert cell == None
        cell = self.grid.cell_at((1, COLUMN))
        assert cell == None

    def test_getitem(self) -> None:
        cell = self.grid[1, 2]
        assert cell == Cell(1, 2)

    def test_getitem_invalid_args(self) -> None:
        cell = self.grid[-1, 2]
        assert cell == None
        cell = self.grid[1, -2]
        assert cell == None
        cell = self.grid[ROW, 2]
        assert cell == None
        cell = self.grid[1, COLUMN]
        assert cell == None

    def test_prepare_grid(self) -> None:
        assert len(self.grid._grid) == ROW
        assert len(self.grid._grid[0]) == COLUMN

    def test_configure_cells(self) -> None:
        north_west = cast(Cell, self.grid[0, 0])
        north_east = cast(Cell, self.grid[0, ROW])
        south_west = cast(Cell, self.grid[3, 0])
        south_east = cast(Cell, self.grid[3, ROW])
        middle = cast(Cell, self.grid[2, 3])
        assert len(north_west.neighbours) == 2
        assert len(north_east.neighbours) == 2
        assert len(south_west.neighbours) == 2
        assert len(south_east.neighbours) == 2
        assert len(middle.neighbours) == ROW

    def test_random_cell(self) -> None:
        cell = self.grid.random_cell()
        assert 0 <= cell.row < ROW and 0 <= cell.column < COLUMN
