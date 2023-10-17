from typing import Dict
import unittest

from shoze.core.cell import Cell, Distances, is_cell
from shoze.core.maze import Algorithms, Maze


class CellTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cell_1 = Cell(1, 1)
        self.cell_2 = Cell(1, 1)
        self.cell_3 = Cell(1, 2)

    def test_invalid_args(self) -> None:
        with self.assertRaises(ValueError):
            cell = Cell(-1, 2)
        with self.assertRaises(ValueError):
            cell = Cell(1, -2)
        with self.assertRaises(ValueError):
            cell = Cell(-1, None)
        with self.assertRaises(ValueError):
            cell = Cell(None, -2)

    def test_constructor(self) -> None:
        assert self.cell_3.row == 1
        assert self.cell_3.column == 2

    def test_is_cell(self) -> None:
        self.assertTrue(is_cell(self.cell_1))
        self.assertFalse(is_cell(1))

    def test_equal(self) -> None:
        assert self.cell_1 == self.cell_2

    def test_not_equal(self) -> None:
        assert self.cell_1 != self.cell_3
        assert self.cell_2 != self.cell_3

    def test_link(self) -> None:
        self.assertFalse(self.cell_1.is_linked(self.cell_3))
        self.assertFalse(self.cell_3.is_linked(self.cell_1))

        self.cell_1.link(self.cell_3)

        self.assertTrue(self.cell_1.is_linked(self.cell_3))
        self.assertTrue(self.cell_3.is_linked(self.cell_1))
        self.assertEqual(len(self.cell_1.links), 1)
        self.assertEqual(len(self.cell_3.links), 1)

    def test_unlink(self) -> None:
        self.cell_1.link(self.cell_3)
        self.assertTrue(self.cell_1.is_linked(self.cell_3))
        self.assertTrue(self.cell_3.is_linked(self.cell_1))

        self.cell_1.unlink(self.cell_3)

        self.assertFalse(self.cell_1.is_linked(self.cell_3))
        self.assertFalse(self.cell_3.is_linked(self.cell_1))
        self.assertEqual(len(self.cell_1.links), 0)
        self.assertEqual(len(self.cell_3.links), 0)

    def test_distances(self) -> None:
        ROW = 4
        COLUMN = 4
        maze = Maze(ROW, COLUMN).on(Algorithms.BINARY_TREE)
        cell = maze.grid[0, 0]
        distances = cell.distances
        self.assertTrue(isinstance(distances, Dict))
        assert len(distances) == ROW * COLUMN
        assert distances[cell] == 0


if __name__ == "__main__":
    unittest.main()