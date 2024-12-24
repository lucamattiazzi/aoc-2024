import networkx as nx

with open("./aoc2024/day23/data1.txt", "r") as file:
    lines = file.read().split("\n")
    couples = [line.strip().split("-") for line in lines]

G = nx.Graph()

for couple in couples:
    G.add_edge(*couple)


biggest_clique = max([c for c in nx.find_cliques(G)], key=lambda x: len(x))
sorted_clique = sorted(biggest_clique)
print(",".join(sorted_clique))
