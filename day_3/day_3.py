import re

expression = re.compile("[^A-Za-z0-9.\n]")

with (open("./input", "r") as f):
    lines = f.readlines()

    total = 0
    for line_number, line in enumerate(lines):
        # find all numbers and indices in line (start, end, number)
        numbers_in_line = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(r'\d+', line)]
        numbers_found_in_line = []

        for start, end, number in numbers_in_line:  # iterate over each number in the current line
            adjacent_chars = ""

            for index_in_line in range(start, end):  # iterate over all digits

                try:
                    a1 = lines[line_number - 1][index_in_line - 1]
                except:
                    pass
                try:
                    a2 = lines[line_number - 1][index_in_line]
                except:
                    pass
                try:
                    a3 = lines[line_number - 1][index_in_line + 1]
                except:
                    pass
                try:
                    b1 = line[index_in_line - 1]
                except:
                    pass
                try:
                    b2 = line[index_in_line + 1]
                except:
                    pass
                try:
                    c1 = lines[line_number + 1][index_in_line - 1]
                except:
                    pass
                try:
                    c2 = lines[line_number + 1][index_in_line]
                except:
                    pass
                try:
                    c3 = lines[line_number + 1][index_in_line + 1]
                except:
                    pass
                adjacent_chars = adjacent_chars + a1 + a2 + a3 + b1 + b2 + c1 + c2 + c3

            if expression.findall(adjacent_chars):
                numbers_found_in_line.append((number, adjacent_chars))
                total += int(number)

        print(line_number, numbers_found_in_line)

print(total)
