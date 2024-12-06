import re

with open("day3/data1.txt") as f:
    content = f.read()
    content = content.replace("\n", "")


regex = re.compile("mul(\(\d{1,3},\d{1,3}\))")

groups = regex.findall(content)
total = 0

for group in groups:
    nums = group[1:-1].split(",")
    total += int(nums[0]) * int(nums[1])
print(total)
