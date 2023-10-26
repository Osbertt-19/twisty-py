from random import choice
from typing import List
from twisty.algorithms.base import Algorithm
from twisty.core.cell import Cell
from twisty.core.grids.grid import Grid


class Wilson(Algorithm):
    def on(self, grid: Grid) -> None:
        unvisited: List[Cell] = []
        for cell in grid.each_cell():
            unvisited.append(cell)

        first_cell = choice(unvisited)
        unvisited.remove(first_cell)

        while len(unvisited) > 0:
            cell = choice(unvisited)
            path = [cell]

            while cell in unvisited:
                cell = cell.random_neighbour()
                try:
                    position = path.index(cell)
                    path = path[: position + 1]
                except ValueError:
                    path.append(cell)

            for index in range(len(path) - 1):
                path[index].link(path[index + 1])
                unvisited.remove(path[index])
