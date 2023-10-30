import json
from twisty.core.grids.grid import Grid

from twisty.core.mazes.maze import Maze


def load(file) -> Maze:
    with open(file, "r") as file:
        obj = json.load(file)

    maze = Maze(Grid(obj["grid"]["rows"], obj["grid"]["columns"]), algorithm=None)
    for cell in obj["grid"]["cells"]:
        for link in cell["links"]:
            maze.grid[cell["row"], cell["column"]].link(maze.grid[link[0], link[1]])
    return maze
