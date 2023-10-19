import unittest
from tests.algorithms.test_binary_tree import BinaryTreeTestCase
from tests.algorithms.test_sidewinder import SideWinderTestCase
from tests.core.test_cell import CellTestCase
from tests.core.test_grid import GridTestCase


def core_suite():
    suite = unittest.TestSuite()
    suite.addTests(CellTestCase, GridTestCase)
    return suite


def algorithms_suite():
    suite = unittest.TestSuite()
    suite.addTests(BinaryTreeTestCase, SideWinderTestCase)
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(core_suite())
    unittest.TextTestRunner().run(algorithms_suite())

# python3 -m unittest -v tests/test.py
