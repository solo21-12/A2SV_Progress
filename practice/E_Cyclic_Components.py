from collections import defaultdict
 
n, m = map(int, input().split())
adj = defaultdict(list)
 
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
 
 
vis = set()
 
 
def dfs(current):
    stack = [current]
    has_cycle = True
    while stack:
        node = stack.pop()
 
        for neigbour in adj[node]:
            if neigbour not in vis:
                stack.append(neigbour)
                vis.add(neigbour)
                
            if len(adj[neigbour]) != 2 :
                has_cycle = False
 
    return has_cycle
 
 
connected_graphs = 0
for i in adj.keys():
    if i not in vis:
        if dfs(i):
            connected_graphs += 1
 
print(connected_graphs)