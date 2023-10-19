from typing import List, Optional, Tuple, cast
from shoze.algorithms.base import Algorithm
from shoze.algorithms.binary_tree import BinaryTree
from shoze.core.cell import Cell

from shoze.core.grid import Grid
from shoze.exporters.ascii import AsciiExporter
from shoze.exporters.base import Exporter
from shoze.utils.colors import Color, get_max_colors
from shoze.utils.types import Distances, Point


class Maze:
    @property
    def distances(self) -> Distances:
        return self._distances

    @property
    def farthest_cell(self) -> Cell:
        return self._farthest_cell

    @property
    def path(self) -> Distances:
        return self._path

    def __init__(
        self,
        grid: Point,
        start: Optional[Point] = None,
        end: Optional[Point] = None,
        algorithm: Algorithm = BinaryTree(),
    ) -> None:
        rows, columns = grid
        if rows < 0 or columns < 0:
            raise ValueError("grid must contain positive integers")

        if not isinstance(algorithm, Algorithm):
            raise ValueError("algorithm must be of type Algorithm ")

        self.grid = Grid(rows, columns)

        algorithm.on(self.grid)
        self.algorithm = algorithm

        self.start = self.grid[start] if start else None
        self.end = self.grid[end] if end else None

        self._distances: Distances = self._find_distances() if self.start else None
        self._farthest_cell: Cell = self._find_farthest_cell() if self.start else None

        self._path: Distances = self._find_path() if self.start and self.end else None

    def _find_distances(self):
        distances: Distances = {self.start: 0}
        frontier: List[Cell] = [self.start]
        while len(frontier) > 0:
            new_frontier = []
            for cell in frontier:
                for linked_cell in cell.links:
                    if not linked_cell in distances.keys():
                        distances[linked_cell] = cast(int, distances[cell]) + 1
                        new_frontier.append(linked_cell)
                frontier = new_frontier
        return distances

    def _find_path(self) -> Distances:
        current = self.end
        path: Distances = {current: self._distances[current]}
        while current != self.start:
            for neighbour in current.links:
                neighbour = cast(Cell, neighbour)
                if self._distances[neighbour] < self._distances[current]:
                    path[neighbour] = self._distances[neighbour]
                    current = neighbour
        return path

    def _find_farthest_cell(self):
        mx = 0
        farthest_cell = self.start
        for cell in self._distances:
            if self._distances[cell] > mx:
                mx = self._distances[cell]
                farthest_cell = cell

        return farthest_cell

    def bg_for_cell(self, cell: Cell) -> Color:
        MAX_DARK, MAX_BRIGHT, MAX_BRIGHT_INTENSITY = get_max_colors()
        mx = self._distances[self._farthest_cell]
        distance = self._distances[cell]
        if distance < mx and distance > 0:
            intensity = (mx - distance) / mx
            dark = round(MAX_DARK * intensity)
            bright = round(MAX_BRIGHT + (MAX_BRIGHT_INTENSITY * intensity))
            color: Color = (dark, bright, dark)
        elif distance == mx:
            color: Color = (128, 0, 0)
        else:
            color: Color = (0, 148, 255)
        return color

    def export(self, exporter: Exporter = AsciiExporter()) -> None:
        exporter.on(self)
