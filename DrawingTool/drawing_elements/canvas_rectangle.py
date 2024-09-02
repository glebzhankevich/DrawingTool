from typing import Tuple

from DrawingTool.services.validators import DrawingToolValidator
from DrawingTool.drawing_elements.canvas_line import CanvasLine
from dataclasses import dataclass


@dataclass
class CanvasRectangle(DrawingToolValidator):
    coords: Tuple[int, int, int, int]

    def execute(self, canvas):
        x1, y1, x2, y2 = self.coords
        self.validate(canvas, self.coords)
        self._draw_rectangle_borders(canvas, x1, y1, x2, y2)

    def _draw_rectangle_borders(self, canvas, x1: int, y1: int, x2: int, y2: int):
        borders = [
            (x1, y1, x2, y1),  # Top border
            (x1, y2, x2, y2),  # Bottom border
            (x1, y1, x1, y2),  # Left border
            (x2, y1, x2, y2)  # Right border
        ]

        for border in borders:
            CanvasLine(border).execute(canvas)
