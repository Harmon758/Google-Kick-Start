from math import factorial

T = int(input())
for x in range(1, T + 1):
    M, N = map(int, input().split())
    y = sum(
        (-1) ** m * (M - m) ** N * factorial(M) //
        (factorial(m) * factorial(M - m))
        for m in range(M + 1)
    ) % (10 ** 9 + 7)
    print(f"Case #{x}: {y}")
