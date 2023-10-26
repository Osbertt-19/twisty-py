from random import choice
from twisty.algorithms.base import Algorithm
from twisty.core.grids.grid import Grid


class BinaryTree(Algorithm):
    def on(self, grid: Grid) -> None:
        for cell in grid.each_cell():
            neighbours = []
            if cell.north:
                neighbours.append(cell.north)
            if cell.east:
                neighbours.append(cell.east)
            if len(neighbours) > 0:
                neighbour = choice(neighbours)
                cell.link(neighbour)
