class Solution:
    def totalNQueens(self, n: int) -> int:
        
        
        def backtrack(row, path, colSet, negDeg, posDeg):
            nonlocal count

            if len(path) == n:
                count += 1
                return

            for col in range(n):
                if col not in colSet and (col + row) not in posDeg and (row - col) not in negDeg:
                    path.append((row, col))
                    colSet.add(col)
                    negDeg.add(row - col)
                    posDeg.add(row + col)
                    backtrack(row + 1 , path, colSet, negDeg, posDeg)
                    path.pop()
                    colSet.remove(col)
                    posDeg.remove(row + col)
                    negDeg.remove(row - col)



        count = 0
        backtrack(0, [], set(), set(), set())

        return count