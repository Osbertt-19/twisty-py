from typing import List
from shoze.utils.types import Key


class Mask:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows: int = rows
        self.columns: int = columns
        self.bits: List[List[bool]] = [
            [True for i in range(self.columns)] for j in range(self.rows)
        ]

    def __getitem__(self, key: Key) -> bool:
        row, column = key
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.bits[row][column]
        else:
            return False

    def __setitem__(self, key: Key, value: bool) -> None:
        row, column = key
        if not (0 <= row < self.rows) or not (0 <= column < self.columns):
            raise ValueError(
                f"Such key doesn't exist. The mask is of {self.rows} rows and {self.columns} columns."
            )
        if not isinstance(value, bool):
            raise ValueError("Setter of Mask object only accepts boolean values")

        self.bits[row][column] = value

    def count(self) -> int:
        count = 0
        for i in self.bits:
            for j in i:
                if j:
                    count += 1
        return count

    def __repr__(self) -> str:
        return str(self.bits)
