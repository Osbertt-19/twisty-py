from shoze.algorithms.binary_tree import BinaryTree
from shoze.algorithms.sidewinder import SideWinder
from shoze.core.grid import Grid
from shoze.core.mazes.empty_maze import EmptyMaze
from shoze.core.mazes.start_end_maze import StartEndMaze
from shoze.core.mazes.start_maze import StartMaze
from shoze.exporters.png_exporter import export_png


maze = StartEndMaze((10, 10), start=(0, 0), end=(6, 5))
export_png(maze, "abc")
