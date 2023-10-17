from abc import ABCMeta, abstractmethod

from shoze.core.mazes.base import Maze


class AsciiExporter(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def on(maze: Maze) -> None:
        raise NotImplementedError

    @property
    def name(self) -> None:
        return self.__class__.__name__
