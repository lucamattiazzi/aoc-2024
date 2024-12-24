from sympy import simplify_logic, symbols

with open("./aoc2024/day24/data1.txt", "r") as file:
    values, ops = file.read().split("\n\n")

    values = [v.split(": ") for v in values.split("\n")]
    ops = [o.split(" -> ") for o in ops.split("\n")]

    original_values = {v[0]: bool(int(v[1])) for v in values}
    values = {v[0]: symbols(v[0]) for v in values}
    ops = {o[1]: o[0] for o in ops}

    values = {**values, **ops}

OPS = {
    "AND": lambda v1, v2: v1 & v2,
    "OR": lambda v1, v2: v1 | v2,
    "XOR": lambda v1, v2: v1 ^ v2,
}


def compute_op(values, op):
    [v1, operator, v2] = op.split(" ")
    return OPS[operator](compute_value(values, v1), compute_value(values, v2))


def compute_value(values, key):
    if isinstance(values[key], str):
        values[key] = compute_op(values, values[key])
    return values[key]


for key, value in values.items():
    if key.startswith("z"):
        subs_map = {k: v for k, v in original_values.items() if k[1:3] != key[1:3]}
        value = compute_value(values, key)
        simplified = value.subs(subs_map)
        # print(f"{key} = {simplified}")
        solved = value.subs(original_values)
        if key[1:3] == "45":
            continue
        correct = original_values[f"x{key[1:3]}"] & original_values[f"y{key[1:3]}"]
        if not correct:
            print(f"{key} is wrong")
