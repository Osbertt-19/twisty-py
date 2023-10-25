from time import gmtime, strftime
from typing import List
from shoze.core.cell import Cell
from shoze.core.mazes.masked_maze import MaskedMaze
from shoze.core.mazes.maze import Maze
from shoze.exporters.base import Exporter
from shoze.exporters.png.maze import PngExporter
from shoze.utils.colors import BLACK, WHITE, Color
from PIL import Image, ImageDraw

from shoze.utils.config import PNG_OFFSET


class MaskedPngExporter(PngExporter):
    def exists(self, cells: List[Cell]) -> bool:
        for cell in cells:
            if cell and self.maze.grid.mask[cell.row, cell.column]:
                return True
        return False

    def _render_image(self, maze: MaskedMaze):
        self.maze = maze
        image_width = (self.cell_size * maze.grid.columns) + (
            PNG_OFFSET * 2
        )  # offset to both sides
        image_height = (self.cell_size * maze.grid.rows) + (
            PNG_OFFSET * 2
        )  # offset to top and bottom

        image = Image.new("RGBA", (image_width, image_height), self.background_color)
        draw = ImageDraw.Draw(image)
        for i in range(2):
            for cell in maze.grid.each_cell():
                x1 = cell.column * self.cell_size + PNG_OFFSET
                y1 = cell.row * self.cell_size + PNG_OFFSET
                x2 = (cell.column + 1) * self.cell_size + PNG_OFFSET
                y2 = (cell.row + 1) * self.cell_size + PNG_OFFSET

                if i == 0:
                    if self.show_distances and self.exists([cell]):
                        color = maze.bg_for_cell(cell)
                    elif (
                        self.show_path
                        and cell in maze.path.keys()
                        and self.exists([cell])
                    ):
                        color = maze.bg_for_cell(cell)
                    else:
                        color = WHITE
                    draw.rectangle((x1, y1, x2, y2), fill=color)

                if self.exists([cell]) and not cell.north:
                    draw.line((x1, y1, x2, y1), self.wall_color, self.wall_width)
                if self.exists([cell]) and not cell.west:
                    draw.line((x1, y1, x1, y2), self.wall_color, self.wall_width)
                if self.exists([cell]) and not cell.is_linked(cell.east):
                    draw.line((x2, y1, x2, y2), self.wall_color, self.wall_width)
                if self.exists([cell]) and not cell.is_linked(cell.south):
                    draw.line((x1, y2, x2, y2), self.wall_color, self.wall_width)
        return image
