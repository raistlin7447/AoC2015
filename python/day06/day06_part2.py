grid_size = 1000
light_grid = [[0 for i in range(grid_size)] for j in range(grid_size)]

instructions = open("day06_input.txt").read().splitlines()

for instruction in instructions:
    split_instruction = instruction.split()
    turn_on = None
    if instruction.startswith("turn on"):
        turn_on = True
        start = list(map(int, split_instruction[2].split(",")))
        end = list(map(int, split_instruction[4].split(",")))
    elif instruction.startswith("turn off"):
        turn_on = False
        start = list(map(int, split_instruction[2].split(",")))
        end = list(map(int, split_instruction[4].split(",")))
    else:
        start = list(map(int, split_instruction[1].split(",")))
        end = list(map(int, split_instruction[3].split(",")))

    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            match turn_on:
                case True:
                    light_grid[i][j] += 1
                case False:
                    if light_grid[i][j] > 0:
                        light_grid[i][j] -= 1
                case None:
                    light_grid[i][j] += 2
                case _:
                    print("huh?")

total = 0
for i in range(grid_size):
    for j in range(grid_size):
        if light_grid[i][j]:
            total += light_grid[i][j]

print(total)