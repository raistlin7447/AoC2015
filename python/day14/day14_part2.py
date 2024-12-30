import re
from collections import defaultdict

regex = re.compile(r"(.*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.")

reindeer = list(re.findall(regex, open("day14_input.txt").read()))


def get_winner(race_time):
    distances = {}
    for name, speed, travel_time, rest_time in reindeer:
        speed = int(speed)
        travel_time = int(travel_time)
        rest_time = int(rest_time)
        q, r = divmod(race_time, travel_time + rest_time)
        distance = (q * travel_time + min(r, travel_time)) * speed
        distances[name] = distance
    return max(distances, key=distances.get)


scores = defaultdict(int)
total_time = 2503
for i in range(1, total_time+1):
    scores[get_winner(i)] += 1

print(max(scores.values()))
