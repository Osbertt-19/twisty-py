from typing import Dict
import unittest

from shoze.core.cell import Cell, Distances, is_cell
from shoze.core.maze import Algorithms, Maze


class CellTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cell_1 = Cell(1, 1)
        self.cell_2 = Cell(1, 1)
        self.cell_3 = Cell(1, 2)
        ROW = 4
        COLUMN = 4
        self.maze = Maze(ROW, COLUMN).on(Algorithms.BINARY_TREE)

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

    def test_initial_distances(self) -> None:
        cell = self.maze[0, 0]
        assert cell._distances is None

    def test_find_distances(self) -> None:
        cell = self.maze[0, 0]
        cell.find_distances()
        assert cell._distances is not None
        assert isinstance(cell._distances, dict)
        assert len(cell._distances) == self.maze.size

    def test_longest_path(self) -> None:
        cell = self.maze[0, 0]
        assert cell.longest_path is None

        cell.find_distances()
        assert isinstance(cell.longest_path, int)

    def test_distances(self) -> None:
        cell = self.maze[0, 0]
        distances = cell.distances
        assert distances is not None
        assert isinstance(distances, dict)
        assert len(distances) == self.maze.size
