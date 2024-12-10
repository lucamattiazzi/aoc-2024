from itertools import product

with open("./day7/data1.txt") as f:
    lines = [line.strip() for line in f.readlines()]

operations = []

for line in lines:
    solution, operation = line.split(":")
    operands = operation.strip().split(" ")
    operations.append([solution.strip(), operands])


valid_total = 0
VALID_OPERATORS = ["+", "*"]

for operation in operations:
    solution, operands = operation
    operators = len(operands) - 1
    operators_combinations = product(VALID_OPERATORS, repeat=operators)
    for operators_combination in operators_combinations:
        open_brackets = "(" * operators
        equation = f"{open_brackets}{operands[0]}"
        for i in range(operators):
            equation += f" {operators_combination[i]} {operands[i+1]})"
        value = eval(equation)
        if value == int(solution):
            print(value)
            valid_total += value
            break

print(valid_total)
