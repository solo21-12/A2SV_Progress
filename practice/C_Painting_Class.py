from collections import defaultdict, deque


n = int(input())
edges = list(map(int, input().split()))
colors = list(map(int, input().split()))


adj = defaultdict(list)

for i, num in enumerate(edges):
    adj[num].append(i + 2)
    
q = deque([(1,  colors[0])])
vis = set()
nums = deque()
ans = 1
while q:

    node, color = q.popleft()

    if colors[node - 1] != color:
        ans += 1

    for nbr in adj[node]:
        if nbr not in vis:

            q.append((nbr, colors[node - 1]))
            vis.add(nbr)

print(ans)
