import unittest
from twisty.core.grids.grid import Grid

from twisty.core.mazes.maze import Maze
from twisty.json.dump import dump
from twisty.json.load import load

ROWS = 4
COLUMNS = 4


class LoadJsonTestCase(unittest.TestCase):
    def test_load(self) -> None:
        maze = Maze(Grid(ROWS, COLUMNS))
        dump(maze, "test")
        loaded_maze = load("test.json")
        assert maze == loaded_maze
