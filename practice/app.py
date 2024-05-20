
from collections import deque
from typing import List


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        vis = [False] * (V + 1)
        bfs = []
        q = deque()
        q.append(0)
        vis[0] = True

        while q:
            top = q.popleft()
            bfs.append(top)

            for i in adj[top]:
                if not vis[i]:
                    q.append(i)
                    vis[i] = True

        return bfs

