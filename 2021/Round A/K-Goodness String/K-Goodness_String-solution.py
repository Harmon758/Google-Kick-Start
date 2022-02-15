T = int(input())
for x in range(1, T + 1):
    N, K = map(int, input().split())
    S = input()
    goodness_score = 0
    for i in range(N // 2):
        goodness_score += S[i] != S[N - i - 1]
    y = abs(K - goodness_score)
    print(f"Case #{x}: {y}", flush = True)
