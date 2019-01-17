
# Problem A. Diwali lightings
# https://code.google.com/codejam/contest/12254486/dashboard#s=p0

T = int(input())
for t in range(T):
    S = input()
    I, J = map(int, input().split())
    count = (J - I) // len(S) * S.count('B')
    initial_index = (I - 1) % len(S)
    final_index = (J - 1) % len(S)
    if final_index >= initial_index:
        count += S[initial_index:final_index + 1].count('B')
    else:
        count += S[:final_index + 1].count('B') + S[initial_index:].count('B')
    print(f"Case #{t + 1}: {count}")
