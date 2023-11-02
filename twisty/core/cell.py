from random import choice
from typing import Dict, List, Optional


class Cell:
    @property
    def row(self) -> int:
        return self._row

    @property
    def column(self) -> int:
        return self._column

    @property
    def links(self):
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

    def __init__(self, row: int, column: int) -> None:
        if row is None or row < 0:
            raise ValueError("row must be a positive integer")
        if column is None or column < 0:
            raise ValueError("column must be a positive integer")

        self._row: int = row
        self._column: int = column

        self.north: Optional[Cell] = None
        self.south: Optional[Cell] = None
        self.east: Optional[Cell] = None
        self.west: Optional[Cell] = None

        self._links: Dict[Cell, bool] = {}

    def link(self, cell: "Cell", bidirectionally: bool = True) -> None:
        if not isinstance(cell, Cell):
            raise ValueError("Link can only be made between two cells")

        self._links[cell] = True

        if bidirectionally:
            cell.link(self, False)

    def unlink(self, cell: "Cell", bidirectionally: bool = True) -> None:
        if not isinstance(cell, Cell):
            raise ValueError("Unlink can only be made between two cells")

        elif self.is_linked(cell):
            del self._links[cell]
            if bidirectionally:
                cell.unlink(self, False)

    def random_neighbour(self) -> "Cell":
        return choice(self.neighbours)

    def is_linked(self, cell: "Cell") -> bool:
        return cell in self._links

    def __eq__(self, cell: "Cell") -> bool:
        return self.row == cell.row and self.column == cell.column

    def __ne__(self, cell: "Cell") -> bool:
        return not (self.row == cell.row and self.column == cell.column)

    def __hash__(self) -> int:
        return hash((self.row, self.column))

    def __repr__(self) -> str:
        return f"Cell({self.row},{self.column})"

    def __json__(self) -> dict:
        return {
            "row": self.row,
            "column": self.column,
            "links": [(link.row, link.column) for link in self.links],
        }
