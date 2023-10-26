import io
import unittest
from unittest.mock import patch
from shoze.core.grids.masked_grid import MaskedGrid
from shoze.core.masks.mask import Mask

from shoze.core.mazes.masked_maze import MaskedMaze
from shoze.exporters.ascii.masked_maze import MaskedAsciiExporter

ROWS = 4
COLUMNS = 4


class MaskedAsciiTestCase(unittest.TestCase):
    def test_ascii(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mask = Mask(ROWS, COLUMNS)
            mask[0, 0] = False
            mask[0, 1] = False
            maze = MaskedMaze(MaskedGrid(mask))
            MaskedAsciiExporter().on(maze)
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3
