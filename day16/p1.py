import sys

import networkx as nx
import numpy as np

sys.setrecursionlimit(10000)

with open("./day16/data1.txt", "r") as file:
    content = file.read()
    matrix = np.array([list(line.strip()) for line in content.split("\n")])


def print_matrix(matrix):
    lines = "\n".join(["".join(line) for line in matrix])
    print(lines)


DIRECTIONS = [">", "v", "<", "^"]
DIFF = {">": [0, 1], "<": [0, -1], "^": [-1, 0], "v": [1, 0]}

start_direction = ">"

start = np.where(matrix == "S")
start_coords = (int(start[0][0]), int(start[1][0]))

end_nodes = []


def build_graph(matrix, graph, from_node):
    from_coords, from_direction, _ = from_node
    from_direction_idx = DIRECTIONS.index(from_direction)
    for i in [-1, 0, 1]:
        next_direction_idx = (from_direction_idx + i) % len(DIRECTIONS)
        next_direction = DIRECTIONS[next_direction_idx]
        diff = DIFF[next_direction]
        next_coords = (from_coords[0] + diff[0], from_coords[1] + diff[1])
        if matrix[next_coords] == "#":
            continue
        next_node = (next_coords, next_direction, from_coords)
        weight = 1 if next_direction == from_direction else 1001
        edge = (from_node, next_node, weight)
        if graph.has_node(next_node):
            graph.add_weighted_edges_from([edge])
            continue
        graph.add_node(next_node)
        graph.add_weighted_edges_from([edge])
        if matrix[next_coords] == "E":
            end_nodes.append(next_node)
        else:
            build_graph(matrix, graph, next_node)


G = nx.DiGraph()
start_node = (start_coords, start_direction, start_coords)
G.add_node(start_node)
build_graph(matrix, G, start_node)

winning_path = None
winning_weight = np.inf

for end_node in end_nodes:
    shortest_paths = nx.all_shortest_paths(
        G, source=start_node, target=end_node, weight="weight"
    )
    shortest_path_weight = nx.shortest_path_length(
        G, source=start_node, target=end_node, weight="weight"
    )

    if shortest_path_weight < winning_weight:
        winning_path = shortest_paths
        winning_weight = shortest_path_weight

for node in winning_path:
    coords, direction, _ = node
    matrix[coords] = "O"
print_matrix(matrix)
print("\n\n")

print(winning_weight)
