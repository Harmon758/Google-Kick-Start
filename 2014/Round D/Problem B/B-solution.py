import collections

Endpoint = collections.namedtuple("Endpoint", ["value", "start"])

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    endpoints = [Endpoint(endpoint + index % 2, not index % 2)
                 for index, endpoint in enumerate(map(int, input().split()))]
    endpoints.sort(key = lambda endpoint: endpoint.value)
    bus_counts = []
    bus_count = 0
    last_endpoint = 0
    for endpoint in endpoints:
        bus_counts.extend([bus_count] * (endpoint.value - last_endpoint))
        if endpoint.start:
            bus_count += 1
        else:
            bus_count -= 1
        last_endpoint = endpoint.value
    print(f"Case #{x}:", end = "")
    P = int(input())
    for p in range(P):
        C = int(input())
        if C >= endpoints[-1].value:
            print(" 0", end = "")
        else:
            print(f" {bus_counts[C]}", end = "")
    print(input())
