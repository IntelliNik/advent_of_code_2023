import re

amount_of_dice = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def check_game(rounds: [str]):
    game_possible = True
    at_least_red = 0
    at_least_green = 0
    at_least_blue = 0

    for round in rounds:
        for draw in re.split(',', round):
            if draw.find("red") != -1:
                number = get_number(draw)
                game_possible &= (number <= 12)
                at_least_red = max(at_least_red, number)
            if draw.find("green") != -1:
                number = get_number(draw)
                game_possible &= (number <= 13)
                at_least_green = max(at_least_green, number)
            if draw.find("blue") != -1:
                number = get_number(draw)
                game_possible &= (number <= 14)
                at_least_blue = max(at_least_blue, number)
    return game_possible, at_least_red, at_least_green, at_least_blue


def get_number(string):
    return int(re.findall(r'\d+', string)[0])

f = open("input", "r")
next_line = f.readline()
total = 0
total_power = 0
while next_line:
    if next_line == "":
        continue
    next_line = next_line[:-1]  # remove \n

    game, rounds = re.split(":", next_line)
    game_id = int(game[5:8])
    rounds = re.split(";", rounds)

    game_possible, red, green, blue = check_game(rounds)
    if game_possible:
        total += game_id
        #print("Game possible", game_id, rounds, total)
    else:
        #print("Game impossible", game_id, rounds)
        pass

    power = red * green * blue
    total_power += power
    print(rounds, red, green, blue)

    next_line = f.readline()

print(total, total_power)