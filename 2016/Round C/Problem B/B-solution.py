import itertools

T = int(input())
for t in range(T):
    R, C, K = map(int, input().split())
    grid = [[1] * C for r in range(R)]
    for k in range(K):
        r, c = map(int, input().split())
        grid[r][c] = 0
    for r in range(1, R):
        for c in range(1, C):
            if not grid[r][c]:
                continue
            grid[r][c] = min(grid[r - 1][c], grid[r][c - 1], grid[r - 1][c - 1]) + 1
    print(f"Case #{t + 1}: {sum(itertools.chain.from_iterable(grid))}")
