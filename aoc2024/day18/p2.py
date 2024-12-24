import sys

import networkx as nx
import numpy as np

sys.setrecursionlimit(10000)

SIDE = 71
FELL_BYTES = 1024
START = (0, 0)
END = (SIDE - 1, SIDE - 1)

with open("./aoc2024/day18/data1.txt", "r") as file:
    lines = file.read().split("\n")
    coords = [line.split(",") for line in lines]
    coords = [(int(coord[1]), int(coord[0])) for coord in coords]


def print_matrix(matrix):
    breakpoint()
    lines = "\n".join(["".join(line) for line in matrix])
    print(lines)


original_matrix = np.reshape(["."] * (SIDE * SIDE), (SIDE, SIDE))


def build_graph(matrix, graph, from_node):
    for i in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        next_coords = (from_node[0] + i[0], from_node[1] + i[1])
        if (
            next_coords[0] < 0
            or next_coords[0] >= SIDE
            or next_coords[1] < 0
            or next_coords[1] >= SIDE
        ):
            continue
        if matrix[next_coords] == "#":
            continue

        if graph.has_edge(from_node, next_coords):
            continue
        graph.add_edge(from_node, next_coords)

        if next_coords == END:
            continue
        build_graph(matrix, graph, next_coords)


start = FELL_BYTES
end = len(coords)

while True:
    if abs(end - start) <= 1:
        break
    mid_point = (end + start) // 2
    matrix = original_matrix.copy()
    for i in range(mid_point):
        matrix[coords[i]] = "#"
    G = nx.Graph()
    G.add_node(START)
    build_graph(matrix, G, START)
    if G.has_node(END):
        start = mid_point
    else:
        end = mid_point

print(coords[start][::-1])
