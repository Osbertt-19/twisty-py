from shoze.core.grid import Grid
from shoze.exporters.base import Exporter


class Ascii(Exporter):
    @staticmethod
    def export(grid: Grid) -> None:
        if grid.show_distances_flag:
            cell_width = len(str(grid.size))
        else:
            cell_width = 3
        output = "+" + ("-" * cell_width + "+") * grid.columns + "\n"
        for row in grid.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                if cell.content is not None:
                    body = " " * (cell_width - len(str(cell.content))) + str(
                        cell.content
                    )
                else:
                    body = "   "
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
