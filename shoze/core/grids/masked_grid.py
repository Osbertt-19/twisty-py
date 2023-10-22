from shoze.core.cell import Cell
from shoze.core.grid import Grid
from shoze.core.mask import Mask


class MaskedGrid(Grid):
    def __init__(self, rows: int, columns: int, mask: Mask) -> None:
        self.mask = mask
        super().__init__(rows, columns)

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

    def size(self):
        return self.mask.count()
