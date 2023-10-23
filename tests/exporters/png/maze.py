import os
import unittest
from shoze.core.grids.grid import Grid
from shoze.core.mazes.maze import Maze
from shoze.exporters.png.maze import PngExporter

ROWS = 4
COLUMNS = 4


class PngTestCase(unittest.TestCase):
    def test_png(self):
        maze = Maze(Grid(ROWS, COLUMNS))
        PngExporter(filename="test").on(maze)
        self.assertTrue(os.path.isfile("images/test.png"))

    def tearDown(self) -> None:
        if os.path.isfile("png/test.png"):
            os.remove("images/test.png")
