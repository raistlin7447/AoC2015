from collections import Counter

c = Counter(open("day01_input.txt").read())

print(c["("]-c[")"])