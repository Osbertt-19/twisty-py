from time import gmtime, strftime
from shoze.core.mazes.base import Maze
from shoze.core.mazes.empty_maze import EmptyMaze
from shoze.core.mazes.start_maze import StartMaze
from shoze.exporters.ascii.empty_maze import EmptyAsciiExporter
from shoze.exporters.ascii.start_end_maze import StartEndAsciiExporter
from shoze.exporters.ascii.start_maze import StartAsciiExporter
from shoze.exporters.png.empty_maze import EmptyPngExporter
from shoze.exporters.png.start_end_maze import StartEndPngExporter
from shoze.exporters.png.start_maze import StartPngExporter


def export_png(maze: Maze, filename: str = strftime("%Y-%m-%d-%H-%M-%S", gmtime())):
    if isinstance(maze, EmptyMaze):
        EmptyPngExporter.on(maze, filename)
    elif isinstance(maze, StartMaze):
        StartPngExporter.on(maze, filename)
    else:
        StartEndPngExporter.on(maze, filename)
