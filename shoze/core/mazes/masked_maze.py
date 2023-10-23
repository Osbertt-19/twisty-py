from typing import Optional
from shoze.algorithms.base import Algorithm
from shoze.core.cell import Cell
from shoze.core.grid import Grid
from shoze.core.grids.masked_grid import MaskedGrid
from shoze.core.maze import Maze
from shoze.exporters.ascii_exporters.masked import MaskedAsciiExporter
from shoze.exporters.base import Exporter
from shoze.utils.config import DEFAULT_ALGORITHM, DEFAULT_EXPORTER
from shoze.utils.types import Distances, Point


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

    def export(self, exporter: Exporter = MaskedAsciiExporter()) -> Maze:
        return super().export(exporter)
