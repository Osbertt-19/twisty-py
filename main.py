from shoze.core.maze import Algorithms, Maze

maze = Maze(10, 20).on(Algorithms.SIDEWINDER).show_distances().save_png("abii")
