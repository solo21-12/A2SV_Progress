class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        
        def backtrack(row, path, col, posDeg, negDeg):
            nonlocal ans

            if len(path) == n:
                ans.append(path[:])
                return

            for c in range(n):
                if c not in col and (row + c) not in posDeg and (row - c) not in negDeg :
                    path.append((row, c))
                    col.add(c)
                    posDeg.add(row + c)
                    negDeg.add(row - c)
                    backtrack(row + 1, path, col, posDeg, negDeg)
                    path.pop()
                    col.remove(c)
                    posDeg.remove(row + c)
                    negDeg.remove(row - c)

        ans = []
        backtrack(0, [], set(), set(), set())
        print(ans)

        result = []
        for num in ans:
            solution = ["." * n for _ in range(n)]
            for r, c in num:
                solution[r] = solution[r][:c] + "Q" + solution[r][c + 1:]
            result.append(solution)

        return result
