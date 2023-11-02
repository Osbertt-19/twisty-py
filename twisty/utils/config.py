from twisty.algorithms.base import Algorithm
from twisty.algorithms.hunt_and_kill import HuntAndKill
from twisty.exporters.ascii.masked_maze import MaskedAsciiExporter
from twisty.exporters.ascii.maze import AsciiExporter
from twisty.exporters.base import Exporter


DEFAULT_ALGORITHM: Algorithm = HuntAndKill
DEFAULT_EXPORTER: Exporter = AsciiExporter
DEFAULT_MASKED_EXPORTER: Exporter = MaskedAsciiExporter

PNG_OFFSET: int = 8
MASK_LETTER: str = "x"
PNG_FOLDER: str = "images"
