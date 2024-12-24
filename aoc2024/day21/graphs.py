from functools import cache

import networkx as nx

numpad_G = nx.DiGraph()

numpad_G.add_edge("A", "0", movement="<")
numpad_G.add_edge("A", "3", movement="^")

numpad_G.add_edge("0", "A", movement=">")
numpad_G.add_edge("0", "2", movement="^")

numpad_G.add_edge("1", "2", movement=">")
numpad_G.add_edge("1", "4", movement="^")

numpad_G.add_edge("2", "1", movement="<")
numpad_G.add_edge("2", "3", movement=">")
numpad_G.add_edge("2", "0", movement="v")
numpad_G.add_edge("2", "5", movement="^")

numpad_G.add_edge("3", "A", movement="v")
numpad_G.add_edge("3", "2", movement="<")
numpad_G.add_edge("3", "6", movement="^")

numpad_G.add_edge("4", "7", movement="^")
numpad_G.add_edge("4", "5", movement=">")
numpad_G.add_edge("4", "1", movement="v")

numpad_G.add_edge("5", "8", movement="^")
numpad_G.add_edge("5", "6", movement=">")
numpad_G.add_edge("5", "2", movement="v")
numpad_G.add_edge("5", "4", movement="<")

numpad_G.add_edge("6", "9", movement="^")
numpad_G.add_edge("6", "3", movement="v")
numpad_G.add_edge("6", "5", movement="<")

numpad_G.add_edge("7", "4", movement="v")
numpad_G.add_edge("7", "8", movement=">")

numpad_G.add_edge("8", "5", movement="v")
numpad_G.add_edge("8", "9", movement=">")
numpad_G.add_edge("8", "7", movement="<")

numpad_G.add_edge("9", "6", movement="v")
numpad_G.add_edge("9", "8", movement="<")

dirpad_G = nx.DiGraph()


dirpad_G.add_edge("A", "^", movement="<")
dirpad_G.add_edge("A", ">", movement="v")

dirpad_G.add_edge("^", "A", movement=">")
dirpad_G.add_edge("^", "v", movement="v")

dirpad_G.add_edge(">", "v", movement="<")
dirpad_G.add_edge(">", "A", movement="^")

dirpad_G.add_edge("v", ">", movement=">")
dirpad_G.add_edge("v", "^", movement="^")
dirpad_G.add_edge("v", "<", movement="<")

dirpad_G.add_edge("<", "v", movement=">")


def get_best_path(G, all_paths):
    for path in all_paths:
        is_optimal_path = check_path(G, tuple(path))
        if is_optimal_path:
            return path
    return all_paths[-1]


def get_path(G, start, end):
    all_shortest_paths = list(nx.all_shortest_paths(G, start, end))
    if len(all_shortest_paths) == 1:
        return all_shortest_paths[0]
    best_path = get_best_path(G, all_shortest_paths)
    return best_path


@cache
def get_num_path(start, end):
    return get_path(numpad_G, start, end)


@cache
def get_dir_path(start, end):
    return get_path(dirpad_G, start, end)


def check_path(G, path):
    movements = [G[path[i]][path[i + 1]]["movement"] for i in range(len(path) - 1)]
    if len(movements) < 3:
        return True
    if movements[0] == movements[1] or movements[1] == movements[2]:
        return True
