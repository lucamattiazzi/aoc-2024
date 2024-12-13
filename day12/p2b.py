from collections import Counter

import numpy as np

with open("./day12/data1.txt") as f:
    lines = f.readlines()
    blocks = [list(line.strip()) for line in lines]
    matrix = np.array(blocks)


unique = np.unique(matrix)

all_groups = []


def find_neighbors(starting_point, positions):
    if not positions:
        return []

    neighbors = []
    if (starting_point[0] + 1, starting_point[1]) in positions:
        candidate = (starting_point[0] + 1, starting_point[1])
        positions.remove(candidate)
        neighbors += [candidate, *find_neighbors(candidate, positions)]
    if (starting_point[0] - 1, starting_point[1]) in positions:
        candidate = (starting_point[0] - 1, starting_point[1])
        positions.remove(candidate)
        neighbors += [candidate, *find_neighbors(candidate, positions)]
    if (starting_point[0], starting_point[1] + 1) in positions:
        candidate = (starting_point[0], starting_point[1] + 1)
        positions.remove(candidate)
        neighbors += [candidate, *find_neighbors(candidate, positions)]
    if (starting_point[0], starting_point[1] - 1) in positions:
        candidate = (starting_point[0], starting_point[1] - 1)
        positions.remove(candidate)
        neighbors += [candidate, *find_neighbors(candidate, positions)]

    return neighbors


def compute_sides(group):
    all_vertices = []
    for point in group:
        all_vertices.append((point[0] + 1, point[1]))
        all_vertices.append((point[0] - 1, point[1]))
        all_vertices.append((point[0], point[1] + 1))
        all_vertices.append((point[0], point[1] - 1))
    counter = Counter(all_vertices)
    vertices = len([k for k, v in counter.items() if v == 1])
    return vertices


for value in unique:
    value_groups = []
    positions = np.where(matrix == value)
    positions = list(zip(positions[0], positions[1]))
    positions = [(int(p[0]), int(p[1])) for p in positions]
    while positions:
        starting_point = positions.pop()
        new_group = [starting_point]
        neighbors = find_neighbors(starting_point, positions)
        value_groups.append([*new_group, *neighbors])

    for group in value_groups:
        area = len(group)
        sides = compute_sides(group)

        all_groups.append({"value": value, "area": area, "sides": sides})


total = 0
for group in all_groups:
    total += group["area"] * group["sides"]
print(total)
