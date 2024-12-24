import numpy as np

with open("./aoc2024/day15/data1.txt", "r") as file:
    text = file.read()
    raw_map, movements = text.split("\n\n")
    raw_map = (
        raw_map.replace("#", "##")
        .replace(".", "..")
        .replace("@", "@.")
        .replace("O", "[]")
    )
    start_matrix = np.array([list(line.strip()) for line in raw_map.split("\n")])
    all_movements = movements.replace("\n", "")
    movements = list(all_movements.strip())


def print_matrix(matrix):
    lines = "\n".join(["".join(line) for line in current_matrix])
    print(lines)


current_matrix = start_matrix.copy()


def move_vertically(matrix, from_coords, diff):
    to_coords = (from_coords[0] + diff, from_coords[1])
    from_content = str(matrix[from_coords])
    to_content = str(matrix[to_coords])
    if to_content == "#":
        return False
    if to_content == ".":
        matrix[from_coords] = "."
        matrix[to_coords] = from_content
        return True
    if to_content == "[":
        other_half_coords = (to_coords[0], to_coords[1] + 1)
    if to_content == "]":
        other_half_coords = (to_coords[0], to_coords[1] - 1)
    can_move = move_vertically(matrix, to_coords, diff) and move_vertically(
        matrix, other_half_coords, diff
    )
    if not can_move:
        return False
    matrix[from_coords] = "."
    matrix[to_coords] = from_content
    matrix[other_half_coords] = "."
    return True


def move_horizontally(matrix, from_coords, diff):
    to_coords = (from_coords[0], from_coords[1] + diff)
    from_content = str(matrix[from_coords])
    to_content = str(matrix[to_coords])
    if to_content == "#":
        return False
    if to_content == ".":
        matrix[from_coords] = "."
        matrix[to_coords] = from_content
        return True
    can_move = move_horizontally(matrix, to_coords, diff)
    if not can_move:
        return False

    matrix[from_coords] = "."
    matrix[to_coords] = from_content
    return True


def compute_points(matrix):
    all_boxes = np.where(matrix == "[")
    all_boxes_coords = list(zip(all_boxes[0], all_boxes[1]))
    total = 0
    for box in all_boxes_coords:
        total += 100 * box[0] + box[1]
    return total


current_matrix = start_matrix.copy()

for movement in movements:
    next_matrix = current_matrix.copy()
    robot = np.where(next_matrix == "@")
    robot_coords = (int(robot[0][0]), int(robot[1][0]))
    if movement == "^":
        could_move = move_vertically(next_matrix, robot_coords, -1)
    if movement == "v":
        could_move = move_vertically(next_matrix, robot_coords, 1)
    if movement == ">":
        could_move = move_horizontally(next_matrix, robot_coords, 1)
    if movement == "<":
        could_move = move_horizontally(next_matrix, robot_coords, -1)
    if could_move:
        current_matrix = next_matrix

print(compute_points(current_matrix))
