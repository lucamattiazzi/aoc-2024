with open("./aoc2024/day9/data1.txt") as file:
    line = file.read().strip()


groups = list(line)
data_symbol = 0
hd = []
for i in range(len(groups)):
    if i % 2 == 0:
        hd += [str(data_symbol)] * int(groups[i])
        data_symbol += 1

defragged_hd = []

for i in range(len(groups)):
    pop_idx = 0 if i % 2 == 0 else -1
    for j in range(int(groups[i])):
        if not hd:
            break
        defragged_hd.append(hd.pop(pop_idx))

total = 0
for idx, value in enumerate(list(defragged_hd)):
    total += idx * int(value)
print(total)
