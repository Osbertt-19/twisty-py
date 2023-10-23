import heapq
import unittest
from unittest.mock import MagicMock, patch
from shoze.algorithms.base import Algorithm
from shoze.algorithms.binary_tree import BinaryTree
from shoze.core.grids.grid import Grid

from shoze.core.mazes.maze import Maze
from shoze.utils.config import DEFAULT_ALGORITHM, DEFAULT_EXPORTER

ROWS = 4
COLUMNS = 4
START = (0, 0)
END = (ROWS - 1, 0)


class MazeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.maze1 = Maze(Grid(ROWS, COLUMNS))
        self.maze2 = Maze(Grid(ROWS, COLUMNS), START)
        self.maze3 = Maze(Grid(ROWS, COLUMNS), START, END)

    def test_constructor_invalid_args(self) -> None:
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

    @patch.object(DEFAULT_ALGORITHM, "on")
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

    def test_deadends(self) -> None:
        for cell in self.maze1.deadends:
            assert len(cell.links) == 1

    @patch.object(DEFAULT_EXPORTER, "on")
    def test_export(self, mock_export: MagicMock) -> None:
        self.maze1.export()
        mock_export.assert_called_once_with(self.maze1)

    # No test for the function bg_for_cell
