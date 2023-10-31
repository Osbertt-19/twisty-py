import unittest
from tests.algorithms.test_binary_tree import BinaryTreeTestCase
from tests.algorithms.test_sidewinder import SideWinderTestCase
from tests.core.grids.test_masked_grid import MaskedGridTestCase
from tests.core.masks.test_text_mask import TextMaskTestCase
from tests.core.mazes.test_masked_maze import MaskedMazeTestCase
from tests.core.test_cell import CellTestCase
from tests.core.grids.test_grid import GridTestCase
from tests.core.masks.test_mask import MaskTestCase
from tests.core.mazes.test_maze import MazeTestCase
from tests.exporters.ascii.masked_maze import MaskedAsciiTestCase
from tests.exporters.ascii.maze import AsciiTestCase
from tests.exporters.png.masked_maze import MaskedPngTestCase
from tests.exporters.png.maze import PngTestCase
from tests.goals import GoalsTestCase
from tests.json.test_dump import DumpJsonTestCase
from tests.json.test_load import LoadJsonTestCase


def core_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTests(
        CellTestCase,
        GridTestCase,
        MazeTestCase,
        MaskTestCase,
        TextMaskTestCase,
        MaskedGridTestCase,
        MaskedMazeTestCase,
    )
    return suite


def algorithms_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTests(BinaryTreeTestCase, SideWinderTestCase)
    return suite


def exporter_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTests(AsciiTestCase, PngTestCase, MaskedAsciiTestCase, MaskedPngTestCase)
    return suite


def json_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTests(DumpJsonTestCase, LoadJsonTestCase)
    return suite


def goals_suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    suite.addTests(GoalsTestCase)


if __name__ == "__main__":
    unittest.TextTestRunner().run(core_suite())
    unittest.TextTestRunner().run(algorithms_suite())
    unittest.TextTestRunner().run(exporter_suite())
    unittest.TextTestRunner().run(goals_suite())
    unittest.TextTestRunner().run(json_suite())


# python3 -m unittest -v tests/test.py
# python3 -m unittest tests/test.py
