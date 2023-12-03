import re

with open("/Users/nschulte/git/adventOfCode2023/day_3/input", "r") as f:
    lines = f.readlines()

    total = 0
    for line in lines:
        # (start, end, number)
        numbers_in_line = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(r'\d+', line)]
        for start, end, number in numbers_in_line:
            print(line[start-1], line[end+1])

        print(numbers_in_line, line)
        break
