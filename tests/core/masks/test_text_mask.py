import unittest

from twisty.core.masks.mask import Mask
from twisty.core.masks.text_mask import TextMask


class TextMaskTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mask = TextMask("mask.txt")

    def test_constructor_valid_args(self) -> None:
        with open("mask.txt", "r") as file:
            lines = file.read().split("\n")

        assert self.mask.rows == len(lines)
        assert self.mask.columns == len(lines[0])
        assert self.mask.bits == [
            [True, True, False, True],
            [True, True, True, True],
            [False, True, True, True],
            [True, True, True, False],
        ]
