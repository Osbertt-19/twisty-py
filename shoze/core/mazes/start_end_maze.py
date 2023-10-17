from typing import List, cast
from shoze.algorithms.base import Algorithm
from shoze.algorithms.binary_tree import BinaryTree
from shoze.core.cell import Cell
from shoze.core.grid import MAX_BRIGHT, MAX_BRIGHT_INTENSITY, MAX_DARK, Grid
from shoze.core.mazes.base import Maze
from shoze.utils.types import Distances, Point
from shoze.utils.colors import Color


class StartEndMaze(Maze):
    def __init__(
        self,
        grid: Point,
        algorithm: Algorithm = BinaryTree(),
        start: Point = None,
        end: Point = None,
    ) -> None:
        super().__init__(grid, algorithm)
        self.start = self.grid[start] if start else self.grid[0, 0]
        if not end:
            row = self.grid.rows - 1
            column = self.grid.columns - 1
            self.end = self.grid[row, column]
        else:
            self.end = self.grid[end]
        self.path: Distances = self._find_path()

    def _find_path(self) -> Distances:
        distances: Distances = self._find_distances()
        current = self.end
        path: Distances = {current: distances[current]}
        while current != self.start:
            for neighbour in current.links:
                neighbour = cast(Cell, neighbour)
                if distances[neighbour] < distances[current]:
                    path[neighbour] = distances[neighbour]
                    current = neighbour
        return path

    def _find_distances(self) -> Distances:
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

    def bg_for_cell(self, cell: Cell) -> Color:
        mx = self.path[self.end]
        distance = self.path[cell]
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
