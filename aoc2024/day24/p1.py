with open("./aoc2024/day24/data1.txt", "r") as file:
    values, ops = file.read().split("\n\n")

    values = [v.split(": ") for v in values.split("\n")]
    ops = [o.split(" -> ") for o in ops.split("\n")]

    values = {v[0]: bool(int(v[1])) for v in values}
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
    if not isinstance(values[key], bool):
        values[key] = compute_op(values, values[key])
    return values[key]


z_bytes = {}
for key, value in values.items():
    if key.startswith("z"):
        value = compute_value(values, key)
        z_bytes[key] = value

total = sum([int(i[1]) << idx for idx, i in enumerate(sorted(z_bytes.items()))])
print(total)
