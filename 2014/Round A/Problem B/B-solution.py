T = int(input())
for x in range(1, T + 1):
    N, DIR = input().split()
    N = int(N)
    board = []
    for row in range(N):
        board.append(list(map(int, input().split())))
    if DIR in ("up", "down"):
        board = [list(column) for column in zip(*board)]
    if DIR in ("right", "down"):
        board = [row[::-1] for row in board]
    new_board = []
    for row in board:
        new_board.append([])
        previous = -1
        for number in row:
            if not number:
                continue
            elif number == previous:
                new_board[-1].append(number * 2)
                previous = -1
            else:
                if previous != -1:
                    new_board[-1].append(previous)
                previous = number
        if previous != -1:
            new_board[-1].append(previous)
        new_board[-1].extend([0] * (N - len(new_board[-1])))
    if DIR in ("right", "down"):
        new_board = [row[::-1] for row in new_board]
    if DIR in ("up", "down"):
        new_board = [list(row) for row in zip(*new_board)]
    print(f"Case #{x}:")
    for row in new_board:
        print(' '.join(map(str, row)))
