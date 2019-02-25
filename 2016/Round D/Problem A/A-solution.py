T = int(input())
for x in range(1, T + 1):
    N, M = map(int, input().split())
    # Bertrand's ballot theorem
    print(f"Case #{x}: {(N - M) / (N + M)}")
