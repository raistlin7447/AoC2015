import re

regex = re.compile(r"(.*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.")

reindeer = re.findall(regex, open("day14_input.txt").read())

distances = {}
total_time = 2503
for name, speed, travel_time, rest_time in reindeer:
    speed = int(speed)
    travel_time = int(travel_time)
    rest_time = int(rest_time)
    q, r = divmod(total_time, travel_time + rest_time)
    distance = (q * travel_time + min(r, travel_time)) * speed
    distances[name] = distance

print(max(distances.values()))