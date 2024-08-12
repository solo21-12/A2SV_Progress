class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(r, c, i, path):
            if i == len(word):
                return True

            if (
                r < 0
                or c < 0
                or r >= row
                or c >= col
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False

            path.add((r, c))

            res = (
                backtrack(r + 1, c, i + 1, path)
                or backtrack(r, c + 1, i + 1, path)
                or backtrack(r - 1, c, i + 1, path)
                or backtrack(r, c - 1, i + 1, path)
            )

            path.remove((r, c))

            return res

        row, col = len(board), len(board[0])
        path = set()
        for r in range(row):
            for c in range(col):
                if backtrack(r, c, 0, path):
                    return True

        return False
