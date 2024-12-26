from collections import Counter

floor = 0
for i, c in enumerate(open("day01_input.txt").read(), start=1):
    match c:
        case "(":
            floor += 1
        case ")":
            floor -= 1
    if floor == -1:
        print(i)
        break
