from shoze.core.maze import Maze
from shoze.exporters.ascii_exporter import AsciiExporter
from shoze.exporters.png_exporter import PngExporter


# maze = Maze((10, 10)).export(AsciiExporter())
# maze = Maze((10, 10), (0, 0)).export(AsciiExporter(show_distances=True))
# maze = Maze((10, 10), (0, 0), (9, 0)).export(AsciiExporter(show_path=True))

# maze = Maze((10, 10)).export(PngExporter(filename="empty"))
# maze = Maze((10, 10), (0, 0)).export(
#     PngExporter(show_distances=True, filename="start")
# )
# maze = Maze((10, 10), (0, 0), (9, 0)).export(
#     PngExporter(show_path=True, filepath="png/start-end/startend.png")
# )
