from random import choice
from typing import Optional, cast
from shoze.algorithms.base import Algorithm
from shoze.core.cell import Cell
from shoze.core.grids.grid import Grid


class HuntAndKill(Algorithm):
    def on(self, grid: Grid) -> None:
        current_cell: Optional[Cell] = grid.random_cell()

        while current_cell is not None:
            unvisited_neighbours = [
                neighbour
                for neighbour in current_cell.neighbours
                if len(neighbour.links) == 0
            ]
            if len(unvisited_neighbours) > 0:
                neighbour = choice(unvisited_neighbours)
                current_cell.link(neighbour)
                current_cell = neighbour
            else:
                current_cell = None

                for cell in grid.each_cell():
                    visited_neighbours = [
                        neighbour
                        for neighbour in cell.neighbours
                        if len(neighbour.links) > 0
                    ]
                    if len(cell.links) == 0 and len(visited_neighbours) > 0:
                        current_cell = cast(Cell, cell)
                        neighbour = choice(visited_neighbours)
                        current_cell.link(neighbour)
                        break
