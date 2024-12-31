from itertools import combinations, chain

containers = map(int, open("day17_input.txt").read().splitlines())

def powerset(iterable):
    "Subsequences of the iterable from shortest to longest."
    # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

total = 0
for combination in powerset(list(containers)):
    if sum(combination) == 150:
        total += 1

print(total)