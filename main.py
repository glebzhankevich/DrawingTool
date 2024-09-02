import sys
from DrawingTool.services.utils import read_drawing_commands_from_file, execute_commands
from DrawingTool.drawing_tool import DrawingTool


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    commands = read_drawing_commands_from_file(input_file)

    tool = DrawingTool()
    execute_commands(tool, commands)

    # Output the final result to a file or console
    result = tool.render_all_steps()
    with open("output.txt", "w") as output_file:
        output_file.write(result)

    print("Drawing completed. Output with all steps written to output.txt.")


if __name__ == "__main__":
    main()
