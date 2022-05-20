T = int(input())

for x in range(1, T + 1):

    N = int(input())
    S = input()

    print(f"Case #{x}:", end = "", flush = True)

    previous_character = ""
    y = 0

    for i in range(1, N + 1):
        character = S[i - 1]

        if character > previous_character:
            y += 1
        else:
            y = 1

        print(f" {y}", end = "", flush = True)

        previous_character = character

    print(flush = True)
