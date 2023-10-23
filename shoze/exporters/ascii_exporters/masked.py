from typing import TYPE_CHECKING
from shoze.core.cell import Cell
from shoze.exporters.ascii import AsciiExporter


if TYPE_CHECKING:
    from shoze.core.mazes.masked_maze import MaskedMaze
else:
    MaskedMaze = "MaskedMaze"
from shoze.exporters.base import Exporter


class MaskedAsciiExporter(AsciiExporter):
    def check_mask(self,cell:Cell)->bool:
        return self.maze
    
    def on(self, maze: MaskedMaze) -> None:
        Exporter.on(self, maze)
        cell_width = (
            len(str(maze.grid.size))
            if self.show_distances or self.show_path
            else self.cell_width
        )
        output = ""

        if self.check_mask(maze,maze.grid[0,0]):
            output+="+"+"-"*cell_width
        else:
            output+=" "+" "*cell_width

        if self.check_mask(maze,maze.grid[0,1]) or maze.grid[0,1].west:

        