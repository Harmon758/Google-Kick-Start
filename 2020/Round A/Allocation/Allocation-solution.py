T = int(input())
for x in range(1, T + 1):
    N, B = map(int, input().split())
    A = map(int, input().split())
    y = 0
    total = 0
    for A_i in sorted(A):
        total += A_i
        if total > B:
            break
        else:
            y += 1
    print("Case #{}: {}". format(x, y), flush = True)
