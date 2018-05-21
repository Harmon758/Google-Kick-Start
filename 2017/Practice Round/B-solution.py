
# Problem B. Vote
# https://code.google.com/codejam/contest/6304486/dashboard#s=p1

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    # Bertrand's ballot theorem
    print(f"Case #{t + 1}: {(N - M) / (N + M)}")
