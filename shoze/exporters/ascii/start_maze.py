from shoze.core.grid import Grid
from shoze.core.mazes.start_maze import StartMaze
from shoze.exporters.ascii.base import AsciiExporter
from shoze.exporters.base import Exporter


class StartAsciiExporter(AsciiExporter):
    @staticmethod
    def on(maze: StartMaze) -> None:
        cell_width = len(str(maze.grid.size))

        output = "+" + ("-" * cell_width + "+") * maze.grid.columns + "\n"
        for row in maze.grid.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                body = " " * (cell_width - len(str(maze.distances[cell]))) + str(
                    maze.distances[cell]
                )

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
