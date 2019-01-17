T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    S1, S2 = min(R, C), max(R, C)
    squares = (S1 * (S1 - 1) * (S1 + 1) * (2 * S2 - S1) // 12) % (10 ** 9 + 7)
    print(f"Case #{t + 1}: {squares}")
