T = int(input())
for x in range(1, T + 1):
    N, P = map(int, input().split())
    forbidden = []
    for p in range(P):
        forbidden.append(input())
    forbidden.sort(key = len, reverse = True)
    forbidden_copy = forbidden.copy()
    for n, f in enumerate(forbidden_copy):
        for i in range(n):
            if forbidden_copy[i].startswith(f):
                if forbidden_copy[i] in forbidden:
                    forbidden.remove(forbidden_copy[i])
    y = 2 ** N
    for f in forbidden:
        y -= 2 ** (N - len(f))
    print(f"Case #{x}: {y}")
