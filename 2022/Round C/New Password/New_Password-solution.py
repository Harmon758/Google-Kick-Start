T = int(input())

for x in range(1, T + 1):

    N = int(input())
    y = input()

    uppercase_letter = False
    lowercase_letter = False
    digit = False
    special_character = False

    for character in y:
        if character.isupper():
            uppercase_letter = True
        elif character.islower():
            lowercase_letter = True
        elif character.isdigit():
            digit = True
        elif character in "#@*&":
            special_character = True

    if not uppercase_letter:
        y += 'A'
    if not lowercase_letter:
        y += 'a'
    if not digit:
        y += '0'
    if not special_character:
        y += '#'

    y = y.ljust(7, '#')

    print(f"Case #{x}: {y}", flush = True)
