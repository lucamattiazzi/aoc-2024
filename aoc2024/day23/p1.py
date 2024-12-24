import networkx as nx

with open("./aoc2024/day23/data1.txt", "r") as file:
    lines = file.read().split("\n")
    couples = [line.strip().split("-") for line in lines]

G = nx.Graph()

for couple in couples:
    G.add_edge(*couple)


def has_chief(triplet):
    return bool([node for node in triplet if node[0] == "t"])


possible_triplets = 0

for cycle in nx.simple_cycles(G, length_bound=3):
    if has_chief(cycle):
        possible_triplets += 1

print(possible_triplets)
