from bisect import bisect
from math import inf, log

def fill_tile(side1, side2, sides, hi = inf):
    if not side1 or not side2 or not sides:
        return
    smaller_side = min(side1, side2)
    index = bisect(sides, log(smaller_side, 2), hi = min(hi, len(sides)))
    if not index:
        return
    size = 2 ** sides.pop(index - 1)
    fill_tile(max(side1, side2) - size, smaller_side, sides, hi = index - 1)
    fill_tile(smaller_side - size, size, sides, hi = index - 1)

T = int(input())
for x in range(1, T + 1):
    sides = list(map(int, input().split()))
    N = sides.pop(0)
    M = sides.pop(0)
    sides.sort()
    y = 0
    while sides:
        fill_tile(M, M, sides)
        y += 1
    print(f"Case #{x}: {y}")
