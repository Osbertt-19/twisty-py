from shoze.algorithms.binary_tree import BinaryTree
from shoze.display.ascii import display_ascii
from shoze.models.cell import Cell, is_cell
from shoze.models.grid import Grid


maze = Grid(5, 20)
BinaryTree.on(maze)

display_ascii(maze)
print(maze)
