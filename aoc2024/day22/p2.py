with open("./aoc2024/day22/data1.txt", "r") as file:
    lines = file.read().split("\n")
    inputs = [int(line.strip()) for line in lines]

TIMES = 2000


def mix(v1, v2):
    return v1 ^ v2


def prune(val):
    return val % 16777216


def compute_next(secret):
    secret = mix(secret, secret << 6)
    secret = prune(secret)

    secret = mix(secret, secret >> 5)
    secret = prune(secret)

    secret = mix(secret, secret * 2048)
    secret = prune(secret)

    return secret


all_sequences = {}

for idx, val in enumerate(inputs):
    sequences = {}
    diffs = []
    diff_window = ()
    for i in range(TIMES):
        val_digit = val % 10
        val = compute_next(val)
        next_val_digit = val % 10
        diff = next_val_digit - val_digit
        diffs.append(diff)
        diff_window = (*diff_window[-3:], diff)
        sequences[diff_window] = sequences.get(diff_window, next_val_digit)

    for k, v in sequences.items():
        all_sequences[k] = all_sequences.get(k, 0) + v

best_sequence = sorted(all_sequences.items(), key=lambda x: x[1])[-1]
print(best_sequence)
