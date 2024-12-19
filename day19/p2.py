with open("./day19/data1.txt") as file:
    all_patterns, strings = file.read().split("\n\n")
    all_patterns = all_patterns.split(", ")
    strings = strings.split("\n")

cache = {}


def find_pattern(patterns, string):
    if string in cache:
        return cache.get(string)
    for pattern in patterns:
        if string == pattern:
            cache[string] = cache.get(string, 0) + 1
            continue
        if not string[0 : len(pattern)] == pattern:
            continue
        if total := find_pattern(patterns, string[len(pattern) :]):
            cache[string] = cache.get(string, 0) + total
            continue

    cache[string] = cache.get(string, 0)
    return cache[string]


possible_patterns = 0

for string in strings:
    possible_patterns += find_pattern(all_patterns, string)
    print(string, find_pattern(all_patterns, string))

print(possible_patterns)
