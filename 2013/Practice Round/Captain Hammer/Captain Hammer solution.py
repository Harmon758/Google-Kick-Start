from decimal import Decimal
from math import asin, pi

T = int(input())
for x in range(1, T + 1):
    V, D = map(Decimal, input().split())
    θ = 90 * asin(Decimal(9.8) * D / (V ** 2)) / pi
    print(f"Case #{x}: {θ:.7f}", flush=True)
