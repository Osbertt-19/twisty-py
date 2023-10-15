import unittest

from tests.models.test_cell import CellTestCase
from tests.models.test_grid import GridTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTests(CellTestCase, GridTestCase)
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
