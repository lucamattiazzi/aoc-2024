import numpy as np

with open("./aoc2024/day14/ex1.txt") as f:
    lines = f.readlines()

SIDES = (11, 7)
TURNS = 100
# SIDES = (101, 103)

start_matrix = np.zeros(SIDES)
end_matrix = np.zeros(SIDES)


def parse_robot(line):
    pos, spd = line.split(" ")
    pos = pos.split("=")[1]
    spd = spd.split("=")[1]
    x, y = (int(v) for v in pos.split(","))
    vx, vy = (int(v) for v in spd.split(","))
    return (x, y, vx, vy)


robot = [parse_robot(line) for line in lines]

for r in robot:
    x, y, vx, vy = r
    start_matrix[x, y] += 1

start_matrix = start_matrix.T
print(start_matrix)


def get_final_position(robot):
    x, y, vx, vy = robot
    final_x = (x + TURNS * vx) % SIDES[0]
    final_y = (y + TURNS * vy) % SIDES[1]
    return (final_x, final_y, vx, vy)


final_robots = [get_final_position(r) for r in robot]
for robot in final_robots:
    x, y, _, __ = robot
    end_matrix[x, y] += 1


end_matrix = end_matrix.T
print(end_matrix)

top_left = end_matrix[0 : SIDES[1] // 2, 0 : SIDES[0] // 2]
print(top_left)
top_right = end_matrix[0 : SIDES[1] // 2, SIDES[0] // 2 + 1 :]
print(top_right)
bottom_left = end_matrix[SIDES[1] // 2 + 1 :, 0 : SIDES[0] // 2]
print(bottom_left)
bottom_right = end_matrix[SIDES[1] // 2 + 1 :, SIDES[0] // 2 + 1 :]
print(bottom_right)

total = (
    np.sum(top_left) * np.sum(top_right) * np.sum(bottom_left) * np.sum(bottom_right)
)

print(total)
