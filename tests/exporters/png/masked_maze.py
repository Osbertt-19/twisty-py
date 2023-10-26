import os
import unittest
from twisty.core.grids.grid import Grid
from twisty.core.grids.masked_grid import MaskedGrid
from twisty.core.masks.mask import Mask
from twisty.core.mazes.masked_maze import MaskedMaze
from twisty.core.mazes.maze import Maze
from twisty.exporters.png.masked_maze import MaskedPngExporter
from twisty.exporters.png.maze import PngExporter

ROWS = 4
COLUMNS = 4


class MaskedPngTestCase(unittest.TestCase):
    def test_png(self):
        mask = Mask(ROWS, COLUMNS)
        mask[0, 0] = False
        mask[0, 1] = False
        maze = MaskedMaze(MaskedGrid(mask))
        MaskedPngExporter(filename="test").on(maze)
        self.assertTrue(os.path.isfile("images/test.png"))

    def tearDown(self) -> None:
        if os.path.isfile("png/test.png"):
            os.remove("images/test.png")
