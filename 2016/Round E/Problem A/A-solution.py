T = int(input())
for x in range(1, T + 1):
    S = input()
    I, J = map(int, input().split())
    y = (J - I) // len(S) * S.count('B')
    initial_index = (I - 1) % len(S)
    final_index = (J - 1) % len(S)
    if final_index >= initial_index:
        y += S[initial_index:final_index + 1].count('B')
    else:
        y += S[:final_index + 1].count('B') + S[initial_index:].count('B')
    print(f"Case #{x}: {y}")
