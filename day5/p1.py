with open("./day5/data1.txt") as f:
    rules, updates = f.read().split("\n\n")
    rules = rules.split("\n")
    updates = updates.split("\n")

rules_dict = {}

for rule in rules:
    before, after = rule.split("|")
    rules_dict[before] = rules_dict.get(before, set())
    rules_dict[before].add(after)


def get_update_middle_value(update):
    values = update.split(",")
    for idx, v in enumerate(values):
        expected_after = rules_dict.get(v, set())
        actual_before = set(values[:idx])
        if expected_after.intersection(actual_before):
            return 0
    return values[len(values) // 2]


total = 0
for update in updates:
    middle_value = get_update_middle_value(update)
    total += int(middle_value)

print(total)
