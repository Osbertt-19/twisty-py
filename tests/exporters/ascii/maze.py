import io
import unittest
from unittest.mock import patch
from twisty.core.grids.grid import Grid
from twisty.core.mazes.maze import Maze
from twisty.exporters.ascii.maze import AsciiExporter


ROWS = 4
COLUMNS = 4


class AsciiTestCase(unittest.TestCase):
    def test_ascii(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            maze = Maze(Grid(ROWS, COLUMNS))
            AsciiExporter().on(maze)
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3
