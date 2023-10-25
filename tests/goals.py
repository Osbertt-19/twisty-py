import io
import os
import unittest
from unittest.mock import patch
from shoze.core.grids.grid import Grid
from shoze.core.grids.masked_grid import MaskedGrid
from shoze.core.mask import Mask
from shoze.core.mazes.masked_maze import MaskedMaze

from shoze.core.mazes.maze import Maze
from shoze.exporters.ascii.masked_maze import MaskedAsciiExporter
from shoze.exporters.ascii.maze import AsciiExporter
from shoze.exporters.png.masked_maze import MaskedPngExporter
from shoze.exporters.png.maze import PngExporter

ROWS = 4
COLUMNS = 4


class GoalsTestCase(unittest.TestCase):
    def tearDown(self) -> None:
        if os.path.isfile("png/test.png"):
            os.remove("png/test.png")

    def test_1(self) -> None:
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            Maze(Grid(ROWS, COLUMNS)).export()
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3

    def test_2(self) -> None:
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            Maze(Grid(ROWS, COLUMNS), (0, 0)).export(AsciiExporter(show_distances=True))
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3

    def test_3(self) -> None:
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            Maze(Grid(ROWS, COLUMNS), (0, 0), (ROWS - 1, 0)).export(
                AsciiExporter(show_path=True)
            )
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3

    def test_4(self):
        Maze(Grid(ROWS, COLUMNS)).export(PngExporter(filename="test"))
        self.assertTrue(os.path.isfile("images/test.png"))

    def test_5(self):
        Maze(Grid(ROWS, COLUMNS), (0, 0)).export(
            PngExporter(filename="test", show_distances=True)
        )
        self.assertTrue(os.path.isfile("images/test.png"))

    def test_6(self):
        Maze(Grid(ROWS, COLUMNS), (0, 0), (ROWS - 1, 0)).export(
            PngExporter(filename="test", show_path=True)
        )
        self.assertTrue(os.path.isfile("images/test.png"))

    def test_7(self) -> None:
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mask = Mask(ROWS, COLUMNS)
            mask[0, 0] = False
            mask[0, 1] = False
            MaskedMaze(MaskedGrid(mask)).export()
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3

    def test_8(self) -> None:
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mask = Mask(ROWS, COLUMNS)
            mask[0, 0] = False
            mask[0, 1] = False
            MaskedMaze(MaskedGrid(mask), (0, 2)).export(
                MaskedAsciiExporter(show_distances=True)
            )
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3

    def test_9(self) -> None:
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mask = Mask(ROWS, COLUMNS)
            mask[0, 0] = False
            mask[0, 1] = False
            MaskedMaze(MaskedGrid(mask), (0, 2), (ROWS - 1, 0)).export(
                MaskedAsciiExporter(show_path=True)
            )
            output: str = mock_stdout.getvalue()
            assert len(output.split("\n")) == ROWS + ROWS + 3

    def test_10(self) -> None:
        mask = Mask(ROWS, COLUMNS)
        mask[0, 0] = False
        mask[0, 1] = False
        MaskedMaze(MaskedGrid(mask)).export(MaskedPngExporter(filename="test"))
        self.assertTrue(os.path.isfile("images/test.png"))

    def test_11(self) -> None:
        mask = Mask(ROWS, COLUMNS)
        mask[0, 0] = False
        mask[0, 1] = False
        MaskedMaze(MaskedGrid(mask), (0, 2)).export(
            MaskedPngExporter(filename="test", show_distances=True)
        )
        self.assertTrue(os.path.isfile("images/test.png"))

    def test_12(self) -> None:
        mask = Mask(ROWS, COLUMNS)
        mask[0, 0] = False
        mask[0, 1] = False
        MaskedMaze(MaskedGrid(mask), (0, 2), (ROWS - 1, 0)).export(
            MaskedPngExporter(filename="test", show_path=True)
        )
        self.assertTrue(os.path.isfile("images/test.png"))
