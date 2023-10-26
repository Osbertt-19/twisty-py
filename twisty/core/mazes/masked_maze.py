from typing import Optional
from twisty.algorithms.base import Algorithm
from twisty.core.cell import Cell
from twisty.core.grids.grid import Grid
from twisty.core.grids.masked_grid import MaskedGrid
from twisty.core.mazes.maze import Maze
from twisty.exporters.ascii.masked_maze import MaskedAsciiExporter
from twisty.exporters.base import Exporter
from twisty.utils.config import (
    DEFAULT_ALGORITHM,
    DEFAULT_EXPORTER,
    DEFAULT_MASKED_EXPORTER,
)
from twisty.utils.types import Distances, Point


class MaskedMaze(Maze):
    def __init__(
        self,
        grid: MaskedGrid,
        start: Point | None = None,
        end: Point | None = None,
        algorithm: Algorithm = DEFAULT_ALGORITHM(),
    ) -> None:
        if not isinstance(grid, MaskedGrid):
            raise ValueError("grid must be of MaskedGrid")

        if not isinstance(algorithm, Algorithm):
            raise ValueError("algorithm must be of type Algorithm ")

        if start and not grid.mask[start]:
            raise ValueError("start point cannot point to a masked cell")

        if end and not grid.mask[end]:
            raise ValueError("end point cannot point to a masked cell")
        self.grid = grid

        algorithm.on(self.grid)
        self.algorithm = algorithm

        self.start = self.grid[start] if start else None
        self.end = self.grid[end] if end else None

        self._distances: Distances = self._find_distances() if self.start else None
        self._farthest_cell: Cell = self._find_farthest_cell() if self.start else None

        self._path: Distances = self._find_path() if self.start and self.end else None

    def export(self, exporter: Exporter = DEFAULT_MASKED_EXPORTER()) -> Maze:
        return super().export(exporter)
