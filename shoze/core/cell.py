from typing import Dict, List, Optional, cast
from shoze.core.types import Distances


class Cell:
    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._column

    @property
    def links(self) -> "Cell":
        return self._links.keys()

    @property
    def neighbours(self) -> List["Cell"]:
        neighbours = []
        if self.north:
            neighbours.append(self.north)
        if self.south:
            neighbours.append(self.south)
        if self.east:
            neighbours.append(self.east)
        if self.west:
            neighbours.append(self.west)
        return neighbours

    @property
    def distances(self) -> Distances:
        if not self._distances:
            self.find_distances()
        return self._distances

    def find_distances(self) -> None:
        distances: Distances = {self: 0}
        frontier: List[Cell] = [self]
        while len(frontier) > 0:
            new_frontier = []
            for cell in frontier:
                for linked_cell in cell.links:
                    if not linked_cell in distances.keys():
                        distances[linked_cell] = cast(int, distances[cell]) + 1
                        new_frontier.append(linked_cell)
                        self._longest_path = distances[linked_cell]
                frontier = new_frontier
        self._distances = distances

    @property
    def longest_path(self) -> Optional[int]:
        return self._longest_path

    def __init__(self, row: int, column: int) -> None:
        if row is None or row < 0:
            raise ValueError("Row must be a positive integer")
        if column is None or column < 0:
            raise ValueError("Column must be a positive integer")

        self._row: int = row
        self._column: int = column
        self.content: Optional[int] = None
        self.north: Optional[Cell] = None
        self.south: Optional[Cell] = None
        self.east: Optional[Cell] = None
        self.west: Optional[Cell] = None
        self._distances: Optional[Distances] = None
        self._links: Dict[Cell, bool] = {}
        self._longest_path: Optional[int] = None

    def link(self, cell: "Cell", bidirectionally: bool = True):
        self._links[cell] = True
        if bidirectionally:
            cell.link(self, False)

    def unlink(self, cell: "Cell", bidirectionally: bool = True):
        del self._links[cell]
        if bidirectionally:
            cell.unlink(self, False)

    def is_linked(self, cell: "Cell"):
        return cell in self._links

    def __eq__(self, cell: "Cell"):
        return self.row == cell.row and self.column == cell.column

    def __ne__(self, cell: "Cell"):
        return not (self.row == cell.row and self.column == cell.column)

    def __hash__(self) -> int:
        return hash((self.row, self.column))

    def __repr__(self):
        return f"Cell {self.row},{self.column}: \n"


def is_cell(cell: "Cell") -> bool:
    return isinstance(cell, Cell)
