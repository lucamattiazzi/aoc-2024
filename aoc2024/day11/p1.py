from functools import lru_cache

with open("./aoc2024/day11/ex1.txt", "r") as file:
    original_numbers = [int(n) for n in file.read().strip().split(" ")]


@lru_cache(maxsize=None)
def apply_rules(number, times):
    if times == 0:
        result = [number]
        return result

    if number == 0:
        return apply_rules(1, times - 1)
    elif len(str(number)) % 2 == 0:
        number_str = str(number)
        first_part = number_str[0 : len(number_str) // 2]
        second_part = number_str[len(number_str) // 2 :]
        return [
            *apply_rules(int(first_part), times - 1),
            *apply_rules(int(second_part), times - 1),
        ]
    else:
        return apply_rules(number * 2024, times - 1)


def transform_stones(numbers, times):
    final_result = []
    for number in numbers:
        print(f"starting {number}")
        final_result += apply_rules(number, times)
        print(f"done with {number}")
    print(final_result)
    print(apply_rules.cache_info())


transform_stones(original_numbers, 6)
