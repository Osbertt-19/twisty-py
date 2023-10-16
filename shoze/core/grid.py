from random import randrange
from typing import List, Optional, Tuple, cast
from shoze.core.cell import Cell
from shoze.core.utils import Point

Key = Tuple[int, int]


class Grid:
    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns

    @property
    def size(self) -> int:
        return self.rows * self.columns

    def __init__(self, rows: int, columns: int) -> None:
        if rows is None or rows < 0:
            raise ValueError("rows must be a positive integer")
        if columns is None or columns < 0:
            raise ValueError("columns must be a positive integer")
        self._rows: int = rows
        self._columns: int = columns
        self._grid: List[List[Cell]] = self.prepare_grid()
        self._show_distances: bool = False
        self.configure_cells()

    def prepare_grid(self):
        return [[Cell(i, j) for j in range(self.columns)] for i in range(self.rows)]

    def configure_cells(self):
        for cell in self.each_cell():
            row, column = cell.row, cell.column
            cell.north = self[row - 1, column]
            cell.south = self[row + 1, column]
            cell.west = self[row, column - 1]
            cell.east = self[row, column + 1]

    def each_row(self):
        for row in range(self.rows):
            yield self._grid[row]

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def cell_at(self, key: Key) -> Optional[Cell]:
        row, column = key
        if not 0 <= row < self.rows:
            return None
        if not 0 <= column < self.columns:
            return None
        return cast(Cell, self._grid[row][column])

    def __getitem__(self, key: Key):
        return self.cell_at(key)

    def random_cell(self):
        row = randrange(0, self.rows)
        column = randrange(0, self.columns)
        cell: Cell = self[row, column]
        return cell

    def show_distances(self, start: Point):
        start = self[start]
        self._show_distances = True
        distances = start.distances
        for cell in self.each_cell():
            cell.content = distances[cell]

    def __repr__(self):
        return f"Grid of {self.rows} rows and {self.columns} columns"
