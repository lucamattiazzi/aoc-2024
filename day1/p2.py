import re
from collections import Counter

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


counter = Counter(second)

total = 0

for i in first:
    if i in counter:
        total += counter[i] * i

print(total)
