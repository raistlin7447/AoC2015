import itertools

string = open("day10_input.txt").read()
for _ in range(40):
    new_string = ""
    for group in itertools.groupby(string):
        new_string += str(len(list(group[1]))) + group[0]
    string = new_string

print(len(string))