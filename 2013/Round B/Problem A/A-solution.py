from itertools import product

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    matrix = []
    uniques = set(range(1, N ** 2 + 1))
    valid = True
    for row_index in range(N ** 2):
        row = list(map(int, input().split()))
        matrix.append(row)
        if valid and set(row) != uniques:
            valid = False
    if valid:
        for column in zip(*matrix):
            if set(column) != uniques:
                valid = False
                break
    if valid:
        for row_index, column_index in product(range(N), range(N)):
            submatrix_numbers = set()
            for row in matrix[row_index * N:(row_index + 1) * N]:
                for number in row[column_index * N:(column_index + 1) * N]:
                    submatrix_numbers.add(number)
            if submatrix_numbers != uniques:
                valid = False
                break
    if valid:
        print(f"Case #{x}: Yes")
    else:
        print(f"Case #{x}: No")
