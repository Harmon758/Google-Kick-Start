T = int(input())
for t in range(T):
    N = int(input())
    leader = input()
    greatest = len(set(leader.replace(" ", "")))
    for i in range(N - 1):
        name = input()
        count = len(set(name.replace(" ", "")))
        if count > greatest or (count == greatest and name < leader):
            greatest = count
            leader = name
    print(f"Case #{t + 1}: {leader}")
