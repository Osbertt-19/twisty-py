from shoze.core.grids.masked_grid import MaskedGrid
from shoze.core.masks.mask import Mask
from shoze.core.mazes.maze import Maze
from shoze.exporters.ascii.maze import AsciiExporter
from shoze.exporters.png.maze import PngExporter

mask = Mask(10, 10)
mask[1, 1] = False
mask[2, 2] = False
maze = Maze(MaskedGrid(10, 10, mask)).export(AsciiExporter())
maze = Maze(MaskedGrid(10, 10, mask), (0, 0)).export(AsciiExporter(show_distances=True))
maze = Maze(MaskedGrid(10, 10, mask), (0, 0), (9, 0)).export(
    AsciiExporter(show_path=True)
)

maze = Maze(MaskedGrid(10, 10, mask)).export(PngExporter(filename="empty"))
maze = Maze(MaskedGrid(10, 10, mask), (0, 0)).export(
    PngExporter(show_distances=True, filename="start")
)
maze = Maze(MaskedGrid(10, 10, mask), (0, 0), (9, 0)).export(
    PngExporter(show_path=True, filepath="png/start-end/startend.png")
)
