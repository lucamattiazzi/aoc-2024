from functools import cmp_to_key

with open("./day5/data1.txt") as f:
    rules, updates = f.read().split("\n\n")
    rules = rules.split("\n")
    updates = updates.split("\n")

rules_dict = {}

for rule in rules:
    before, after = rule.split("|")
    rules_dict[before] = rules_dict.get(before, set())
    rules_dict[before].add(after)


def check_is_ordered(update):
    values = update.split(",")
    for idx, v in enumerate(values):
        expected_after = rules_dict.get(v, set())
        actual_before = set(values[:idx])
        if expected_after.intersection(actual_before):
            return False
    return True


def comparison_fn(val_a, val_b):
    if val_a in rules_dict.get(val_b, set()):
        return -1
    if val_b in rules_dict.get(val_a, set()):
        return 1
    breakpoint()
    return 0


def get_correct_order(update):
    values = update.split(",")
    ordered_values = sorted(values, key=cmp_to_key(comparison_fn), reverse=True)
    return ordered_values[len(ordered_values) // 2]


total = 0
for update in updates:
    is_ordered = check_is_ordered(update)
    if is_ordered:
        continue
    correct_order_middle = get_correct_order(update)
    total += int(correct_order_middle)

print(total)
