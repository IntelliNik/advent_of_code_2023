numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

numbers_reversed = {}
for key in numbers.keys():
    numbers_reversed[key[::-1]] = numbers[key]


def find_first_digit(string, reversed=False):
    numbers_array = numbers_reversed if reversed else numbers

    current_word = ""
    for char in string:
        if char.isdigit():
            return int(char)
        else:
            current_word += char
            # check if spelled word is found in current substring
            for key in numbers_array.keys():
                spelled_word = current_word.find(key)
                if spelled_word != -1:
                    # found a spelled word!
                    return numbers_array[key]

    assert False  # no digit found!

total = 0
f = open("input", "r")
next_line = f.readline()
while next_line:
    left = find_first_digit(next_line)
    right = find_first_digit(next_line[::-1], reversed=True)

    calibration_value = int(str(left) + str(right))
    total += calibration_value

    print(next_line[:-1], left, right, calibration_value, total)

    next_line = f.readline()
