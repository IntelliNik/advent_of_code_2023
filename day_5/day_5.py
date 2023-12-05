from collections import defaultdict

with open("input", "r") as f:
    lines = f.readlines()

seeds = lines[0].split(":")[1][1:-1].split(" ")


def map_to_next(source, number):
    for id, line in enumerate(lines):
        if f"{source}-to" in line:
            dest_name = line.split(" ")[0].split("-")[2]
            break

    id += 1
    while lines[id] != "\n":
        dest, source, r = lines[id].split(" ")
        if source <= number <= source + r:
            return dest_name, dest + r
        id += 1

    return dest_name, number


for seed in seeds:
    target = ""
    while target != "location":
        target, number = map_to_next("seed", seed)
        print(target, number)
