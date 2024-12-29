import json

json_input = json.loads(open("day12_input.txt").read())

def item_generator(json_input):
    match json_input:
        case int():
            yield json_input
        case dict():
            for v in json_input.values():
                yield from item_generator(v)
        case list():
            for item in json_input:
                yield from item_generator(item)

print(sum(item_generator(json_input)))