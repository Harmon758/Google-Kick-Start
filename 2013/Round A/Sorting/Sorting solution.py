T = int(input())
for X in range(1, T + 1):
    N = int(input())
    s = list(map(int, input().split()))
    even = []
    odd = []
    for s_i in s:
        if s_i % 2:
            odd.append(s_i)
        else:
            even.append(s_i)
    even.sort()
    odd.sort(reverse=True)
    t = []
    for s_i in s:
        if s_i % 2:
            t.append(odd.pop())
        else:
            t.append(even.pop())
    print(f"Case #{X}: {' '.join(map(str, t))}", flush=True)
