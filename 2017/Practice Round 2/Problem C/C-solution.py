import math

T = int(input())
for t in range(T):
    N = int(input())
    B = 0
    for n in range(int(math.log(N, 2)), 1, -1):
        b = int(N ** (1 / n))
        if (b ** (n + 1) - 1) // (b - 1) == N:
            B = b
            break
    if not B:
        B = N - 1
    print(f"Case #{t + 1}: {B}")
