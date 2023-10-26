from twisty.core.cell import Cell
from twisty.core.grids.grid import Grid
from twisty.core.masks.mask import Mask


class MaskedGrid(Grid):
    def __init__(self, mask: Mask) -> None:
        self.mask = mask
        super().__init__(self.mask.rows, self.mask.columns)

    def configure_cells(self):
        for cell in self.each_cell():
            row, column = cell.row, cell.column
            if not self.mask[row, column]:
                cell = None
                continue
            cell.north = self[row - 1, column] if self.mask[row - 1, column] else None
            cell.south = self[row + 1, column] if self.mask[row + 1, column] else None
            cell.west = self[row, column - 1] if self.mask[row, column - 1] else None
            cell.east = self[row, column + 1] if self.mask[row, column + 1] else None

    def random_cell(self):
        row, column = self.mask.random_location()
        return self[row, column]
