from time import gmtime, strftime
from twisty.core.mazes.maze import Maze
from twisty.exporters.base import Exporter
from twisty.utils.colors import BLACK, WHITE, Color
from PIL import Image, ImageDraw

from twisty.utils.config import PNG_OFFSET


class PngExporter(Exporter):
    def __init__(
        self,
        show_distances: bool = False,
        show_path: bool = False,
        filename: str = strftime("%Y-%m-%d-%H-%M-%S", gmtime()),
        filepath: str = None,
        cell_size: int = 10,
        wall_color: Color = BLACK,
        wall_width: int = 1,
        background_color: Color = WHITE,
    ) -> None:
        super().__init__(show_distances, show_path)

        self.filename = filename
        self.filepath = filepath
        self.cell_size = cell_size
        self.wall_color = wall_color
        self.wall_width = wall_width
        self.background_color = background_color

    def on(self, maze: Maze) -> None:
        super().on(maze)
        image = self._render_image(maze)
        if self.filepath:
            image.save(self.filepath, "PNG", optimize=True)
        image.save(f"images/{self.filename}.png", "PNG", optimize=True)

    def _render_image(self, maze: Maze):
        image_width = (self.cell_size * maze.grid.columns) + (PNG_OFFSET * 2)
        image_height = (self.cell_size * maze.grid.rows) + (PNG_OFFSET * 2)

        image = Image.new("RGBA", (image_width, image_height), self.background_color)
        draw = ImageDraw.Draw(image)
        for i in range(2):
            for cell in maze.grid.each_cell():
                x1 = cell.column * self.cell_size + PNG_OFFSET
                y1 = cell.row * self.cell_size + PNG_OFFSET
                x2 = (cell.column + 1) * self.cell_size + PNG_OFFSET
                y2 = (cell.row + 1) * self.cell_size + PNG_OFFSET

                if i == 0:
                    if self.show_distances:
                        color = maze.bg_for_cell(cell)
                    elif self.show_path and cell in maze.path.keys():
                        color = maze.bg_for_cell(cell)
                    else:
                        color = WHITE
                    draw.rectangle((x1, y1, x2, y2), fill=color)

                if not cell.north:
                    draw.line((x1, y1, x2, y1), self.wall_color, self.wall_width)
                if not cell.west:
                    draw.line((x1, y1, x1, y2), self.wall_color, self.wall_width)
                if not cell.is_linked(cell.east):
                    draw.line((x2, y1, x2, y2), self.wall_color, self.wall_width)
                if not cell.is_linked(cell.south):
                    draw.line((x1, y2, x2, y2), self.wall_color, self.wall_width)
        return image
