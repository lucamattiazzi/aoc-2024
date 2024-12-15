import numpy as np

with open("./day15/data1.txt", "r") as file:
    text = file.read()
    raw_map, movements = text.split("\n\n")
    start_matrix = np.array([list(line.strip()) for line in raw_map.split("\n")])
    all_movements = movements.replace("\n", "")
    movements = list(all_movements.strip())


def print_matrix(matrix):
    lines = "\n".join(["".join(line) for line in current_matrix])
    print(lines)


def move_to(matrix, from_coords, diff):
    to_coords = (from_coords[0] + diff[0], from_coords[1] + diff[1])
    from_content = str(matrix[from_coords])
    to_content = str(matrix[to_coords])
    if to_content == "#":
        return False
    if to_content == ".":
        matrix[from_coords] = "."
        matrix[to_coords] = from_content
        return True
    can_move = move_to(matrix, to_coords, diff)
    if not can_move:
        return False
    matrix[from_coords] = "."
    matrix[to_coords] = from_content
    return True


def compute_points(matrix):
    all_boxes = np.where(matrix == "O")
    all_boxes_coords = list(zip(all_boxes[0], all_boxes[1]))
    total = 0
    for box in all_boxes_coords:
        total += 100 * box[0] + box[1]
    return total


current_matrix = start_matrix.copy()
print_matrix(current_matrix)

for movement in movements:
    robot = np.where(current_matrix == "@")
    robot_coords = (int(robot[0][0]), int(robot[1][0]))
    if movement == "^":
        diff = (-1, 0)
    if movement == "v":
        diff = (1, 0)
    if movement == ">":
        diff = (0, 1)
    if movement == "<":
        diff = (0, -1)

    move_to(current_matrix, robot_coords, diff)

print(compute_points(current_matrix))
