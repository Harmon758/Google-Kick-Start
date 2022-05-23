T = int(input())

for x in range(1, T + 1):

    N, X, Y = map(int, input().split())

    total_sum = N * (N + 1) / 2
    alan_sum = total_sum * X / (X + Y)

    if alan_sum.is_integer():
        y = "POSSIBLE"
        print(f"Case #{x}: {y}", flush = True)
        alan_sum = int(alan_sum)
    else:
        y = "IMPOSSIBLE"
        print(f"Case #{x}: {y}", flush = True)
        continue

    alan_subset = []
    partial_sum = 0
    largest_integer = N
    while partial_sum != alan_sum and alan_sum - partial_sum > largest_integer:
        partial_sum += largest_integer
        alan_subset.append(str(largest_integer))
        largest_integer -= 1
    if partial_sum != alan_sum:
        alan_subset.append(str(alan_sum - partial_sum))

    print(len(alan_subset), flush = True)
    print(' '.join(alan_subset), flush  = True)
