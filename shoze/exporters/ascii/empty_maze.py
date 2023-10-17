from shoze.core.mazes.empty_maze import EmptyMaze
from shoze.exporters.ascii.base import AsciiExporter


class EmptyAsciiExporter(AsciiExporter):
    @staticmethod
    def on(maze: EmptyMaze, cell_width: int = 3) -> None:
        output = "+" + ("-" * cell_width + "+") * maze.grid.columns + "\n"
        for row in maze.grid.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
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
