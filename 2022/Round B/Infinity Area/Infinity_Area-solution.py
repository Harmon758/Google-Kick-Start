from math import pi


T = int(input())

for x in range(1, T + 1):

    R, A, B = map(int, input().split())

    y = R * R
    radius = R
    while radius:
        radius *= A
        y += radius * radius
        radius //= B
        y += radius * radius
    y *= pi

    print(f"Case #{x}: {y}", flush = True)
