from collections import defaultdict, deque
import re


n, m = map(int, input().split())
start, end = map(int, input().split())

adj = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())

    adj[a].append(b)
    adj[b].append(a)


def bfs(root):
    q = deque([root])
    vis = set([root])

    parents = defaultdict(int)
    parents[root] = -1
    found = False
    res = deque()
    while q:

        top = q.popleft()
        found_val = -1
        for neigburs in adj[top]:
            if neigburs not in vis:
                parents[neigburs] = top

                if neigburs == end:
                    found_val = neigburs
                    found = True
                    break

                if not found:
                    vis.add(neigburs)
                    q.append(neigburs)

        if found:
            while found_val != -1:
                res.appendleft(found_val)
                found_val = parents[found_val]

            return list(res)
    return []


ans = bfs(start)
print(len(ans) - 1)
print(*ans)




