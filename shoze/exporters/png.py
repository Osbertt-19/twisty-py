from time import gmtime, strftime
from typing import Tuple
from shoze.core.grid import Grid
from PIL import Image, ImageDraw

from shoze.exporters.base import Exporter
from shoze.exporters.colors import BLACK, WHITE, Color


class Png(Exporter):
    @staticmethod
    def export(
        grid: Grid,
        filename: str,
        cell_size: int,
        wall_color: Color,
        wall_width: int,
        background_color: Color,
    ):
        image = Png._render_image(
            grid, cell_size, wall_color, wall_width, background_color
        )
        image.save(f"png/{filename}.png", "PNG", optimize=True)

    @staticmethod
    def _render_image(
        grid: Grid,
        cell_size: int,
        wall_color: Color,
        wall_width: int,
        background_color: Color,
    ):
        image_width = (cell_size * grid.columns) + 1
        image_height = (cell_size * grid.rows) + 1

        image = Image.new("RGBA", (image_width, image_height), background_color)
        draw = ImageDraw.Draw(image)
        for i in range(2):
            for cell in grid.each_cell():
                x1 = cell.column * cell_size
                y1 = cell.row * cell_size
                x2 = (cell.column + 1) * cell_size
                y2 = (cell.row + 1) * cell_size
                if (
                    i == 0
                    and grid.show_distances_flag
                    and grid.start.distances[cell] is not None
                ):
                    color = grid.bg_for_cell(cell)
                    draw.rectangle((x1, y1, x2, y2), fill=color)
                if not cell.north:
                    draw.line((x1, y1, x2, y1), wall_color, wall_width)
                if not cell.west:
                    draw.line((x1, y1, x1, y2), wall_color, wall_width)
                if not cell.is_linked(cell.east):
                    draw.line((x2, y1, x2, y2), wall_color, wall_width)
                if not cell.is_linked(cell.south):
                    draw.line((x1, y2, x2, y2), wall_color, wall_width)
        return image
