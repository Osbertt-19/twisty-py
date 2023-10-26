from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from twisty.core.mazes.maze import Maze
else:
    Maze = "Maze"


class Exporter(metaclass=ABCMeta):
    def __init__(self, show_distances: bool, show_path: bool) -> None:
        if show_distances and show_path:
            raise ValueError(
                "Both the distances and the path cannot be displayed at the same time"
            )
        self.show_distances = show_distances
        self.show_path = show_path

    @abstractmethod
    def on(self, maze: Maze) -> None:
        if self.show_distances and not maze.start:
            raise ValueError("Mazes with no start cannot show distances")
        if self.show_path and (not maze.end or not maze.start):
            raise ValueError("Mazes with no start or no end cannot show the path")

    @property
    def name(self):
        return self.__class__.__name__
