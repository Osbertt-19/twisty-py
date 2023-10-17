from shoze.core.mazes.base import Maze
from shoze.core.mazes.empty_maze import EmptyMaze
from shoze.core.mazes.start_maze import StartMaze
from shoze.exporters.ascii.empty_maze import EmptyAsciiExporter
from shoze.exporters.ascii.start_end_maze import StartEndAsciiExporter
from shoze.exporters.ascii.start_maze import StartAsciiExporter


def export_ascii(maze: Maze):
    if isinstance(maze, EmptyMaze):
        EmptyAsciiExporter.on(maze)
    elif isinstance(maze, StartMaze):
        StartAsciiExporter.on(maze)
    else:
        StartEndAsciiExporter.on(maze)
