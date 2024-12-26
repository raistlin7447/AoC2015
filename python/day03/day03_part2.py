from collections import defaultdict

houses = defaultdict(int)
houses[(0, 0)] += 2
santa_location = [0, 0]
robot_location = [0, 0]
santa_turn = True

for direction in open("day03_input.txt").read():
    if santa_turn:
        location = santa_location
    else:
        location = robot_location
    santa_turn = not santa_turn

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