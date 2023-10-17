from shoze.algorithms.binary_tree import BinaryTree
from shoze.algorithms.sidewinder import SideWinder
from shoze.core.grid import Grid
from shoze.core.mazes.empty_maze import EmptyMaze
from shoze.core.mazes.start_end_maze import StartEndMaze
from shoze.core.mazes.start_maze import StartMaze
from shoze.exporters.exporter import export_ascii


maze = StartMaze(Grid(4, 4), start=(2, 1))
export_ascii(maze)
