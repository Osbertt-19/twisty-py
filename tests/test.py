import unittest

from tests.core.test_cell import CellTestCase
from tests.core.test_grid import GridShowDistancesTestCase, GridTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTests(CellTestCase, GridTestCase, GridShowDistancesTestCase)
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())


# python3 -m unittest -v tests/test.py
