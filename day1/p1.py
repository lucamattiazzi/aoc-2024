import re

first = []
second = []

numbers_separated_by_spaces = re.compile(r"(\d+)\s+(\d+)")

with open("./data1.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        match = numbers_separated_by_spaces.match(line)
        g1 = match.group(1)
        g2 = match.group(2)
        first.append(int(g1))
        second.append(int(g2))

first.sort()
second.sort()

total_diff = 0
for i in range(len(first)):
    total_diff += abs(first[i] - second[i])

print(total_diff)
