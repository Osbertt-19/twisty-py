from shoze.core.maze import Algorithms, Maze

maze = Maze(10, 20).on(Algorithms.BINARY_TREE).show_distances((0, 0)).display_ascii()
