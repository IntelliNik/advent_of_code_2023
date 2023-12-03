import re
from collections import defaultdict

expression = re.compile("[^A-Za-z0-9.\n]")

possible_gears = defaultdict(list)


def add_possible_gear(line, index, number):
    char = lines[line][index]
    if char == "*":
        possible_gears[f"{line}_{index}"] += [number]


with (open("./input", "r") as f):
    lines = f.readlines()

    total = 0
    for line_number, line in enumerate(lines):
        # possible_gears[line_number] = defaultdict(list)
        # find all numbers and indices in line (start, end, number)
        numbers_in_line = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(r'\d+', line)]
        numbers_found_in_line = []

        for start, end, number in numbers_in_line:  # iterate over each number in the current line
            adjacent_chars = ""

            for index_in_line in range(start, end):  # iterate over all digits
                char = None
                try:
                    add_possible_gear(line_number - 1, index_in_line - 1, number)
                    adjacent_chars += char
                except:
                    pass
                try:
                    add_possible_gear(line_number - 1, index_in_line, number)
                    adjacent_chars += char
                except:
                    pass
                try:
                    add_possible_gear(line_number - 1, index_in_line + 1, number)
                    adjacent_chars += char
                except:
                    pass
                try:
                    add_possible_gear(line_number, index_in_line - 1, number)
                    adjacent_chars += char
                except:
                    pass
                try:
                    add_possible_gear(line_number, index_in_line + 1, number)
                    adjacent_chars += char
                except:
                    pass
                try:
                    add_possible_gear(line_number + 1, index_in_line - 1, number)
                    adjacent_chars += char
                except:
                    pass
                try:
                    add_possible_gear(line_number + 1, index_in_line, number)
                    adjacent_chars += char
                except:
                    pass
                try:
                    add_possible_gear(line_number + 1, index_in_line + 1, number)
                    adjacent_chars += char
                except:
                    pass

            adjacent_symbols = expression.findall(adjacent_chars)
            if adjacent_symbols:
                numbers_found_in_line.append((number, adjacent_chars))
                total += int(number)

        print(line_number, numbers_found_in_line)

print(total)

# remove duplicate parts


total_gear_ratio = 0
for key in possible_gears.keys():
    possible_gears[key] = list(dict.fromkeys(possible_gears[key]))

for key in possible_gears.keys():
    value = possible_gears[key]
    if len(value) == 2:
        gear_ratio = int(value[0]) * int(value[1])
        total_gear_ratio += gear_ratio

print(possible_gears)
print(total_gear_ratio)
