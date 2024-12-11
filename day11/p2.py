from collections import Counter
from functools import cache

with open("./day11/data1.txt", "r") as file:
    original_numbers = [int(n) for n in file.read().strip().split(" ")]


@cache
def apply_rules(number):
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        number_str = str(number)
        first_part = number_str[0 : len(number_str) // 2]
        second_part = number_str[len(number_str) // 2 :]
        return [int(first_part), int(second_part)]
    else:
        return [number * 2024]


def transform_stones(numbers, times):
    counter = Counter(numbers)
    for i in range(times):
        new_counter = Counter()
        for number, count in counter.items():
            for new_number in apply_rules(number):
                new_counter[new_number] += count
        counter = new_counter
    print(sum(counter.values()))


transform_stones(original_numbers, 75)
