A_LOWERCASE = ord('a')
ALPHABET_SIZE = 26


def _decompose(number):
    """Generate digits from `number` in base alphabet, least significants
    bits first.

    Since A is 1 rather than 0 in base alphabet, we are dealing with
    `number - 1` at each iteration to be able to extract the proper digits.
    """

    while number:
        number, remainder = divmod(number - 1, ALPHABET_SIZE)
        yield remainder


def base_10_to_alphabet(number):
    """Convert a decimal number to its base alphabet representation"""

    return ''.join(
            chr(A_LOWERCASE + part)
            for part in _decompose(number)
    )[::-1]


def base_alphabet_to_10(letters):
    """Convert an alphabet number to its decimal representation"""

    return sum(
        (ord(letter) - A_LOWERCASE + 1) * ALPHABET_SIZE ** i
        for i, letter in enumerate(reversed(letters.lower()))
    )

def next_password(password):
    return base_10_to_alphabet(base_alphabet_to_10(password) + 1)

def has_run_of_three(password):
    run_of_three = False

    for i, char in enumerate(password):
        try:
            next_letter = chr(ord(char) + 1)
            next_letter2 = chr(ord(next_letter) + 1)
            if next_letter == password[i+1] and next_letter2 == password[i+2]:
                run_of_three = True
        except IndexError:
            pass

    return run_of_three


def has_two_different_doubles(password):
    has_double = False
    first_double = ""
    for i, char in enumerate(password):
        try:
            if char == password[i+1]:
                if first_double and char not in first_double:
                    has_double = True
                first_double = char
        except IndexError:
            pass

    return has_double

def valid_password(password):
    for invalid in "iol":
        if invalid in password:
            return False

    if not(has_two_different_doubles(password)):
        return False

    if not(has_run_of_three(password)):
        return False

    return True

password = open("day11_input.txt").read()
while True:
    password = next_password(password)

    if valid_password(password):
        break

while True:
    password = next_password(password)

    if valid_password(password):
        break

print(password)