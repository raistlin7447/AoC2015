presents = open("day02_input.txt").read().splitlines()

total = 0
for present in presents:
    l, w, h = map(int, present.split("x"))
    s1 = 2*l*w
    s2 = 2*w*h
    s3 = 2*h*l

    total += s1+s2+s3+min(s1, s2, s3)//2

print(total)