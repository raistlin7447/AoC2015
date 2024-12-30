from collections import defaultdict
import re
from itertools import product

regex = re.compile(r"(.*): capacity (-?\d*), durability (-?\d*), flavor (-?\d*), texture (-?\d*), calories (-?\d*)")

ingredient_input = re.findall(regex, open("day15_input.txt").read())

ingredients = defaultdict(dict)
for ingredient, capacity, durability, flavor, texture, calories in ingredient_input:
    ingredients[ingredient]["capacity"] = int(capacity)
    ingredients[ingredient]["durability"] = int(durability)
    ingredients[ingredient]["flavor"] = int(flavor)
    ingredients[ingredient]["texture"] = int(texture)
    ingredients[ingredient]["calories"] = int(calories)

ingredient_names = ingredients.keys()
all_nums = product(range(0, 101), repeat=len(ingredient_names) - 1)

best_score = 0
for option in all_nums:
    if sum(option) > 99:
        continue
    quantities = list(option) + [100 - sum(option)]

    capacity_score = 0
    durability_score = 0
    flavor_score = 0
    texture_score = 0
    calories = 0

    for ingredient_number, ingredient_name in enumerate(ingredient_names):
        capacity_score += ingredients[ingredient_name]["capacity"] * quantities[ingredient_number]
        durability_score += ingredients[ingredient_name]["durability"] * quantities[ingredient_number]
        flavor_score += ingredients[ingredient_name]["flavor"] * quantities[ingredient_number]
        texture_score += ingredients[ingredient_name]["texture"] * quantities[ingredient_number]
        calories += ingredients[ingredient_name]["calories"] * quantities[ingredient_number]

    if calories == 500:
        if capacity_score < 0:
            capacity_score = 0
        if durability_score < 0:
            durability_score = 0
        if flavor_score < 0:
            flavor_score = 0
        if texture_score < 0:
            texture_score = 0

        score = capacity_score * durability_score * flavor_score * texture_score
        best_score = max(best_score, score)

print(best_score)