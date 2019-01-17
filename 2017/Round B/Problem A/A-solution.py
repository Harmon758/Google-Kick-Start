powers_of_2 = [1]
for i in range(1, 10000):
    powers_of_2.append(2 * powers_of_2[-1])

T = int(input())
for t in range(T):
    N = int(input())
    K = list(map(int, input().split()))
    total = 0
    for n in range(N):
        end = N - n - 1
        for i in range(end):
            total += (K[end] - K[i]) * powers_of_2[max(end - i - 1, 0)]
    print(f"Case #{t + 1}: {total % (10 ** 9 + 7)}")
