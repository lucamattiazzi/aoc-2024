import re

with open("day3/data1.txt") as f:
    content = f.read()
    content = content.replace("\n", "")
    content = f"do(){content}don't()"

# regex = re.compile("do\(\).*?mul(\(\d{1,3},\d{1,3}\)).*?[don't\(\)|do\(\)]")
regex_valids = re.compile("do\(\).*?don't\(\)")
regex = re.compile("mul(\(\d{1,3},\d{1,3}\))")

valid_groups = regex_valids.findall(content)

total = 0
for group in valid_groups:
    mults = regex.findall(group)
    for mult in mults:
        nums = mult[1:-1].split(",")
        total += int(nums[0]) * int(nums[1])


# for group in groups:
#     nums = group[1:-1].split(",")
#     total += int(nums[0]) * int(nums[1])
print(total)
