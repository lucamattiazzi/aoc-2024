from aoc2024.day21.graphs import dirpad_G, get_dir_path, get_num_path, numpad_G

with open("./aoc2024/day21/ex1.txt", "r") as f:
    data = f.read().split("\n")


def get_final_path(target):
    numpad_path = []
    for i in range(len(target) - 1):
        path = get_num_path(target[i], target[i + 1])
        next_path = [
            numpad_G[path[i]][path[i + 1]]["movement"] for i in range(len(path) - 1)
        ]
        numpad_path.extend(next_path)

        numpad_path.extend(["A"])
    print("".join(numpad_path))

    numpad_path = ["A", *numpad_path]
    dirpad_path_1 = []

    for i in range(len(numpad_path) - 1):
        path = get_dir_path(numpad_path[i], numpad_path[i + 1])
        next_path = [
            dirpad_G[path[i]][path[i + 1]]["movement"] for i in range(len(path) - 1)
        ]
        dirpad_path_1.extend(next_path)

        dirpad_path_1.extend(["A"])
    print("".join(dirpad_path_1))

    dirpad_path_1 = ["A", *dirpad_path_1]
    dirpad_path_2 = []

    for i in range(len(dirpad_path_1) - 1):
        path = get_dir_path(dirpad_path_1[i], dirpad_path_1[i + 1])
        next_path = [
            dirpad_G[path[i]][path[i + 1]]["movement"] for i in range(len(path) - 1)
        ]
        dirpad_path_2.extend(next_path)

        dirpad_path_2.extend(["A"])
    print("".join(dirpad_path_2))

    return "".join(dirpad_path_2)


total_complexity = 0

for line in data:
    target = f"A{line}"
    print(target)
    total_path = get_final_path(target)
    numerical_part = line.replace("A", "")
    complexity = int(numerical_part) * len(total_path)
    total_complexity += complexity

print(total_complexity)
