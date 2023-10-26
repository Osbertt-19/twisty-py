from abc import ABCMeta, abstractmethod

from twisty.core.grids.grid import Grid


class Algorithm(metaclass=ABCMeta):
    @abstractmethod
    def on(self, grid: Grid) -> None:
        raise NotImplementedError

    @property
    def name(self) -> None:
        return self.__class__.__name__
