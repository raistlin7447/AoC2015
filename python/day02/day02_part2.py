presents = open("day02_input.txt").read().splitlines()

total = 0
for present in presents:
    l, w, h = map(int, present.split("x"))
    p1 = 2 * l + 2 * w
    p2 = 2 * w + 2 * h
    p3 = 2 * h + 2 * l
    v = l * w * h

    total += min(p1, p2, p3) + v

print(total)
