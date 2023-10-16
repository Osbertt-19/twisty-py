from abc import ABCMeta, abstractmethod
from typing import Any

from shoze.core.grid import Grid


class Exporter(metaclass=ABCMeta):
    @abstractmethod
    def export(grid: Grid, **kwargs: Any):
        raise NotImplementedError

    @property
    def name(self):
        return self.__class__.__name__
