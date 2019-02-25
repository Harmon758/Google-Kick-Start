T = int(input())
for x in range(1, T + 1):
    W = input()
    answers = 1 + int(len(W) > 1 and W[0] != W[1])
    for i in range(1, len(W)):
        answers *= len(set(W[i - 1:i + 2]))
    print(f"Case #{x}: {answers % (10 ** 9 + 7)}")
