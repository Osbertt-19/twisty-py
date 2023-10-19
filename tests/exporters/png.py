import os
import unittest
from shoze.core.maze import Maze
from shoze.exporters.png import PngExporter

ROWS = 4
COLUMNS = 4


class PngTestCase(unittest.TestCase):
    def test_printed_output(self):
        maze = Maze((ROWS, COLUMNS))
        PngExporter(filename="test").on(maze)
        self.assertTrue(os.path.isfile("png/test.png"))

    def tearDown(self) -> None:
        if os.path.isfile("png/test.png"):
            os.remove("png/test.png")
