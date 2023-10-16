from shoze.core.maze import Algorithms, Maze

maze = (
    Maze(5, 20)
    .on(Algorithms.BINARY_TREE)
    .display_ascii()
    .save_png("abc", 20, (40, 50, 100), 3, (0, 0, 0))
)
