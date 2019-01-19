T = int(input())
for t in range(T):
    L, R = map(int, input().split())
    pairs = min(L, R)
    print(f"Case #{t + 1}: {pairs * (pairs + 1) // 2}")
