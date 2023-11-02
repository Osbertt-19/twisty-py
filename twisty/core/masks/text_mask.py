from twisty.core.masks.mask import Mask
from twisty.utils.config import MASK_LETTER


class TextMask(Mask):
    def __init__(self, textfile: str) -> None:
        with open(textfile, "r") as file:
            lines = file.read()

        lines = lines.split("\n")
        rows = len(lines)
        columns = len(lines[0])

        super().__init__(rows, columns)

        # Set False to mask[cell] if text[cell] is MASK_LETTER
        for row in range(len(lines)):
            for column in range(len(lines[row])):
                if lines[row][column] == MASK_LETTER:
                    self[row, column] = False
