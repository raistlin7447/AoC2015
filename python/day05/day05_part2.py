from itertools import pairwise


def is_nice(string):
    return has_pair_of_two_letters(string) and has_split_repeat(string)

def has_pair_of_two_letters(string):
    for i, pair in enumerate(pairwise(string)):
        if pair[0]+pair[1] in string[i+2:]:
            return True
    return False

def has_split_repeat(string):
    for i, char in enumerate(string):
        try:
            if char == string[i+2]:
                return True
        except IndexError:
            break
    return False

total = 0
for string in open("day05_input.txt").read().splitlines():
    if is_nice(string):
        total += 1

print(total)
