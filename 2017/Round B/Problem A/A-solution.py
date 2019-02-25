powers_of_2 = [1]
for i in range(1, 10000):
    powers_of_2.append(2 * powers_of_2[-1])

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    K = list(map(int, input().split()))
    y = 0
    for n in range(N):
        end = N - n - 1
        for i in range(end):
            y += (K[end] - K[i]) * powers_of_2[max(end - i - 1, 0)]
    print(f"Case #{x}: {y % (10 ** 9 + 7)}")
