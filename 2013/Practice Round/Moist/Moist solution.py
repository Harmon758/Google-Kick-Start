T = int(input())
for x in range(1, T + 1):
    N = int(input())
    names = [input() for index in range(N)]
    y = 0
    previous = names[0]
    for name in names[1:]:
        if name < previous:
            y += 1
        else:
            previous = name
    print(f"Case #{x}: {y}", flush = True)
