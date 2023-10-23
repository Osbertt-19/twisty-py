from typing import TYPE_CHECKING, List
from shoze.core.cell import Cell
from shoze.exporters.ascii import AsciiExporter


if TYPE_CHECKING:
    from shoze.core.mazes.masked_maze import MaskedMaze
else:
    MaskedMaze = "MaskedMaze"
from shoze.exporters.base import Exporter


class MaskedAsciiExporter(AsciiExporter):
    def exists(self, cells: List[Cell]) -> bool:
        for cell in cells:
            if cell and self.maze.grid.mask[cell.row, cell.column]:
                return True
        return False

    def on(self, maze: MaskedMaze) -> None:
        Exporter.on(self, maze)
        self.maze = maze
        cell_width = (
            len(str(maze.grid.size))
            if self.show_distances or self.show_path
            else self.cell_width
        )

        H = "-" * cell_width
        V = "|"
        I = "+"
        S = " "
        SS = " " * cell_width
        output = ""

        # Topmost line
        output += I if self.exists([maze.grid[0, 0]]) else S
        output += H if self.exists([maze.grid[0, 0]]) else SS
        for i in range(1, maze.grid.columns):
            output += I if self.exists([maze.grid[0, i], maze.grid[0, i - 1]]) else S
            output += H if self.exists([maze.grid[0, i]]) else SS
        output += I if self.exists([maze.grid[0, i]]) else S

        output += "\n"

        # Bodies
        for j in range(maze.grid.rows):
            output += V if self.exists([maze.grid[j, 0]]) else S
            output += SS if self.exists([maze.grid[j, 0]]) else SS
            for i in range(1, maze.grid.columns):
                if self.exists([maze.grid[j, i], maze.grid[j, i - 1]]):
                    if not maze.grid[j, i].is_linked(maze.grid[j, i - 1]):
                        output += V
                    else:
                        output += S
                else:
                    output += S

                output += SS if self.exists([maze.grid[j, i]]) else SS
            output += V if self.exists([maze.grid[j, i]]) else S

            output += "\n"
            # Bottom lines
            output += I if self.exists([maze.grid[j, 0], maze.grid[j + 1, 0]]) else S

            if self.exists([maze.grid[j, 0], maze.grid[j + 1, 0]]):
                if not maze.grid[j, 0].is_linked(maze.grid[j + 1, 0]):
                    output += H
                else:
                    output += SS
            else:
                output += SS
            for i in range(1, maze.grid.columns):
                output += (
                    I
                    if self.exists(
                        [
                            maze.grid[j, i],
                            maze.grid[j, i - 1],
                            maze.grid[j + 1, i],
                            maze.grid[j + 1, i - 1],
                        ]
                    )
                    else S
                )

                if self.exists([maze.grid[j, i], maze.grid[j + 1, i]]):
                    if not maze.grid[j, i].is_linked(maze.grid[j + 1, i]):
                        output += H
                    else:
                        output += SS
                else:
                    output += SS

            output += I if self.exists([maze.grid[j, i], maze.grid[j + 1, i]]) else S

            output += "\n"

        print(output)
