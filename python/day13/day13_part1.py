import itertools
from collections import defaultdict

happiness = defaultdict(dict)

for relationship in open("day13_input.txt").read().splitlines():
    person1, gain_or_lose, amount, person2 = (relationship
                                              .replace("would ", "")
                                              .replace("happiness units by sitting next to ", "")
                                              [:-1].split())
    amount = int(amount)
    if gain_or_lose == "lose":
        amount = -amount

    happiness[person1][person2] = amount

def calculate_happiness(arrangement):
    total_happiness = 0
    n = len(arrangement)

    for i in range(n):
        left = arrangement[i]
        right = arrangement[(i + 1) % n]
        total_happiness += happiness[left][right] + happiness[right][left]

    return total_happiness

best_happiness = float('-inf')
for arrangement in itertools.permutations(happiness.keys()):
    total_happiness = calculate_happiness(arrangement)
    best_happiness = max(best_happiness, total_happiness)

print(best_happiness)
