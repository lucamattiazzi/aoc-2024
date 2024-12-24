with open("./aoc2024/day4/data1.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]

SIDE = len(lines)


def get_left_up(lines: list[list[str]], x: int, y: int):
    if x - 1 < 0 or y - 1 < 0:
        return ""
    return lines[y - 1][x - 1]


def get_right_up(lines: list[list[str]], x: int, y: int):
    if x + 1 >= SIDE or y - 1 < 0:
        return ""
    return lines[y - 1][x + 1]


def get_right_down(lines: list[list[str]], x: int, y: int):
    if x + 1 >= SIDE or y + 1 >= SIDE:
        return ""
    return lines[y + 1][x + 1]


def get_left_down(lines: list[list[str]], x: int, y: int):
    if x - 1 < 0 or y + 1 >= SIDE:
        return ""
    return lines[y + 1][x - 1]


def main(lines: list[list[str]]):
    total = 0
    for y in range(SIDE):
        line = lines[y]
        x_indexes = [i for i, x in enumerate(line) if x == "A"]
        for x in x_indexes:
            left_up = get_left_up(lines, x, y)
            right_up = get_right_up(lines, x, y)
            right_down = get_right_down(lines, x, y)
            left_down = get_left_down(lines, x, y)
            main_diagonal_right = (left_up == "M" and right_down == "S") or (
                left_up == "S" and right_down == "M"
            )
            main_diagonal_left = (right_up == "M" and left_down == "S") or (
                right_up == "S" and left_down == "M"
            )
            if main_diagonal_right and main_diagonal_left:
                total += 1

    print(total)


main(lines)
