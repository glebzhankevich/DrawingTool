from dataclasses import dataclass
from typing import Tuple

from DrawingTool.services.validators import DrawingToolValidator


@dataclass
class CanvasLine(DrawingToolValidator):
    coords: Tuple[int, int, int, int]

    def execute(self, canvas):
        self.validate(canvas, self.coords)
        x1, y1, x2, y2 = self.coords

        if x1 == x2:
            self._draw_vertical_line(canvas, x1, y1, y2)
        elif y1 == y2:
            self._draw_horizontal_line(canvas, x1, x2, y1)
        else:
            raise ValueError("Only horizontal or vertical lines are supported.")

    def _draw_vertical_line(self, canvas, x: int, y1: int, y2: int):
        for y in range(min(y1, y2) - 1, max(y1, y2)):
            canvas.grid[y][x - 1] = 'x'

    def _draw_horizontal_line(self, canvas, x1: int, x2: int, y: int):
        for x in range(min(x1, x2) - 1, max(x1, x2)):
            canvas.grid[y - 1][x] = 'x'
