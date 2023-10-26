from shoze.core.masks.mask import Mask
from shoze.utils.config import MASK_LETTER


class TextMask(Mask):
    def __init__(self, textfile) -> None:
        with open(textfile, "r") as file:
            lines = file.read()

        lines = lines.split("\n")
        rows = len(lines)
        columns = len(lines[0])
        super().__init__(rows, columns)

        row = 0
        while row < len(lines):
            column = 0
            while column < len(lines[row]):
                if lines[row][column] == MASK_LETTER:
                    self[row, column] = False
                column += 1
            row += 1
