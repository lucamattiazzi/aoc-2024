import sys

import networkx as nx
import numpy as np

sys.setrecursionlimit(10000)

SIDE = 71
FELL_BYTES = 1024
START = (0, 0)
END = (SIDE - 1, SIDE - 1)

with open("./day18/data1.txt", "r") as file:
    lines = file.read().split("\n")
    coords = [line.split(",") for line in lines]
    coords = [(int(coord[1]), int(coord[0])) for coord in coords]

print(coords)


def print_matrix(matrix):
    breakpoint()
    lines = "\n".join(["".join(line) for line in matrix])
    print(lines)


matrix = np.reshape(["."] * (SIDE * SIDE), (SIDE, SIDE))

for i in range(FELL_BYTES):
    matrix[coords[i]] = "#"


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


G = nx.Graph()
G.add_node(START)
build_graph(matrix, G, START)
print(G)

path = nx.shortest_path(G, source=START, target=END)
for i in path:
    matrix[i] = "o"
# print_matrix(matrix)

print(nx.shortest_path_length(G, source=START, target=END))
