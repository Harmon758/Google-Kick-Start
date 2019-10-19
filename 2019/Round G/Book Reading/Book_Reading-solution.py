T = int(input())
for x in range(1, T + 1):
    N, M, Q = map(int, input().split())
    P = map(int, input().split())
    R = map(int, input().split())
    pages = [True] * (N + 1)
    for P_i in P:
        pages[P_i] = False
    readers = {}
    y = 0
    for R_i in R:
        try:
            y += readers[R_i]
        except KeyError:
            read = sum(pages[page] for page in range(R_i, N + 1, R_i))
            readers[R_i] = read
            y += read
    print("Case #{}: {}".format(x, y), flush = True)
