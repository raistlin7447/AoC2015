from functools import cache

registers = dict()

operations = open("day07_input.txt").read().splitlines()

for operation in operations:
    expression, result_register = operation.split(" -> ")
    expression = expression.split()

    match len(expression):
        case 1: # literal value
            if expression[0].isdigit():
                value = int(expression[0])
                registers[result_register] = ("VAL", value, "_")
            else:
                reference = expression[0]
                registers[result_register] = ("REF", reference, "_")
        case 2: # NOT
            opr, o1 = expression
            registers[result_register] = (opr, o1, "_")
        case 3: # AND, OR, LSHIFT, RSHIFT
            o1, opr, o2 = expression
            registers[result_register] = (opr, o1, o2)

@cache
def get_register(register_name):
    if register_name.isdigit():
        return int(register_name)

    operation, operand1, operand2 = registers[register_name]
    match operation:
        case "VAL":
            return operand1
        case "REF":
            return get_register(operand1)
        case "NOT":
            return ~get_register(operand1) & 0xffff
        case "AND":
            return get_register(operand1) & get_register(operand2)
        case "OR":
            return get_register(operand1) | get_register(operand2)
        case "LSHIFT":
            return get_register(operand1) << int(operand2)
        case "RSHIFT":
            return get_register(operand1) >> int(operand2)

print(get_register("a"))
