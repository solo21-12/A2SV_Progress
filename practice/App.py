from collections import defaultdict, deque
import sys
n, e = map(int, sys.stdin.readline().split())
adj = defaultdict(list)
start = n
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
    start = min(a, b, start)


def detect_bfs(n, start):
    q = deque()
    vis = [False] * (n + 1)

    q.append((start, -1))
    vis[start] = True

    while q:
        idx, parent = q.popleft()

        for num in adj[idx]:
            if not vis[num]:
                vis[num] = True
                q.append((num, idx))
            elif num != parent:
                return True
            else:
                continue

    return False


def detect_DFS(start):
    stack = [(start, -1)]
    vis = set([start])
    while stack:
        idx, parent = stack.pop()

        for neigbour in adj[idx]:
            if neigbour not in vis:
                vis.add(neigbour)
                stack.append(((neigbour, idx)))
            elif neigbour != parent:
                return True
            else:
                continue

    return False


def solve():
    for i in range(n+1):
        if detect_DFS(i):
            return True

    return False


print(solve())
