import itertools

string = open("day10_input.txt").read()
for _ in range(50):
    string = ''.join(str(len([1 for _ in v])) + k for k, v in itertools.groupby(string))

print(len(string))