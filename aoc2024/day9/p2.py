with open("./aoc2024/day9/data1.txt") as file:
    line = file.read().strip()


def print_hd(hd):
    hd_str = ""
    for block in hd:
        hd_str += "".join([str(v) for v in block["values"]])
        remaning_empty = block["empty_size"]
        hd_str += "." * remaning_empty
    return hd_str


groups = list(line)
data_symbol = 0
hd = []
for i in range(len(groups)):
    length = int(groups[i])
    if i % 2 == 0:
        block = {
            "empty_size": 0,
            "values": [data_symbol] * length,
        }
        hd.append(block)
        data_symbol += 1
    elif length != 0:
        block = {"empty_size": length, "values": []}
        hd.append(block)

empty_blocks = [
    {**block, "idx": idx} for idx, block in enumerate(hd) if block["empty_size"]
]


def find_empty_block_idx(empty_blocks, current_idx, length):
    for block in empty_blocks:
        if block["empty_size"] >= length and block["idx"] < current_idx:
            block["empty_size"] -= length
            return block["idx"]
    return None


defragmenting_block_idx = -1

while True:
    if -defragmenting_block_idx >= len(hd):
        break
    last_block = hd[defragmenting_block_idx]
    if not last_block["values"]:
        defragmenting_block_idx -= 1
        continue
    values = last_block["values"]
    length = len(values)
    current_idx = len(hd) + defragmenting_block_idx
    empty_block_idx = find_empty_block_idx(empty_blocks, current_idx, length)
    if empty_block_idx is None:
        defragmenting_block_idx -= 1
        continue
    empty_block = hd[empty_block_idx]
    hd[empty_block_idx] = {
        "values": [*empty_block["values"], *values],
        "empty_size": empty_block["empty_size"] - length,
    }
    hd[defragmenting_block_idx] = {
        "values": [],
        "empty_size": length,
    }
    defragmenting_block_idx -= 1


all_values = []
for block in hd:
    all_values += block["values"]
    remaning_empty = block["empty_size"]
    all_values += [0] * remaning_empty

total = 0

for i in range(len(all_values)):
    total += all_values[i] * (i)
print(total)
