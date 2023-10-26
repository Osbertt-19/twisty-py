from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from twisty.core.mazes.maze import Maze
else:
    Maze = "Maze"
from twisty.exporters.base import Exporter


class AsciiExporter(Exporter):
    def __init__(
        self, show_distances: bool = False, show_path: bool = False, cell_width: int = 3
    ) -> None:
        super().__init__(show_distances, show_path)
        self.cell_width = cell_width

    def on(self, maze: Maze) -> None:
        super().on(maze)
        cell_width = (
            len(str(maze.grid.size))
            if self.show_distances or self.show_path
            else self.cell_width
        )

        output = "+" + ("-" * cell_width + "+") * maze.grid.columns + "\n"
        for row in maze.grid.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                if self.show_distances:
                    body = " " * (cell_width - len(str(maze.distances[cell]))) + str(
                        maze.distances[cell]
                    )
                elif self.show_path and cell in maze.path:
                    body = " " * (cell_width - len(str(maze.path[cell]))) + str(
                        maze.path[cell]
                    )
                else:
                    body = " " * cell_width

                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary
                south_boundary = (
                    " " * cell_width if cell.is_linked(cell.south) else "-" * cell_width
                )
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"
        print(output)
