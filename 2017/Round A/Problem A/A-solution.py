T = int(input())
for x in range(1, T + 1):
    R, C = map(int, input().split())
    S1, S2 = min(R, C), max(R, C)
    y = (S1 * (S1 - 1) * (S1 + 1) * (2 * S2 - S1) // 12) % (10 ** 9 + 7)
    print(f"Case #{x}: {y}")
