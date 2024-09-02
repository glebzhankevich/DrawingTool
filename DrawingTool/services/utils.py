from DrawingTool.services.enums import DrawingCommandType
from DrawingTool.drawing_tool import DrawingTool


def read_drawing_commands_from_file(file_path: str):
    with open(file_path, 'r') as f:
        try:
            commands = [line.strip() for line in f.readlines()]
        except IOError as e:
            raise IOError(f"Error reading file '{file_path}': {e}")

    return commands


def execute_commands(d_tool: DrawingTool, commands: list[str]):
    for cmd in commands:
        cmd_parts = cmd.split()

        cmd_name = cmd_parts[0]
        if cmd_name not in DrawingCommandType.values():
            raise ValueError(f"Unknown command: {cmd_name}. Supported commands: {DrawingCommandType.values()}")

        cmd_type = DrawingCommandType(cmd_name)

        if cmd_type == DrawingCommandType.CREATE_CANVAS:
            width, height = map(int, cmd_parts[1:])
            d_tool.create_canvas(width, height)

        elif cmd_type == DrawingCommandType.DRAW_LINE:
            coords = tuple(map(int, cmd_parts[1:]))
            d_tool.draw_line(coords)

        elif cmd_type == DrawingCommandType.DRAW_RECTANGLE:
            coords = tuple(map(int, cmd_parts[1:]))
            d_tool.draw_rectangle(coords)

        elif cmd_type == DrawingCommandType.BUCKET_FILL:
            x, y = map(int, cmd_parts[1:3])
            color = cmd_parts[3]
            d_tool.bucket_fill(x, y, color)

        else:
            raise ValueError(f"Command: {cmd_name} is not supported")
