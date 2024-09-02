from DrawingTool.drawing_elements.canvas_rectangle import CanvasRectangle
from DrawingTool.drawing_elements.canvas_line import CanvasLine
from DrawingTool.drawing_elements.canvas import Canvas


class DrawingTool:
    """ Main class to interact with DrawingTool """
    def __init__(self):
        self.canvas = None
        self.output = []

    def create_canvas(self, width, height):
        self.canvas = Canvas(width, height)
        self.capture_canvas_state()

    def draw_line(self, coords):
        line = CanvasLine(coords)
        line.execute(self.canvas)
        self.capture_canvas_state()

    def draw_rectangle(self, coords):
        rectangle = CanvasRectangle(coords)
        rectangle.execute(self.canvas)
        self.capture_canvas_state()

    def bucket_fill(self, x, y, color):
        self.canvas.bucket_fill(x, y, color)
        self.capture_canvas_state()

    def capture_canvas_state(self):
        """" Method to capture each state of drawing process and add it to final result"""
        if not self.canvas:
            raise ValueError("Canvas not created.")

        top_border = '-' * (self.canvas.width + 2)

        canvas_with_border = [top_border]
        canvas_with_border.extend('|' + ''.join(row) + '|' for row in self.canvas.grid)
        canvas_with_border.append(top_border)

        self.output.append("\n".join(canvas_with_border))

    def render_all_steps(self):
        return "\n\n".join(self.output)
