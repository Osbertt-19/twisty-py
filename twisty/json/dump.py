import json
from time import gmtime, strftime
from twisty.core.mazes.maze import Maze


def dump(
    maze: Maze,
    filename: str = strftime("%Y-%m-%d-%H-%M-%S", gmtime()),
    filepath: str = None,
) -> None:
    path = filepath if filepath else f"{filename}.json"
    with open(path, "w") as file:
        json.dump(maze.__json__(), file)
