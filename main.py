from shoze.core.grid import Grid
from shoze.core.maze import Algorithms, Maze

grid = Maze(4, 4).on(Algorithms.BINARY_TREE)
grid.show_distances((0, 0))
