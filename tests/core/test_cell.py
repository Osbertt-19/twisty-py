import unittest
import warnings

from shoze.core.cell import Cell


class CellTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.cell_1 = Cell(1, 1)
        self.cell_2 = Cell(1, 1)
        self.cell_3 = Cell(1, 2)

    def test_constructor_invalid_args(self) -> None:
        with self.assertRaises(ValueError):
            cell = Cell(-1, 2)
        with self.assertRaises(ValueError):
            cell = Cell(1, -2)
        with self.assertRaises(ValueError):
            cell = Cell(-1, None)
        with self.assertRaises(ValueError):
            cell = Cell(None, -2)

    def test_constructor_valid_args(self) -> None:
        assert self.cell_3.east is None
        assert self.cell_3.west is None
        assert self.cell_3.north is None
        assert self.cell_3.south is None
        assert self.cell_3.row == 1
        assert self.cell_3.column == 2

    def test_equal(self) -> None:
        assert self.cell_1 == self.cell_2

    def test_not_equal(self) -> None:
        assert self.cell_1 != self.cell_3
        assert self.cell_2 != self.cell_3

    def test_link(self) -> None:
        self.assertFalse(self.cell_1.is_linked(self.cell_3))
        self.assertFalse(self.cell_3.is_linked(self.cell_1))

        self.cell_1.link(self.cell_3)

        self.assertTrue(self.cell_1.is_linked(self.cell_3))
        self.assertTrue(self.cell_3.is_linked(self.cell_1))
        self.assertEqual(len(self.cell_1.links), 1)
        self.assertEqual(len(self.cell_3.links), 1)

    def test_link_errors(self) -> None:
        with self.assertRaises(ValueError):
            self.cell_1.link(1)

    def test_unlink(self) -> None:
        self.cell_1.link(self.cell_3)
        self.assertTrue(self.cell_1.is_linked(self.cell_3))
        self.assertTrue(self.cell_3.is_linked(self.cell_1))

        self.cell_1.unlink(self.cell_3)

        self.assertFalse(self.cell_1.is_linked(self.cell_3))
        self.assertFalse(self.cell_3.is_linked(self.cell_1))
        self.assertEqual(len(self.cell_1.links), 0)
        self.assertEqual(len(self.cell_3.links), 0)

    def test_unlink_errors(self) -> None:
        with self.assertRaises(ValueError):
            self.cell_1.unlink(1)
        with warnings.catch_warnings(record=True) as w:
            self.cell_1.unlink(self.cell_3)
            assert len(w) == 1
            assert (
                str(w[0].message)
                == f"Cell({self.cell_1.row},{self.cell_1.column}) and Cell({self.cell_3.row},{self.cell_3.column}) are not linked"
            )
