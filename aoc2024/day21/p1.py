with open("./aoc2024/day21/ex1.txt", "r") as f:
    data = f.read().split("\n")

BEST_MOVES = {
    "A": {"^": "<A", ">": "vA", "v": "<vA", "<": "v<<A"},
    "^": {
        "A": ">A",
        ">": "v>A",
        "v": "vA",
        "<": "v<A",
    },
    ">": {
        "A": "^A",
        "^": "<^A",
        "v": "<A",
        "<": "<<A",
    },
    "v": {
        "A": "^>A",
        ">": ">A",
        "<": "<A",
        "^": "^A",
    },
    "<": {
        "A": ">>^A",
        "^": ">^A",
        "v": ">A",
        ">": ">>A",
    },
}


total_complexity = 0

for line in data:
    target = f"A{line}"

print(total_complexity)
