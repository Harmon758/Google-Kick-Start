T = int(input())

for x in range(1, T + 1):

    I = input()
    P = input()

    index = 0
    for character in I:
        index = P.find(character, index) + 1
        if not index:
            y = "IMPOSSIBLE"
            break
    else:
        y = len(P) - len(I)

    print(f"Case #{x}: {y}", flush = True)
