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


all_numbers = set(rules_dict.keys())
for value in rules_dict.values():
    all_numbers.update(set(value))

all_numbers = list(all_numbers)


def sort_list(unsorted_list, rules_dict):
    def compare(val_a, val_b):
        if val_a in rules_dict.get(val_b, set()):
            return -1
        if val_b in rules_dict.get(val_a, set()):
            return 1
        return 0

    sorted_list = sorted(unsorted_list, key=cmp_to_key(compare), reverse=True)
    return sorted_list


ordered = sort_list(all_numbers, rules_dict)


def get_update_middle_value(update):
    values = update.split(",")
    indices = []
    for v in values:
        index = ordered.index(v)
        indices.append(index)
    for idx, current_val in enumerate(indices):
        next_val = indices[idx + 1] if idx + 1 < len(indices) else None
        if next_val is None:
            continue
        if current_val > next_val:
            return 0

    return values[len(values) // 2]


total = 0
for update in updates:
    middle_value = get_update_middle_value(update)
    total += int(middle_value)

print(total)

# def build_order(rules_dict):
#     order = []
#     all_numbers = set()

#     while True:
#         all_before = set()
#         for before, after in rules_dict.items():
#             all_numbers.add(before)
#             all_numbers.add(after)
#             all_before.add(before)
#     breakpoint()


# # build_order(rules)
