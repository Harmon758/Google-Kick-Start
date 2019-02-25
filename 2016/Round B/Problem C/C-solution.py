import collections

Endpoint = collections.namedtuple("Endpoint", ["index", "value", "start"])

T = int(input())
for t in range(1, T + 1):
    N, L1, R1, A, B, C1, C2, M = map(int, input().split())
    endpoints = [Endpoint(0, L1, True), Endpoint(0, R1 + 1, False)]
    for i in range(1, N):
        x = (A * L1 + B * R1 + C1) % M
        y = (A * R1 + B * L1 + C2) % M
        endpoints.append(Endpoint(i, min(x, y), True))
        endpoints.append(Endpoint(i, max(x, y) + 1, False))
        L1, R1 = x, y
    endpoints.sort(key = lambda endpoint: endpoint.value)
    unique_integers = {}
    current_intervals = set()
    total_integers = 0
    for endpoint in endpoints:
        if not current_intervals:
            interval_start = endpoint
        elif len(current_intervals) == 1:
            index = next(iter(current_intervals))
            unique_integers[index] = (unique_integers.get(index, 0) +
                                      endpoint.value - unique_start.value)
        if endpoint.start:
            current_intervals.add(endpoint.index)
        else:
            current_intervals.remove(endpoint.index)
        if not current_intervals:
            total_integers += endpoint.value - interval_start.value
        elif len(current_intervals) == 1:
            unique_start = endpoint
    print(f"Case #{t}: {total_integers - max(unique_integers.values())}")
