from collections import defaultdict, deque

from cupshelpers import Printer


t = int(input())


def solve(graph, undirected, inorder, n):
    q = deque()
    for i in graph.keys():
        if i not in inorder:
            q.append(i)
            
            
    res = []
    print(q, 'queue')
    while q:
        node = q.popleft()
        res.append(node)

        for nbr in graph[node]:
            inorder[nbr] -= 1

            if inorder[nbr] == 0:
                q.append(nbr)
                
    print(res)

    # res = {num: i for i, num in enumerate(res)}
    # result = []
    
    # for a, b in undirected:
    #     if res[a] < res[b]:
    #         result.append((a, b))
    #     else:
    #         result.append((b, a))

    # for node, neigbour in graph:
    #     for n in neigbour:
    #         result.append((node, b))

    return []


for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    inorder = defaultdict(int)
    undirected = []

    for _ in range(m):
        ty, a, b = map(int, input().split())

        if ty == 1:
            graph[a].append(b)
            inorder[b] += 1
        else:
            undirected.append((a, b))
            
    # print(graph, undirected)
    result = solve(graph,undirected, inorder, n)
    # for a, b in result:
    #     print(f'{a} {b}')
