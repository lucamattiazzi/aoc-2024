import numpy as np

with open("./aoc2024/day20/data1.txt", "r") as file:
    lines = file.read()

start_matrix = np.array([list(line.strip()) for line in lines.split("\n")])
CHEAT_SIZE = 20
MIN_GAIN = 100


def print_matrix(matrix):
    lines = "\n".join(["".join(line) for line in matrix])
    print(lines)


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_racetrack(start_matrix):
    matrix = np.copy(start_matrix)
    start_coords = np.where(matrix == "S")
    start_coords = (int(start_coords[0][0]), int(start_coords[1][0]))

    end_coords = np.where(matrix == "E")
    end_coords = (int(end_coords[0][0]), int(end_coords[1][0]))

    current_pos = start_coords
    racetrack_coords = [current_pos]

    matrix[current_pos] = "x"

    while True:
        close_points = [
            (current_pos[0] - 1, current_pos[1]),
            (current_pos[0] + 1, current_pos[1]),
            (current_pos[0], current_pos[1] - 1),
            (current_pos[0], current_pos[1] + 1),
        ]
        for point in close_points:
            if matrix[point] == "E":
                racetrack_coords.append(point)
                return racetrack_coords
            elif matrix[point] == ".":
                current_pos = point
                racetrack_coords.append(point)
                matrix[current_pos] = "x"
                break


racetrack_coords = get_racetrack(start_matrix)
worst_res_time = len(racetrack_coords) - 1
useful_cheats = 0

for idx, coords in enumerate(racetrack_coords[:-(MIN_GAIN)]):
    valid_cheats = set(
        [
            point
            for point in racetrack_coords[idx + MIN_GAIN :]
            if manhattan(coords, point) <= CHEAT_SIZE
        ]
    )
    for valid_cheat in valid_cheats:
        time_gain = (
            racetrack_coords.index(valid_cheat) - idx - manhattan(coords, valid_cheat)
        )
        if time_gain >= MIN_GAIN:
            useful_cheats += 1

print(useful_cheats)
