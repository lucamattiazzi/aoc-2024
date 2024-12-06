with open("./day4/data1.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]

LENGTH = 4
SIDE = len(lines)


def get_horizontal_right(lines: list[list[str]], x: int, y: int):
    if x + LENGTH > SIDE:
        return ""
    return "".join(lines[y][x : x + LENGTH])


def get_diagonal_right_down(lines: list[list[str]], x: int, y: int):
    if x + LENGTH > SIDE or y + LENGTH > SIDE:
        return ""
    diagonal = ""
    for i in range(LENGTH):
        diagonal += lines[y + i][x + i]
    return diagonal


def get_vertical_down(lines: list[list[str]], x: int, y: int):
    if y + LENGTH > SIDE:
        return ""
    vertical = ""
    for i in range(LENGTH):
        vertical += lines[y + i][x]
    return vertical


def get_diagonal_left_down(lines: list[list[str]], x: int, y: int):
    if x - LENGTH + 1 < 0 or y + LENGTH > SIDE:
        return ""
    diagonal = ""
    for i in range(LENGTH):
        diagonal += lines[y + i][x - i]
    return diagonal


def get_horizontal_left(lines: list[list[str]], x: int, y: int):
    if x - LENGTH + 1 < 0:
        return ""
    horizontal = lines[y][x - LENGTH + 1 : x + 1]
    return "".join(horizontal)


def get_diagonal_left_up(lines: list[list[str]], x: int, y: int):
    if x - LENGTH + 1 < 0 or y - LENGTH + 1 < 0:
        return ""
    diagonal = ""
    for i in range(LENGTH):
        diagonal += lines[y - i][x - i]
    return diagonal


def get_vertical_up(lines: list[list[str]], x: int, y: int):
    if y - LENGTH + 1 < 0:
        return ""
    vertical = ""
    for i in range(LENGTH):
        vertical += lines[y - i][x]
    return vertical


def get_diagonal_right_up(lines: list[list[str]], x: int, y: int):
    if x + LENGTH > SIDE or y - LENGTH + 1 < 0:
        return ""
    diagonal = ""
    for i in range(LENGTH):
        diagonal += lines[y - i][x + i]
    return diagonal


def main(lines: list[list[str]]):
    total = 0
    # new_matrix = [["." * 10] * 10]
    for y in range(SIDE):
        line = lines[y]
        x_indexes = [i for i, x in enumerate(line) if x == "X"]
        for x in x_indexes:
            all_lines = [
                get_horizontal_right(lines, x, y),
                get_diagonal_right_down(lines, x, y),
                get_vertical_down(lines, x, y),
                get_diagonal_left_down(lines, x, y),
                get_horizontal_left(lines, x, y),
                get_diagonal_left_up(lines, x, y),
                get_vertical_up(lines, x, y),
                get_diagonal_right_up(lines, x, y),
            ]
            for idx, line in enumerate(all_lines):
                if line in ["XMAS", "SAMX"]:
                    total += 1
                    print((x, y), idx, line)
    print(total)


main(lines)
