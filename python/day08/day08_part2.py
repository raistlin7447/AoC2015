codes = open("day08_input.txt").read().splitlines()

num_characters = 0
encoded_usage = 0

for code in codes:
    num_characters += len(code)
    encoded_usage += 3 #starting quote
    i = 1
    while i < len(code) - 1:
        encoded_usage += 1
        if code[i] in ["\\", '"']:
            encoded_usage += 1
        i += 1
    encoded_usage += 3 #ending quote

print(encoded_usage - num_characters)