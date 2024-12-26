import re

from sympy import simplify_logic, symbols

TO_BE_SWAPPED = [("gws", "nnt"), ("z13", "npf"), ("z19", "cph"), ("z33", "hgj")]

with open("./aoc2024/day24/data1.txt", "r") as file:
    values, ops = file.read().split("\n\n")

    values = [v.split(": ") for v in values.split("\n")]
    ops = [o.split(" -> ") for o in ops.split("\n")]

    sym_values = {v[0]: symbols(v[0]) for v in values}
    ops = {o[1]: o[0] for o in ops}

    sym_values = {**sym_values, **ops}

    values = {v[0]: bool(int(v[1])) for v in values}
    all_computed_values = {**values, **ops}

OPS = {
    "AND": lambda v1, v2: v1 & v2,
    "OR": lambda v1, v2: v1 | v2,
    "XOR": lambda v1, v2: v1 ^ v2,
}


def compute_op(vals, op):
    [v1, operator, v2] = op.split(" ")
    return OPS[operator](compute_value(vals, v1), compute_value(vals, v2))


def compute_value(vals, key):
    if isinstance(vals[key], str):
        vals[key] = compute_op(vals, vals[key])
    return vals[key]


sorted_sym_values = dict(sorted(sym_values.items(), key=lambda x: x[0]))
z_values = []

for key, value in sorted_sym_values.items():
    if re.match("z[0-9]{2}", key):
        print(key)
        subs_map = {k: v for k, v in values.items() if int(k[1:3]) < int(key[1:3])}
        value = compute_value(sorted_sym_values, key)
        simplified = value.subs(subs_map)
        print(f"{key} = {simplify_logic(simplified)}")
        computed_value = compute_value(all_computed_values, key)
        z_values.append((key, computed_value))

x_input = [int(v) for k, v in values.items() if k.startswith("x")]
y_input = [int(v) for k, v in values.items() if k.startswith("y")]
x_value = sum([n << i for i, n in enumerate(x_input)])
y_value = sum([n << i for i, n in enumerate(y_input)])

expected_value = x_value + y_value
z_bits = [int(couple[1]) for couple in z_values]
z_value = sum([n << i for i, n in enumerate(z_bits)])
