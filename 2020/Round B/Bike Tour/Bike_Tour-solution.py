from itertools import tee


T = int(input())

for x in range(1, T + 1):

    N = int(input())
    H = map(int, input().split())

    before, i, after = tee(H, 3)
    next(i, None)
    next(after, None)
    next(after, None)
    y = sum(
        H_i > H_before and H_i > H_after
        for H_before, H_i, H_after in zip(before, i, after)
    )

    print(f"Case #{x}: {y}", flush = True)
