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
    for name, amount in items:
        if name in ["cats", "trees"] and amount <= scanner[name]:
            break

        if name in ["pomeranians", "goldfish"] and amount >= scanner[name]:
            break

        if name in ["children", "samoyeds", "akitas", "vizslas", "cars", "perfumes"] and scanner[name] != amount:
            break
    else:
        break

print(sue_number.group(1))