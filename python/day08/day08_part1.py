codes = open("day08_input.txt").read().splitlines()

num_characters = 0
memory_usage = 0

for code in codes:
    num_characters += len(code)

    i = 1
    while i < len(code) - 1:
        if code[i] != "\\":
            i += 1
            memory_usage += 1
            continue

        match code[i+1]:
            case "\\" | '"':
                i += 2
                memory_usage += 1
            case "x":
                i += 4
                memory_usage += 1

print(num_characters - memory_usage)