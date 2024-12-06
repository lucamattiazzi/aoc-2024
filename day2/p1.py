reports = []

with open("./day2/data1.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        values = [int(i) for i in line.split()]
        reports.append(values)


def is_valid_report(report: list[int]) -> bool:
    direction = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if direction is None:
            direction = diff
        if diff == 0:
            return False
        if diff * direction < 0:
            return False
        if abs(diff) > 3:
            return False
    return True


valid_reports = [report for report in reports if is_valid_report(report)]

print(len(valid_reports))
