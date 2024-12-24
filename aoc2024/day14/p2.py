import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.stride_tricks import sliding_window_view

with open("./aoc2024/day14/data1.txt") as f:
    lines = f.readlines()

# SIDES = (11, 7)
SIDES = (101, 103)

matrix = np.zeros(SIDES)


def parse_robot(line):
    pos, spd = line.split(" ")
    pos = pos.split("=")[1]
    spd = spd.split("=")[1]
    x, y = (int(v) for v in pos.split(","))
    vx, vy = (int(v) for v in spd.split(","))
    return [x, y, vx, vy]


robots = [parse_robot(line) for line in lines]

for r in robots:
    x, y, vx, vy = r
    matrix[x, y] += 1


def save_image(matrix, turn):
    transpose = matrix.T
    win = sliding_window_view(transpose, (5, 2))
    for i in win:
        for j in i:
            if np.prod(j):
                plt.imsave(f"./day14/images/t_{turn}.png", matrix.T)
                print(f"possible tree at {turn}")
                return


turn = 0

while True:
    has_tree = save_image(matrix, turn)
    matrix = np.zeros(SIDES)
    for robot in robots:
        x, y, vx, vy = robot
        next_x = (x + vx) % SIDES[0]
        next_y = (y + vy) % SIDES[1]
        robot[0] = next_x
        robot[1] = next_y
        matrix[next_x, next_y] += 1
    turn += 1
    if turn % 1000 == 0:
        print(turn)
