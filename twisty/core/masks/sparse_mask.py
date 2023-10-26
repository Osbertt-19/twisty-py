from random import randint
from typing import List, Tuple
from twisty.core.masks.mask import Mask

# SparseMask might make unreachable cells and doesn't work with start point and end point (for now)
# Recommended to use Maze(Grid(ROWS,COLUMNS),sparse = True) instead


class SparseMask(Mask):
    def __init__(self, rows: int, columns: int, sparse_level: float) -> None:
        super().__init__(rows, columns)
        if not 0 < sparse_level < 1:
            raise ValueError("sparse level must be a floating point between 0 and 1")

        self.sparse_level = sparse_level
        masked_cells: List[Tuple[int, int]] = []
        while sparse_level > 0:
            sparse_level -= 0.1
            block_num = 6
            while block_num > 0:
                block_size = randint(1, block_num)
                masked_cells += self.mask_gen(block_size)
                block_num -= block_size
        for row, column in masked_cells:
            self[row, column] = False

    def mask_gen(self, block_size: int) -> List[Tuple[int, int]]:
        cell = (randint(0, self.rows - 1), randint(0, self.columns - 1))
        cells = [cell]
        while block_size > 0:
            block_size -= 1
            cell = self.cell_gen(cell)
            cells.append(cell)
        return cells

    def cell_gen(self, cell: Tuple[int, int]) -> Tuple[int, int]:
        row, column = cell
        while True:
            rand = randint(0, 3)
            match rand:
                case 0:
                    if row - 1 >= 0:
                        return (row - 1, column)  # Go North
                case 1:
                    if row + 1 < self.rows:
                        return (row + 1, column)  # Go South
                case 2:
                    if column - 1 >= 0:
                        return (row, column - 1)  # Go West
                case 3:
                    if column + 1 < self.columns:
                        return (row, column + 1)  # Go East
