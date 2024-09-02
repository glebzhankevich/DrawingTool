from enum import Enum


class DrawingCommandType(Enum):
    CREATE_CANVAS = 'C'
    DRAW_LINE = 'L'
    DRAW_RECTANGLE = 'R'
    BUCKET_FILL = 'B'

    @classmethod
    def values(cls):
        return tuple(item.value for item in cls)
