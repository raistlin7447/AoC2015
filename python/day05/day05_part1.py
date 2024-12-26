
def is_nice(string):
    for invalid in ["ab", "cd", "pq", "xy"]:
        if invalid in string:
            return False

    num_vowels = 0
    double_letter = False

    for i, char in enumerate(string):
        if char in "aeiou":
            num_vowels += 1
        try:
            if char == string[i+1]:
                double_letter = True
        except IndexError:
            pass

    if num_vowels >= 3 and double_letter:
        return True
    else:
        return False

total = 0
for string in open("day05_input.txt").read().splitlines():
    if is_nice(string):
        total += 1

print(total)
