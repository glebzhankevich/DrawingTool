from dataclasses import dataclass, field
from typing import List


@dataclass
class Canvas:
    width: int
    height: int
    grid: List[List[str]] = field(init=False)

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be positive integers.")

        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def bucket_fill(self, x: int, y: int, color: str):
        target_color = self.grid[y - 1][x - 1]
        if target_color == color:
            return
        self._fill(x - 1, y - 1, target_color, color)

    def _fill(self, x: int, y: int, target_color: str, color: str):
        if x < 0 or x >= len(self.grid[0]) or y < 0 or y >= len(self.grid):
            return
        if self.grid[y][x] != target_color:
            return

        self.grid[y][x] = color

        # Directions: right, left, down, up
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            self._fill(x + dx, y + dy, target_color, color)
