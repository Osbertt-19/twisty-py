from shoze.core.cell import Cell
from shoze.core.mazes.empty_maze import EmptyMaze
from shoze.core.mazes.start_end_maze import StartEndMaze
from shoze.core.mazes.start_maze import StartMaze
from shoze.exporters.png_exporter import export_png


maze = StartMaze((20, 20))
export_png(maze)
