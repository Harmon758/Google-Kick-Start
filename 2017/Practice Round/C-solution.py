
# Problem C. Sherlock and Parentheses
# https://code.google.com/codejam/contest/6304486/dashboard#s=p2

T = int(input())
for t in range(T):
    L, R = map(int, input().split())
    pairs = min(L, R)
    print(f"Case #{t + 1}: {pairs * (pairs + 1) // 2}")
