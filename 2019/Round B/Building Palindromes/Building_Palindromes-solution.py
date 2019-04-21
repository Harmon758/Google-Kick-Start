from collections import defaultdict

T = int(input())
for x in range(1, T + 1):
    N, Q = map(int, input().split())
    characters = input()
    counters = [defaultdict(int)]
    for character in characters:
        counter = counters[-1].copy()
        counter[character] += 1
        counters.append(counter)
    y = 0
    for i in range(Q):
        L, R = map(int, input().split())
        odd_encountered = False
        for letter, R_count in counters[R].items():
            if (R_count - counters[L - 1][letter]) % 2:
                if odd_encountered:
                    break
                odd_encountered = True
        else:
            y += 1
    print("Case #{}: {}".format(x, y), flush = True)
