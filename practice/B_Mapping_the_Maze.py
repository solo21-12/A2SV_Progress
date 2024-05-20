from collections import defaultdict, deque

n, m = map(int, input().split())

adj = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def bus():
    one = 0
    two = 0

    for key, val in adj.items():
        if len(val) == 1:
            one += 1
        if len(val) == 2:
            two += 1

    return one + two == n


def ring():
    two = 0

    for key, val in adj.items():
        if len(val) == 2:
            two += 1

    return two == n


def star():
    one = 0
    for key, val in adj.items():
        if len(val) == 1:
            one += 1

    return one == n - 1


def solve():
    if ring():

        return "ring topology"
    if star():
        return "star topology"

    if bus():
        return "bus topology"

    return "unknown topology"


print(solve())
