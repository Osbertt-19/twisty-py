import unittest
from tests.algorithms.test_binary_tree import BinaryTreeTestCase
from tests.algorithms.test_sidewinder import SideWinderTestCase
from tests.core.grids.test_masked_grid import MaskedGridTestCase
from tests.core.test_cell import CellTestCase
from tests.core.grids.test_grid import GridTestCase
from tests.core.test_mask import MaskTestCase
from tests.core.mazes.test_maze import MazeTestCase
from tests.exporters.ascii.maze import AsciiTestCase
from tests.exporters.png.maze import PngTestCase


def core_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTests(
        CellTestCase, GridTestCase, MazeTestCase, MaskTestCase, MaskedGridTestCase
    )
    return suite


def algorithms_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTests(BinaryTreeTestCase, SideWinderTestCase)
    return suite


def exporter_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTests(AsciiTestCase, PngTestCase)
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(core_suite())
    unittest.TextTestRunner().run(algorithms_suite())
    unittest.TextTestRunner().run(exporter_suite())


# python3 -m unittest -v tests/test.py
# python3 -m unittest tests/test.py
