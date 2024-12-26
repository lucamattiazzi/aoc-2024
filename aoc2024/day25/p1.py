from itertools import product

import numpy as np

with open("./aoc2024/day25/data1.txt", "r") as file:
    blocks = []
    for block in file.read().split("\n\n"):
        matrix = [list(line) for line in block.split("\n")]
        matrix = np.array(matrix)
        blocks.append(matrix)


def check_is_lock(block):
    return np.sum(block[0] == "#") == len(block[0])


def read_block(block):
    heights = [np.count_nonzero(block[:, i] == "#") for i in range(len(block[0]))]
    return np.array(heights)


locks = []
keys = []

for block in blocks:
    heights = read_block(block)
    if check_is_lock(block):
        locks.append(heights)
    else:
        keys.append(heights)

fitting = 0
for couple in product(keys, locks):
    max_height = np.max(couple[0] + couple[1])
    if max_height <= 7:
        fitting += 1

print(fitting)
