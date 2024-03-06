class Solution:
    def totalNQueens(self, n: int) -> int:
        def not_same_diagonal(coords):
            n = len(coords)

            for i in range(n - 1):
                for j in range(i + 1, n):
                    x1, y1 = coords[i]
                    x2, y2 = coords[j]

                    if abs(x1 - x2) == abs(y1 - y2):
                        return False

            return True 
        
        def backtrack(i, j, path, col):
            nonlocal count
            if not not_same_diagonal(path):
                return

            if len(path) == n:
                count += 1
                return

            for k in range(n):
                if k not in col:
                    path.append((i, k))
                    col.add(k)
                    backtrack(i + 1, k , path, col)
                    path.pop()
                    col.remove(k)

        count = 0
        backtrack(0, 0, [], set())

        return count