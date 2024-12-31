from copy import deepcopy

lights = [[col for col in row] for row in open("day18_input.txt").read().splitlines()]

rows = len(lights)
cols = len(lights[0])

def turn_on_corners():
    lights[0][0] = "#"
    lights[rows-1][0] = "#"
    lights[0][cols-1] = "#"
    lights[rows-1][cols-1] = "#"

turn_on_corners()

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def next_state():
    old_state = deepcopy(lights)
    for i in range(rows):
        for j in range(cols):
            neighbors_on = 0
            for direction in DIRECTIONS:
                nx = i + direction[0]
                ny = j + direction[1]
                if 0 <= nx < rows and 0 <= ny < cols:
                    if old_state[nx][ny] == "#":
                        neighbors_on += 1
            match old_state[i][j], neighbors_on:
                case "#", 0 | 1 | 4 | 5 | 6 | 7 | 8:
                    lights[i][j] = "."
                case ".", 3:
                    lights[i][j] = "#"
    turn_on_corners()

for _ in range(100):
    next_state()

total = 0
for row in lights:
    for col in row:
        if col == "#":
            total += 1

print(total)