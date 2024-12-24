import numpy as np

with open("./aoc2024/day6/data1.txt") as f:
    lines = f.readlines()
    blocks = [list(line.strip()) for line in lines]
    original_matrix = np.array(blocks)


def check_maze(matrix, additional_blocker=None):
    matrix = matrix.copy()
    if additional_blocker:
        matrix[additional_blocker] = "#"

    guard = np.where(matrix == "^")

    blockers = np.where(matrix == "#")
    blockers = list(zip(blockers[0], blockers[1]))

    DIRECTIONS = ["up", "right", "down", "left"]

    guard_pos = (int(guard[0][0]), int(guard[1][0]))

    used_matrix = np.zeros(matrix.shape)
    used_matrix[guard_pos] = 1
    guard_pos_list = set()
    is_out = False
    is_loop = False

    direction_idx = 0
    while True:
        direction = DIRECTIONS[direction_idx]
        if is_out:
            break

        if is_loop:
            return additional_blocker
            break

        if direction == "up":
            guard_row, guard_col = guard_pos
            col = matrix[:, guard_col]
            col_blockers = np.where(col == "#")[0]
            valid_blockers = [
                int(block_row)
                for block_row in col_blockers
                if int(block_row) < guard_row
            ]
            if not valid_blockers:
                is_out = True
                valid_blockers = [-1]
            closest_blocker_row = max(valid_blockers)
            used_matrix[closest_blocker_row + 1 : guard_row, guard_col] = 1
            guard_pos = (int(closest_blocker_row + 1), int(guard_col))
            guard_pos_with_direction = (guard_pos[0], guard_pos[1], direction)
            if guard_pos_with_direction in guard_pos_list:
                is_loop = True
            guard_pos_list.add(guard_pos_with_direction)

        if direction == "right":
            guard_row, guard_col = guard_pos
            row = matrix[guard_row]
            row_blockers = np.where(row == "#")[0]
            valid_blockers = [
                int(bloc_col) for bloc_col in row_blockers if int(bloc_col) > guard_col
            ]
            if not valid_blockers:
                is_out = True
                valid_blockers = [len(row) + 1]
            closest_blocker_col = min(valid_blockers)
            used_matrix[guard_row, guard_col:closest_blocker_col] = 1
            guard_pos = (int(guard_row), int(closest_blocker_col - 1))
            guard_pos_with_direction = (guard_pos[0], guard_pos[1], direction)
            if guard_pos_with_direction in guard_pos_list:
                is_loop = True
            guard_pos_list.add(guard_pos_with_direction)

        if direction == "down":
            guard_row, guard_col = guard_pos
            col = matrix[:, guard_col]
            col_blockers = np.where(col == "#")[0]
            valid_blockers = [
                int(block_row)
                for block_row in col_blockers
                if int(block_row) > guard_row
            ]
            if not valid_blockers:
                is_out = True
                valid_blockers = [len(col) + 1]
            closest_blocker_row = min(valid_blockers)
            used_matrix[guard_row:closest_blocker_row, guard_col] = 1
            guard_pos = (int(closest_blocker_row - 1), int(guard_col))
            guard_pos_with_direction = (guard_pos[0], guard_pos[1], direction)
            if guard_pos_with_direction in guard_pos_list:
                is_loop = True
            guard_pos_list.add(guard_pos_with_direction)

        if direction == "left":
            guard_row, guard_col = guard_pos
            row = matrix[guard_row]
            row_blockers = np.where(row == "#")[0]
            valid_blockers = [
                int(bloc_col) for bloc_col in row_blockers if int(bloc_col) < guard_col
            ]
            if not valid_blockers:
                is_out = True
                valid_blockers = [-1]
            closest_blocker_col = max(valid_blockers)
            used_matrix[guard_row, closest_blocker_col + 1 : guard_col] = 1
            guard_pos = (int(guard_row), int(closest_blocker_col + 1))
            guard_pos_with_direction = (guard_pos[0], guard_pos[1], direction)
            if guard_pos_with_direction in guard_pos_list:
                is_loop = True
            guard_pos_list.add(guard_pos_with_direction)

        direction_idx = (direction_idx + 1) % 4
    return None


non_blockers = np.where(original_matrix == ".")
non_blockers = list(
    zip([int(r) for r in non_blockers[0]], [int(c) for c in non_blockers[1]])
)

total_loops = 0
for non_blocker in non_blockers:
    result = check_maze(original_matrix, non_blocker)
    if result:
        total_loops += 1
        print(result)
print(total_loops)
