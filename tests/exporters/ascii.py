import io
import unittest
from unittest.mock import patch
from shoze.core.maze import Maze

from shoze.exporters.ascii import AsciiExporter

ROWS = 4
COLUMNS = 4


class AsciiTestCase(unittest.TestCase):
    def test_ascii(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            maze = Maze((ROWS, COLUMNS))
            AsciiExporter().on(maze)
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3
