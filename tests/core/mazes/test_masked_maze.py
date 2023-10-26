import unittest
from unittest.mock import MagicMock, patch
from shoze.core.grids.masked_grid import MaskedGrid
from shoze.core.masks.mask import Mask

from shoze.core.mazes.masked_maze import MaskedMaze
from shoze.utils.config import DEFAULT_MASKED_EXPORTER

ROWS = 4
COLUMNS = 4


class MaskedMazeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        mask = Mask(ROWS, COLUMNS)
        mask[0, 0] = False
        mask[0, 1] = False
        self.maze = MaskedMaze(MaskedGrid(mask))

    def test_constructor(self) -> None:
        assert isinstance(self.maze.grid, MaskedGrid)

    @patch.object(DEFAULT_MASKED_EXPORTER, "on")
    def test_export(self, mock_export: MagicMock) -> None:
        self.maze.export()
        mock_export.assert_called_once_with(self.maze)
