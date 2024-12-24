from itertools import product

with open("./aoc2024/day7/data1.txt") as f:
    lines = [line.strip() for line in f.readlines()]

operations = []

for line in lines:
    solution, operation = line.split(":")
    operands = operation.strip().split(" ")
    operations.append([solution.strip(), operands])


valid_total = 0
VALID_OPERATORS = ["+", "*", "|"]


class FakeInt(int):
    def __or__(self, other):
        return FakeInt(f"{self}{other}")

    def __add__(self, other):
        return FakeInt(int.__add__(self, other))

    def __mul__(self, other):
        return FakeInt(int.__mul__(self, other))


for idx, operation in enumerate(operations):
    print(idx)
    solution, operands = operation
    operators = len(operands) - 1
    operators_combinations = product(VALID_OPERATORS, repeat=operators)
    for operators_combination in operators_combinations:
        open_brackets = "(" * operators
        equation = f"{open_brackets}FakeInt({operands[0]})"
        for i in range(operators):
            equation += f" {operators_combination[i]} FakeInt({operands[i+1]}))"
        value = eval(equation)
        if value == int(solution):
            valid_total += value
            break

print(valid_total)
