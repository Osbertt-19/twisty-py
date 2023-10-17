from random import randrange
from typing import List, Optional, Tuple, cast
from shoze.core.cell import Cell
from shoze.core.types import Key

from shoze.core.types import Point
from shoze.exporters.colors import Color


MAX_DARK = 210  # Dark meaning farther than or more distant than
MAX_BRIGHT = round(
    MAX_DARK / 2
)  # And thus, bright means closer than or less distant than
MAX_BRIGHT_INTENSITY = MAX_BRIGHT - 1


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
        self.show_distances_flag: bool = False
        self.solved_flag: bool = False
        self.start: Optional[Cell] = None
        self.end: Optional[Cell] = None
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

    def show_distances(self, start: Point) -> None:
        if not self.show_distances_flag:
            self.show_distances_flag = True
            self.start = self[start]
            for cell in self.each_cell():
                cell.content = self.start.distances[cell]

    def not_show_distances(self) -> None:
        if self.show_distances_flag:
            self.show_distances_flag = False
            self.start = None
            for cell in self.each_cell():
                cell.content = None

    def solve(self, start: Point, end: Point):
        self.show_distances(start)
        if not self.show_distances_flag:
            self.show_distances()
        self.start = self[start]
        self.end = self[end]
        current = self[end]
        breadcrumbs: List[Cell] = [current]
        while current != Cell(start[0], start[1]):
            for neighbour in current.links:
                neighbour = cast(Cell, neighbour)
                if neighbour.content < current.content:
                    breadcrumbs.append(neighbour)
                    current = neighbour
        for cell in self.each_cell():
            if not cell in breadcrumbs:
                cell.content = None
                self.start.distances[cell] = None
        self.solved_flag = True

    def bg_for_cell(self, cell: Cell) -> Color:
        mx = self.start.longest_path
        distance = self.start.distances[cell]
        if distance < mx and distance > 0:
            intensity = (mx - distance) / mx
            dark = round(MAX_DARK * intensity)
            bright = round(MAX_BRIGHT + (MAX_BRIGHT_INTENSITY * intensity))
            color: Color = (dark, bright, dark)
        elif distance == mx:
            color: Color = (128, 0, 0)
        else:
            color: Color = (0, 148, 255)
        return color

    def __repr__(self):
        return f"Grid of {self.rows} rows and {self.columns} columns"
