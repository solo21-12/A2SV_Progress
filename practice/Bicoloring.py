from collections import defaultdict


class Solution:
    def solution(self, graph, n):

        colores = [0] * (n + 1)

        def dfs(current, color):
            colores[current] = color

            for node in graph[current]:
                if not colores[node]:
                    if not dfs(node, color * -1):
                        return False
                elif colores[node] == color:
                    return False

            return True

        def solve():
            for i in range(n + 1):
                if not colores[i]:
                    if not dfs(i, 1):
                        return False

            return True

        if solve():
            print("BICOLOURABLE.")
        else:
            print('NOT BICOLOURABLE.')


n = int(input())
while n > 0:
    edges = int(input())
    graph = defaultdict(list)

    for _ in range(edges):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    solution = Solution()
    solution.solution(graph, n)

    n = int(input())
