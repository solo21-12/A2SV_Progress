from collections import defaultdict, deque
import heapq

adj = defaultdict(list)
indegree = defaultdict(int)


def accept_input(m):
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        indegree[b] += 1


m, n = map(int, input().split())
accept_input(m)
vis = set()
result_stack = []


def khan_algo(n, indegree):
    q = deque()
    result_stack = []
    for i in range(n):
        if i not in indegree:
            q.append(i)

    while q:
        node = q.popleft()
        result_stack.append(node)

        for neigbour in adj[node]:
            indegree[neigbour] -= 1

            if indegree[neigbour] == 0:
                q.append(neigbour)


    return result_stack

vis = set()
def dfs(current):
    vis.add(current)

    for neigbour in adj[current]:
        if neigbour not in vis:
            dfs(neigbour)

    result_stack.append(current)


for i in range(n):
    if i not in vis:
        dfs(i)


print(*result_stack[::-1])
# print(*khan_algo())