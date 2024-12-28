import itertools

cities = []
distances = {}

for distance in open("day09_input.txt").read().splitlines():
    city_names, length = distance.split(" = ")
    city1, city2 = city_names.split(" to ")
    if city1 not in cities:
        cities.append(city1)
    if city2 not in cities:
        cities.append(city2)
    distances[(city1, city2)] = int(length)
    distances[(city2, city1)] = int(length)

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        city_pair = (route[i], route[i + 1])
        total_distance += distances[city_pair]
    return total_distance

all_routes = itertools.permutations(cities)

minsize_distance = 0
for route in all_routes:
    distance = calculate_total_distance(route)
    minsize_distance = max(minsize_distance, distance)

print(minsize_distance)