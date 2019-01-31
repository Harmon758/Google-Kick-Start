from itertools import combinations_with_replacement as combinations_w_r

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    equations = {}
    original_equations = {}
    for n in range(N):
        expression, z = input().split('=')
        x, y = expression.split('+')
        if (x, y) not in equations:
            z = int(z)
            equations[(x, y)] = equations[(y, x)] = z
            original_equations[(x, y)] = z
    previous_length = -1
    while len(equations) != previous_length:
        previous_length = len(equations)
        combinations = combinations_w_r(original_equations.items(), 2)
        for ((x1, y1), z1), ((x2, y2), z2) in combinations:
            if (x1, x2) in equations and (y1, y2) not in equations:
                z = z1 + z2 - equations[(x1, x2)]
                equations[(y1, y2)] = equations[(y2, y1)] = z
            if (x1, y2) in equations and (y1, x2) not in equations:
                z = z1 + z2 - equations[(x1, y2)]
                equations[(y1, x2)] = equations[(x2, y1)] = z
            if (y1, x2) in equations and (x1, y2) not in equations:
                z = z1 + z2 - equations[(y1, x2)]
                equations[(x1, y2)] = equations[(y2, x1)] = z
            if (y1, y2) in equations and (x1, x2) not in equations:
                z = z1 + z2 - equations[(y1, y2)]
                equations[(x1, x2)] = equations[(x2, x1)] = z
    print(f"Case #{t}:")
    Q = int(input())
    for q in range(Q):
        x, y = input().split('+')
        if (x, y) in equations:
            print(f"{x}+{y}={equations[(x, y)]}")
        elif (x, x) in equations and (y, y) in equations:
            print(f"{x}+{y}={(equations[(x, x)] + equations[(y, y)]) // 2}")
