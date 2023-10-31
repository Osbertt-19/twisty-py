import os
import unittest
from twisty.core.grids.grid import Grid

from twisty.core.mazes.maze import Maze
from twisty.json.dump import dump

ROWS = 4
COLUMNS = 4


class DumpJsonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.maze = Maze(Grid(ROWS, COLUMNS))

    def test_dump_filename(self) -> None:
        dump(self.maze, "test")

    def test_file_path(self) -> None:
        dump(self.maze, filepath="test.json")

    def tearDown(self) -> None:
        if os.path.isfile("test.json"):
            os.remove("test.json")
