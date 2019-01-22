T = int(input())
for t in range(T):
    W = input()
    answers = 1 + int(len(W) > 1 and W[0] != W[1])
    for i in range(1, len(W)):
        answers *= len(set(W[i - 1:i + 2]))
    print(f"Case #{t + 1}: {answers % (10 ** 9 + 7)}")
