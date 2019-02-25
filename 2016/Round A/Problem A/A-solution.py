T = int(input())
for x in range(1, T + 1):
    N = int(input())
    greatest = -1
    for i in range(N):
        name = input()
        count = len(set(name.replace(" ", "")))
        if count > greatest or (count == greatest and name < y):
            greatest = count
            y = name
    print(f"Case #{x}: {y}")
