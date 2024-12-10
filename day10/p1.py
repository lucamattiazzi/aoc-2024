import numpy as np

with open("./day10/data1.txt") as f:
    lines = f.readlines()
    blocks = [list(line.strip()) for line in lines]
    matrix = np.array(blocks)


zeroes = np.where(matrix == "0")
zeroes = [(int(x), int(y)) for x, y in zip(zeroes[0], zeroes[1])]


def find_trail(matrix, trails=tuple[tuple[tuple[int]]]):
    current_point = trails[0][-1]
    current_value = int(matrix[current_point])
    new_trails = []
    if current_value == 9:
        return trails
    for trail in trails:
        last_point = trail[-1]
        close_points = [
            (last_point[0] + 1, last_point[1]),
            (last_point[0], last_point[1] + 1),
            (last_point[0] - 1, last_point[1]),
            (last_point[0], last_point[1] - 1),
        ]
        valid_close_points = [
            point
            for point in close_points
            if 0 <= point[0] < matrix.shape[0]
            and 0 <= point[1] < matrix.shape[1]
            and matrix[point] == str(current_value + 1)
        ]
        for point in valid_close_points:
            new_trails.append(trail + (point,))
    return find_trail(matrix, new_trails)


total_rank = 0

for zero in zeroes:
    found_trails = find_trail(matrix, ((zero,),))
    all_nines = [trail[-1] for trail in found_trails]
    unique_nines = set(all_nines)
    total_rank += len(unique_nines)

print(total_rank)
