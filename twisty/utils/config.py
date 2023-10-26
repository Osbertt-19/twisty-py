from twisty.algorithms.hunt_and_kill import HuntAndKill
from twisty.exporters.ascii.masked_maze import MaskedAsciiExporter
from twisty.exporters.ascii.maze import AsciiExporter


DEFAULT_ALGORITHM = HuntAndKill
DEFAULT_EXPORTER = AsciiExporter
DEFAULT_MASKED_EXPORTER = MaskedAsciiExporter

PNG_OFFSET = 8
MASK_LETTER = "x"
