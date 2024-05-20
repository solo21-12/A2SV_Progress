from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(idx, path):
            
            # vis.add(idx)
            if idx == N - 1:
                result.append(path[:])
                return

            for neigbours in graph[idx]:
                if neigbours not in vis:
                    path.append(neigbours)
                    dfs(neigbours, path)
                    path.pop()

        N = len(graph)
        result = []
        vis = set()
        dfs(0, [0])

        
        return result
    
solution = Solution()
print(solution.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))

        