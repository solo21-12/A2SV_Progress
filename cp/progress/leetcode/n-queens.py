from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def not_same_diagonal(coords):
            n = len(coords)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    x1, y1 = coords[i]
                    x2, y2 = coords[j]
                    if abs(x1 - x2) == abs(y1 - y2):
                        return False
            return True

        def backtrack(row, path, col):
            nonlocal ans
            if not not_same_diagonal(path):
                return

            if row == n:
                ans.append(path[:])
                return

            for c in range(n):
                if c not in col:
                    path.append((row, c))
                    col.add(c)
                    backtrack(row + 1, path, col)
                    path.pop()
                    col.remove(c)

        ans = []
        backtrack(0, [], set())

        result = []
        for num in ans:
            solution = ["." * n for _ in range(n)]
            for r, c in num:
                solution[r] = solution[r][:c] + "Q" + solution[r][c + 1:]
                
            result.append(solution)

        return result
