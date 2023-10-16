from shoze.algorithms.binary_tree import BinaryTree
from shoze.algorithms.sidewinder import SideWinder
from shoze.display.ascii import display_ascii
from shoze.display.png import save_png, _render_image
from shoze.models.cell import Cell, is_cell
from shoze.models.grid import Grid

maze = Grid(5, 20)
# BinaryTree.on(maze)
SideWinder.on(maze)

display_ascii(maze)
save_png(maze, "abc")
_render_image(maze, "abc", 30)
