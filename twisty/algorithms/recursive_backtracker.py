from random import choice
from typing import List, Optional
from twisty.algorithms.base import Algorithm
from twisty.core.cell import Cell
from twisty.core.grids.grid import Grid


class RecursiveBacktracker(Algorithm):
    def __init__(self, starting_cell: Optional[Cell] = None) -> None:
        self.starting_cell = starting_cell

    def on(self, grid: Grid) -> None:
        if self.starting_cell is None:
            self.starting_cell = grid.random_cell()

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
