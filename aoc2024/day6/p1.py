import numpy as np

with open("./aoc2024/day6/data1.txt") as f:
    lines = f.readlines()
    blocks = [list(line.strip()) for line in lines]
    matrix = np.array(blocks)

guard = np.where(matrix == "^")

blockers = np.where(matrix == "#")
blockers = list(zip(blockers[0], blockers[1]))


DIRECTIONS = ["up", "right", "down", "left"]

direction_idx = 0
guard_pos = (guard[0][0], guard[1][0])

used_matrix = np.zeros(matrix.shape)
used_matrix[guard_pos] = 1
is_out = False

while True:
    print(used_matrix.sum())
    # print(used_matrix)
    direction = DIRECTIONS[direction_idx]
    if is_out:
        break

    if direction == "up":
        guard_row, guard_col = guard_pos
        col = matrix[:, guard_col]
        col_blockers = np.where(col == "#")[0]
        valid_blockers = [
            int(block_row) for block_row in col_blockers if int(block_row) < guard_row
        ]
        if not valid_blockers:
            breakpoint()
            is_out = True
            valid_blockers = [-1]
        closest_blocker_row = max(valid_blockers)
        used_matrix[closest_blocker_row + 1 : guard_row, guard_col] = 1
        guard_pos = (closest_blocker_row + 1, guard_col)

    if direction == "right":
        guard_row, guard_col = guard_pos
        row = matrix[guard_row]
        row_blockers = np.where(row == "#")[0]
        valid_blockers = [
            int(bloc_col) for bloc_col in row_blockers if int(bloc_col) > guard_col
        ]
        if not valid_blockers:
            breakpoint()
            is_out = True
            valid_blockers = [len(row) + 1]
        closest_blocker_col = min(valid_blockers)
        used_matrix[guard_row, guard_col:closest_blocker_col] = 1
        guard_pos = (guard_row, closest_blocker_col - 1)

    if direction == "down":
        guard_row, guard_col = guard_pos
        col = matrix[:, guard_col]
        col_blockers = np.where(col == "#")[0]
        valid_blockers = [
            int(block_row) for block_row in col_blockers if int(block_row) > guard_row
        ]
        if not valid_blockers:
            breakpoint()
            is_out = True
            valid_blockers = [len(col) + 1]
        closest_blocker_row = min(valid_blockers)
        used_matrix[guard_row:closest_blocker_row, guard_col] = 1
        guard_pos = (closest_blocker_row - 1, guard_col)

    if direction == "left":
        guard_row, guard_col = guard_pos
        row = matrix[guard_row]
        row_blockers = np.where(row == "#")[0]
        valid_blockers = [
            int(bloc_col) for bloc_col in row_blockers if int(bloc_col) < guard_col
        ]
        if not valid_blockers:
            breakpoint()
            is_out = True
            valid_blockers = [-1]
        closest_blocker_col = max(valid_blockers)
        used_matrix[guard_row, closest_blocker_col + 1 : guard_col] = 1
        guard_pos = (guard_row, closest_blocker_col + 1)

    direction_idx = (direction_idx + 1) % 4

print(np.sum(used_matrix))
