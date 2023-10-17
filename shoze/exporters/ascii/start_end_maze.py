from shoze.core.grid import Grid
from shoze.core.mazes.start_end_maze import StartEndMaze
from shoze.core.mazes.start_maze import StartMaze
from shoze.exporters.ascii.base import AsciiExporter
from shoze.exporters.base import Exporter


class StartEndAsciiExporter(AsciiExporter):
    @staticmethod
    def on(maze: StartEndMaze) -> None:
        cell_width = len(str(maze.grid.size))

        output = "+" + ("-" * cell_width + "+") * maze.grid.columns + "\n"
        for row in maze.grid.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                if cell in maze.path:
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
