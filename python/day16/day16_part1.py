import re

scanner = {
    "children": "3",
    "cats": "7",
    "samoyeds": "2",
    "pomeranians": "3",
    "akitas": "0",
    "vizslas": "0",
    "goldfish": "5",
    "trees": "3",
    "cars": "2",
    "perfumes": "1"}

for sue in open("day16_input.txt").read().splitlines():
    sue_number = re.match(r"Sue (\d+)", sue)
    items = re.findall(r"(\w+): (\d+)", sue)
    for item in items:
        if scanner[item[0]] != item[1]:
            break
    else:
        break

print(sue_number.group(1))