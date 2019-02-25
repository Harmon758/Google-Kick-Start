import math

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    scores = [int(s) for s in input()]
    painted = math.ceil(N / 2)
    y = score = sum(scores[:painted])
    for i in range(N // 2):
        score += scores[i + painted] - scores[i]
        if score > y:
            y = score
    print(f"Case #{x}: {y}")
