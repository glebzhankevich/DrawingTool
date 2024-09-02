class DrawingToolValidator:
    def validate(self, canvas, coords):
        self._check_canvas_exists(canvas)
        self.check_within_canvas_bounds(canvas, coords)

    def check_within_canvas_bounds(self, canvas, coords):
        for i in range(0, len(coords), 2):
            x, y = coords[i], coords[i + 1]
            if not (0 <= x <= canvas.width and 0 <= y <= canvas.height):
                raise ValueError(f"Coordinates ({x}, {y}) are out of bounds.")

    def _check_canvas_exists(self, canvas):
        if canvas is None or not hasattr(canvas, 'grid'):
            raise ValueError("Canvas not created. Please create a canvas first.")
