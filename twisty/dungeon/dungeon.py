from random import randint
from typing import List
from twisty.algorithms.base import Algorithm
from twisty.core.grids.masked_grid import MaskedGrid
from twisty.core.masks.sparse_mask import SparseMask
from twisty.core.mazes.masked_maze import MaskedMaze
from twisty.dungeon.room import Room
from twisty.utils.config import DEFAULT_ALGORITHM
from twisty.utils.types import Point


class Dungeon:
    def __init__(self, dimensions: Point, rooms: List[Room]) -> None:
        rows, columns = dimensions
        self.maze = MaskedMaze(MaskedGrid(SparseMask(rows, columns)))

        for room in rooms:
            self.process_room(room)

    def process_room(self, room: Room) -> None:
        row1 = randint(0, self.maze.grid.rows - room.rows)
        column1 = randint(0, self.maze.grid.columns - room.columns)
        row2 = row1 + room.rows
        column2 = column1 + room.columns
        print(row1, row2)
        print(column1, column2)
        for i in range(row1, row2):
            for j in range(column1, column2):
                self.maze.grid.kill(self.maze.grid[i, j])
                self.maze.grid.unkill(self.maze.grid[i, j])

        for i in range(row1, row2):
            for j in range(column1, column2):
                for neighbour in self.maze.grid[i, j].neighbours:
                    if (
                        row1 <= neighbour.row < row2
                        and column1 <= neighbour.column < column2
                    ):
                        self.maze.grid[i, j].link(neighbour)
