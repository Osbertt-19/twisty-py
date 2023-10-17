from shoze.core.maze import Algorithms, Maze

maze = Maze(10, 20).on(Algorithms.SIDEWINDER).save_png()
