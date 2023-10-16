from shoze.core.grid import Grid
from shoze.exporters.base import Exporter


class Ascii(Exporter):
    @staticmethod
    def export(grid: Grid) -> None:
        output = "+" + "---+" * grid.columns + "\n"
        for row in grid.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                body = "   "
                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary
                south_boundary = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"

        print(output)
