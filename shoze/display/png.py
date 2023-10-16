from time import gmtime, strftime
from shoze.models.grid import Grid
from PIL import Image, ImageDraw


def save_png(
    grid: Grid,
    filename: str = strftime("%Y-%m-%d-%H-%M-%S", gmtime()),
    cell_size: int = 30,
):
    image = _render_image(grid, filename, cell_size)
    image.save(f"png/{filename}.png", "PNG", optimize=True)


def _render_image(grid: Grid, filename: str, cell_size: int):
    wall_color = (0, 0, 0)
    wall_width = 1
    image_width = (cell_size * grid.columns) + 1
    image_height = (cell_size * grid.rows) + 1

    image = Image.new("RGBA", (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for cell in grid.each_cell():
        x1 = cell.column * cell_size
        y1 = cell.row * cell_size
        x2 = (cell.column + 1) * cell_size
        y2 = (cell.row + 1) * cell_size

        if not cell.north:
            draw.line((x1, y1, x2, y1), wall_color, wall_width)
        if not cell.west:
            draw.line((x1, y1, x1, y2), wall_color, wall_width)
        if not cell.is_linked(cell.east):
            draw.line((x2, y1, x2, y2), wall_color, wall_width)
        if not cell.is_linked(cell.south):
            draw.line((x1, y2, x2, y2), wall_color, wall_width)
    return image
