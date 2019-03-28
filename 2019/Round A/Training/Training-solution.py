T = int(input())
for x in range(1, T + 1):
    N, P = map(int, input().split())
    S = map(int, input().split())
    S = sorted(S, reverse = True)
    y = hours = sum(S[0] - s for s in S[:P])
    for i in range(1, N - P + 1):
        hours -= (S[i - 1] - S[i]) * (P - 1)
        hours += S[i] - S[P + i - 1]
        if hours < y:
            y = hours
    print("Case #{}: {}".format(x, y), flush = True)
