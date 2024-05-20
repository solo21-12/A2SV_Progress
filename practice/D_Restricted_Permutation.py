

from collections import defaultdict
from heapq import heappush, heappop

n, m = map(int, input().split())
graph = defaultdict(list)
inorder = defaultdict(int)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    inorder[v] += 1


def toplogical_sort():
    q = []
    for i in range(1, n + 1):
        if inorder[i] == 0:
            heappush(q, i)
    ans = []
    while q:
        u = heappop(q)
        ans.append(u)

        for v in graph[u]:
            inorder[v] -= 1
            if inorder[v] == 0:
                heappush(q, v)

    return ans


ans = toplogical_sort()

if len(ans) == n:
    print(*ans)
else:
    print(-1)
