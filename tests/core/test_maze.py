import heapq
import unittest
from unittest.mock import MagicMock, patch
from shoze.algorithms.base import Algorithm
from shoze.algorithms.binary_tree import BinaryTree
from shoze.core.grid import Grid

from shoze.core.maze import Maze
from shoze.exporters.ascii import AsciiExporter

ROWS = 4
COLUMNS = 4
START = (0, 0)
END = (ROWS - 1, 0)


class MazeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.maze1 = Maze((ROWS, COLUMNS))
        self.maze2 = Maze((ROWS, COLUMNS), START)
        self.maze3 = Maze((ROWS, COLUMNS), START, END)

    def test_constructor_invalid_args(self) -> None:
        with self.assertRaises(ValueError) as e:
            maze = Maze((-1, 0))
            assert str(e.exception) == "grid must contain positive integers"

        with self.assertRaises(ValueError) as e:
            maze = Maze((ROWS, COLUMNS), algorithm=1)
            assert str(e.exception) == "algorithm must be of type Algorithm "

    def test_constructor(self) -> None:  # no start, no end
        assert isinstance(self.maze3.grid, Grid)
        assert isinstance(self.maze3.algorithm, Algorithm)
        assert self.maze1.start is None
        assert self.maze1.end is None
        assert self.maze1.distances is None
        assert self.maze1.path is None
        assert self.maze1.farthest_cell is None

    def test_constructor_start(self) -> None:  # start, no end
        assert isinstance(self.maze3.grid, Grid)
        assert isinstance(self.maze3.algorithm, Algorithm)
        assert self.maze2.start is not None
        assert self.maze2.end is None
        assert self.maze2.distances is not None
        assert self.maze2.path is None
        assert self.maze2.farthest_cell is not None

    def test_constructor_start_end(self) -> None:  # start, end
        assert isinstance(self.maze3.grid, Grid)
        assert isinstance(self.maze3.algorithm, Algorithm)
        assert self.maze3.start is not None
        assert self.maze3.end is not None
        assert self.maze3.distances is not None
        assert self.maze3.path is not None
        assert self.maze3.farthest_cell is not None

    @patch.object(BinaryTree, "on")
    def test_algorithm(self, mock_algo: MagicMock) -> None:
        maze = Maze((ROWS, COLUMNS))
        mock_algo.assert_called_once_with(maze.grid)

    def test_distances(self) -> None:
        assert len(self.maze2.distances) == self.maze2.grid.size

    def test_farthest_cell(self) -> None:
        for distance in self.maze2.distances.values():
            assert self.maze2.distances[self.maze2.farthest_cell] >= distance

    def test_path(self) -> None:
        path = []
        for cell in self.maze3.path.keys():
            heapq.heappush(path, self.maze3.path[cell])
        for i in range(len(path)):
            assert heapq.heappop(path) == i

    @patch.object(AsciiExporter, "on")
    def test_export(self, mock_export: MagicMock) -> None:
        self.maze1.export()
        mock_export.assert_called_once_with(self.maze1)

    # No test for the function bg_for_cell
