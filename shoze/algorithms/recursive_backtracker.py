from random import choice
from typing import List, Optional
from shoze.algorithms.base import Algorithm
from shoze.core.cell import Cell
from shoze.core.grids.grid import Grid


class RecursiveBacktracker(Algorithm):
    def __init__(self, starting_cell: Optional[Cell] = None) -> None:
        self.starting_cell = starting_cell

    def on(self, grid: Grid) -> None:
        if self.starting_cell is None:
            self.starting_cell = grid.random_cell()
        if not isinstance(self.starting_cell, Cell):
            ValueError(
                "Starting point of the algorithm must be a valid cell in the grid"
            )

        walked_path: List[Cell] = []
        walked_path.append(self.starting_cell)

        while walked_path:
            current_cell = walked_path[-1]

            unvisited_neighbours = [
                neighbour
                for neighbour in current_cell.neighbours
                if not neighbour.links
            ]
            if not unvisited_neighbours:
                walked_path.pop()
            else:
                neighbour = choice(unvisited_neighbours)
                current_cell.link(neighbour)
                walked_path.append(neighbour)
