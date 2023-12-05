with (open("./input", "r") as f):
    lines = f.readlines()

amount_of_cards = len(lines)
cards_to_process = list(range(len(lines)))


def countX(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


def copy_cards(start_index, amount, cards_to_process, amount_of_cards):
    index = start_index + 1
    new_cards = []
    for _ in range(0, amount):
        cards_to_process += [index]
        amount_of_cards += 1
        index += 1

    return cards_to_process, amount_of_cards


def convert_int(list):
    new_list = []
    for e in list:
        if not e:
            continue
        new_list += [int(e)]
    return new_list


while cards_to_process:
    print(cards_to_process[0], len(cards_to_process), amount_of_cards)
    card_index = cards_to_process.pop(0)
    line = lines[card_index]

    list_to_int = line.split("|")
    winning_numbers = list_to_int[0].split(":")[1][1:-1].split(" ")
    winning_numbers = convert_int(winning_numbers)
    numbers_you_have = list_to_int[1][1:-1].split(" ")
    numbers_you_have = convert_int(numbers_you_have)

    matching_numbers = 0
    for number in numbers_you_have:
        if number in winning_numbers:
            matching_numbers += 1

    cards_to_process, amount_of_cards = copy_cards(card_index, matching_numbers, cards_to_process, amount_of_cards)
    cards_to_process.sort()


print("Final amount", amount_of_cards)
