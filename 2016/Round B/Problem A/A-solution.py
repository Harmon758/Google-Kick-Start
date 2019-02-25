T = int(input())
for x in range(1, T + 1):
    L, R = map(int, input().split())
    pairs = min(L, R)
    print(f"Case #{x}: {pairs * (pairs + 1) // 2}")
