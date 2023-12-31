from random import choice
from typing import List, Optional, cast
from twisty.algorithms.base import Algorithm
from twisty.core.cell import Cell
from twisty.core.grids.grid import Grid
from twisty.exporters.base import Exporter
from twisty.utils.colors import Color, get_max_colors
from twisty.utils.config import DEFAULT_ALGORITHM, DEFAULT_EXPORTER
from twisty.utils.types import Distances, Point


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
        grid: Grid,
        start: Optional[Point] = None,
        end: Optional[Point] = None,
        algorithm: Algorithm = DEFAULT_ALGORITHM(),
        braid: bool = False,
    ) -> None:
        if not isinstance(algorithm, Algorithm) and algorithm is not None:
            raise ValueError("algorithm must be of type Algorithm ")
        if not isinstance(grid, Grid):
            raise ValueError("grid must be of type Grid")
        self.grid = grid
        if algorithm:
            algorithm.on(self.grid)
        self.algorithm = algorithm

        self.start = self.grid[start] if start else None
        self.end = self.grid[end] if end else None

        self._braid = braid
        if self._braid:
            self.braid()

        self._distances: Distances = self._find_distances() if self.start else None
        self._farthest_cell: Cell = self._find_farthest_cell() if self.start else None

        self._path: Distances = self._find_path() if self.start and self.end else None

    def _find_distances(self) -> Distances:
        distances: Distances = {self.start: 0}
        frontier: List[Cell] = [self.start]
        while len(frontier) > 0:
            new_frontier = []
            for cell in frontier:
                for linked_cell in cell.links:
                    if not linked_cell in distances:
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

    def _find_farthest_cell(self) -> Cell:
        mx = 0
        farthest_cell = self.start
        for cell in self._distances:
            if self._distances[cell] > mx:
                mx = self._distances[cell]
                farthest_cell = cell

        return farthest_cell

    # used in png exporters
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

    @property
    def deadends(self) -> List[Cell]:
        deadends = []
        for cell in self.grid.each_cell():
            if len(cell.links) == 1:
                deadends.append(cell)
        return deadends

    # removing deadends by linking it to one of its neighbours
    def braid(self) -> None:
        for deadend in self.deadends:
            neighbours = deadend.neighbours
            for link in neighbours:
                if link in deadend.links:
                    neighbours.remove(link)
            deadend.link(choice(neighbours))

    def export(self, exporter: Exporter = DEFAULT_EXPORTER()) -> "Maze":
        exporter.on(self)
        return self

    def __json__(self) -> dict:
        return {"grid": self.grid.__json__()}

    def __eq__(self, maze: "Maze") -> bool:
        return self.grid == maze.grid
