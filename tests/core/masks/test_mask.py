import unittest

from shoze.core.masks.mask import Mask

ROWS = 4
COLUMNS = 4


class MaskTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mask = Mask(ROWS, COLUMNS)

    def test_constructor_invalid_args(self) -> None:
        with self.assertRaises(ValueError) as e:
            mask = Mask(-1, 2)
            assert str(e.exception) == "rows must be a positive integer"

        with self.assertRaises(ValueError) as e:
            mask = Mask(None, 2)
            assert str(e.exception) == "rows must be a positive integer"

        with self.assertRaises(ValueError) as e:
            mask = Mask(1, -2)
            assert str(e.exception) == "columns must be a positive integer"

        with self.assertRaises(ValueError) as e:
            mask = Mask(1, None)
            assert str(e.exception) == "columns must be a positive integer"

    def test_constructor_valid_args(self) -> None:
        assert self.mask.rows == ROWS
        assert self.mask.columns == COLUMNS
        assert self.mask.bits == [
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
            [True, True, True, True],
        ]

    def test_getitem(self) -> None:
        assert self.mask[0, 0] == True
        assert self.mask[ROWS, COLUMNS] == False

    def test_setitem(self) -> None:
        assert self.mask[0, 0] == True
        self.mask[0, 0] = False
        assert self.mask[0, 0] == False

    def test_setitem_errors(self) -> None:
        ERROR_MSG = (
            f"Such key doesn't exist. The mask is of {ROWS} rows and {COLUMNS} columns."
        )

        with self.assertRaises(ValueError) as e:
            self.mask[-1, 0] = False
            assert str(e.exception) == ERROR_MSG

        with self.assertRaises(ValueError) as e:
            self.mask[0, -1] = False
            assert str(e.exception) == ERROR_MSG

        with self.assertRaises(ValueError) as e:
            self.mask[ROWS, 0] = False
            assert str(e.exception) == ERROR_MSG

        with self.assertRaises(ValueError) as e:
            self.mask[0, COLUMNS] = False
            assert str(e.exception) == ERROR_MSG

    def test_count(self) -> None:
        assert self.mask.count() == ROWS * COLUMNS
        self.mask[0, 0] = False
        assert self.mask.count() == (ROWS * COLUMNS) - 1
