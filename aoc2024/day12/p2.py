import numpy as np

with open("./aoc2024/day12/data1.txt") as f:
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


def compute_top_sides(group):
    sides = 0
    all_values = {}
    for i in group:
        if (i[0] - 1, i[1]) not in group:
            all_values[i[0]] = all_values.get(i[0], [])
            all_values[i[0]].append(i[1])
    for key, values in all_values.items():
        sorted_values = sorted(values)
        differences = [
            sorted_values[i + 1] - sorted_values[i]
            for i in range(len(sorted_values) - 1)
        ]
        diff_more_than_one = [d for d in differences if d > 1]
        sides += len(diff_more_than_one) + 1
    return sides


def compute_bottom_sides(group):
    sides = 0
    all_values = {}
    for i in group:
        if (i[0] + 1, i[1]) not in group:
            all_values[i[0]] = all_values.get(i[0], [])
            all_values[i[0]].append(i[1])
    for key, values in all_values.items():
        sorted_values = sorted(values)
        differences = [
            sorted_values[i + 1] - sorted_values[i]
            for i in range(len(sorted_values) - 1)
        ]
        diff_more_than_one = [d for d in differences if d > 1]
        sides += len(diff_more_than_one) + 1
    return sides


def compute_left_sides(group):
    sides = 0
    all_values = {}
    for i in group:
        if (i[0], i[1] - 1) not in group:
            all_values[i[1]] = all_values.get(i[1], [])
            all_values[i[1]].append(i[0])
    for key, values in all_values.items():
        sorted_values = sorted(values)
        differences = [
            sorted_values[i + 1] - sorted_values[i]
            for i in range(len(sorted_values) - 1)
        ]
        diff_more_than_one = [d for d in differences if d > 1]
        sides += len(diff_more_than_one) + 1
    return sides


def compute_right_sides(group):
    sides = 0
    all_values = {}
    for i in group:
        if (i[0], i[1] + 1) not in group:
            all_values[i[1]] = all_values.get(i[1], [])
            all_values[i[1]].append(i[0])
    for key, values in all_values.items():
        sorted_values = sorted(values)
        differences = [
            sorted_values[i + 1] - sorted_values[i]
            for i in range(len(sorted_values) - 1)
        ]
        diff_more_than_one = [d for d in differences if d > 1]
        sides += len(diff_more_than_one) + 1
    return sides


def compute_sides(group):
    top_sides = compute_top_sides(group)
    left_sides = compute_left_sides(group)
    bottom_sides = compute_bottom_sides(group)
    right_sides = compute_right_sides(group)
    return top_sides + left_sides + bottom_sides + right_sides


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
