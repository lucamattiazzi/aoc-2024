from itertools import combinations

import numpy as np

with open("./day8/data1.txt") as f:
    lines = f.readlines()
    blocks = [list(line.strip()) for line in lines]
    matrix = np.array(blocks)

SIDE = len(matrix)

all_chars = np.unique(matrix)
frequencies = [char for char in all_chars if char != "."]
count = 0
result_matrix = matrix.copy()
for frequency in frequencies:
    antennas = np.where(matrix == frequency)
    antennas_coors = list(zip(antennas[0], antennas[1]))
    for permutation in combinations(antennas_coors, 2):
        antenna_a = permutation[0]
        antenna_b = permutation[1]
        dist_x = antenna_a[0] - antenna_b[0]
        dist_y = antenna_a[1] - antenna_b[1]

        antinode_a = [
            antenna_a[0] + dist_x,
            antenna_a[1] + dist_y,
        ]
        antinode_b = [
            antenna_b[0] - dist_x,
            antenna_b[1] - dist_y,
        ]

        result_matrix[antenna_a[0], antenna_a[1]] = "#"
        result_matrix[antenna_b[0], antenna_b[1]] = "#"

        while True:
            if not (0 <= antinode_a[0] < SIDE and 0 <= antinode_a[1] < SIDE):
                break
            result_matrix[antinode_a[0], antinode_a[1]] = "#"
            antinode_a = [
                antinode_a[0] + dist_x,
                antinode_a[1] + dist_y,
            ]
        while True:
            if not (0 <= antinode_b[0] < SIDE and 0 <= antinode_b[1] < SIDE):
                break
            result_matrix[antinode_b[0], antinode_b[1]] = "#"
            antinode_b = [
                antinode_b[0] - dist_x,
                antinode_b[1] - dist_y,
            ]

print(result_matrix)
print(np.count_nonzero(result_matrix == "#"))
