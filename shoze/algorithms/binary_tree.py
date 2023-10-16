from random import choice
from shoze.algorithms.base import Algorithm
from shoze.core.grid import Grid


class BinaryTree(Algorithm):
    @staticmethod
    def on(grid: Grid) -> None:
        for cell in grid.each_cell():
            neighbours = []
            if cell.north:
                neighbours.append(cell.north)
            if cell.east:
                neighbours.append(cell.east)
            if len(neighbours) > 0:
                neighbour = choice(neighbours)
                cell.link(neighbour)
