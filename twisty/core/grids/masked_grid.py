from twisty.core.cell import Cell
from twisty.core.grids.grid import Grid
from twisty.core.masks.mask import Mask
from twisty.utils.types import Point


class MaskedGrid(Grid):
    def __init__(self, mask: Mask) -> None:
        self.mask = mask
        super().__init__(self.mask.rows, self.mask.columns)

    def configure_cells(self):
        for cell in self.each_cell():
            row, column = cell.row, cell.column
            cell.north = self[row - 1, column] if self.mask[row - 1, column] else None
            cell.south = self[row + 1, column] if self.mask[row + 1, column] else None
            cell.west = self[row, column - 1] if self.mask[row, column - 1] else None
            cell.east = self[row, column + 1] if self.mask[row, column + 1] else None

    def random_cell(self) -> "Cell":
        row, column = self.mask.random_location()
        return self[row, column]

    def kill(self, cell: Cell) -> None:
        self.mask[cell.row, cell.column] = False
        if cell.north:
            cell.north.south = None
            cell.north.unlink(cell)
        if cell.south:
            cell.south.north = None
            cell.south.unlink(cell)
        if cell.east:
            cell.east.west = None
            cell.east.unlink(cell)
        if cell.west:
            cell.west.east = None
            cell.west.unlink(cell)
