from collections import defaultdict

houses = defaultdict(int)
location = [0, 0]
houses[tuple(location)] += 1

for direction in open("day03_input.txt").read():
    match direction:
        case "^":
            location[0] += 1
        case "v":
            location[0] -= 1
        case ">":
            location[1] += 1
        case "<":
            location[1] -= 1
    houses[tuple(location)] += 1

print(len(houses))