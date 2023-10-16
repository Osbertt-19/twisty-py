from shoze.core.maze import Algorithms, Maze

maze = Maze(4, 4).on(Algorithms.BINARY_TREE).display_ascii()

cell = maze.grid[0, 0]
distances = cell.distances
print(distances)
