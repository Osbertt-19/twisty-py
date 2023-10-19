from typing import List, cast
from shoze.algorithms.base import Algorithm
from shoze.algorithms.binary_tree import BinaryTree
from shoze.core.cell import Cell
from shoze.core.mazes.base import Maze
from shoze.utils.types import Distances, Point
from shoze.utils.colors import Color, get_max_colors


class StartMaze(Maze):
    def __init__(
        self, grid: Point, algorithm: Algorithm = BinaryTree(), start: Point = None
    ) -> None:
        super().__init__(grid, algorithm)
        self.start = self.grid[start] if start else self.grid[0, 0]
        self.distances: Distances = self._find_distances()
        self.farthest_cell: Cell = self._find_farthest_cell()

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

    def _find_farthest_cell(self):
        mx = 0
        farthest_cell = self.start
        for cell in self.distances:
            if self.distances[cell] > mx:
                mx = self.distances[cell]
                farthest_cell = cell

        return farthest_cell

    def bg_for_cell(self, cell: Cell) -> Color:
        MAX_DARK, MAX_BRIGHT, MAX_BRIGHT_INTENSITY = get_max_colors()
        mx = self.distances[self.farthest_cell]
        distance = self.distances[cell]
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
