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


total = 0
for val in inputs:
    print(val)
    for i in range(TIMES):
        val = compute_next(val)
    total += val
    print(val)

print(total)
