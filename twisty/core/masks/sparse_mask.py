from random import randint
from typing import Dict, List, Tuple
from twisty.core.masks.mask import Mask
from twisty.utils.types import Point

# Random sparse maze
# might make unreachable cells
# cannot use it with start,end and distances,


class SparseMask(Mask):
    def __init__(
        self,
        rows: int,
        columns: int,
        sparse_level: float = 0.3,
        start: Point = None,
        end: Point = None,
    ) -> None:
        super().__init__(rows, columns)
        if not 0 < sparse_level < 1:
            raise ValueError("sparse level must be a floating point between 0 and 1")
        self.start = start if start else (0, 0)
        self.end = end if end else (rows - 1, columns - 1)
        self.sparse_level = sparse_level
        self.sparse()
        self.validate()

    def all_visited(self, visited) -> bool:
        for i in visited:
            for j in i:
                if not j:
                    return False
        return True

    def groups(self) -> Dict[int, Tuple[int, int]]:
        groups: Dict[int, List[Tuple[int, int]]] = {}
        visited: List[List[bool]] = [
            [False for i in range(self.columns)] for j in range(self.rows)
        ]
        group_no: int = 0
        while not self.all_visited(visited):
            group_no += 1
            for i in range(self.rows):
                for j in range(self.columns):
                    if not visited[i][j]:
                        visited[i][j] = True
                        current = (i, j)
            groups[group_no] = [current]
            cells = [current]
            while len(cells) > 0:
                new_cells = []
                for cell in cells:
                    row, column = cell
                    if self[row + 1, column] and not visited[row + 1][column]:
                        new_cells.append((row + 1, column))
                        groups[group_no].append((row + 1, column))

                    if self[row - 1, column] and not visited[row - 1][column]:
                        new_cells.append((row - 1, column))
                        groups[group_no].append((row - 1, column))

                    if self[row, column + 1] and not visited[row][column + 1]:
                        new_cells.append((row, column + 1))
                        groups[group_no].append((row, column + 1))

                    if self[row, column - 1] and not visited[row][column - 1]:
                        new_cells.append((row, column - 1))
                        groups[group_no].append((row, column - 1))
                    if row + 1 < self.rows:
                        visited[row + 1][column] = True
                    if row - 1 >= 0:
                        visited[row - 1][column] = True
                    if column + 1 < self.columns:
                        visited[row][column + 1] = True
                    if column - 1 >= 0:
                        visited[row][column - 1] = True
                cells = new_cells
        return groups

    def validate(self) -> None:
        groups = self.groups()

    def sparse(self) -> None:
        masked_cells: List[Tuple[int, int]] = []
        while self.sparse_level > 0:
            self.sparse_level -= 0.1
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
