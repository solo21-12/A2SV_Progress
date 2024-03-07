class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        matrixSet = defaultdict(set)

        row = len(board)
        col = len(board[0])

        for r in range(row):
            for c in range(col):
                if board[r][c].isdigit():
                    rowSet[r].add(board[r][c])
                    colSet[c].add(board[r][c])
                    mr = r // 3
                    mc = c // 3
                    matrixSet[(mr, mc)].add(board[r][c])


        def backtrack(r, c):
            if r == row:
                return True


            if not board[r][c].isdigit():
                mr = r // 3
                mc = c // 3
                for k in map(str, range(1, 10)):
                    if k not in matrixSet[(mr, mc)] and k not in rowSet[r] and k not in colSet[c]:
                        board[r][c] = k
                        matrixSet[(mr, mc)].add(k)
                        rowSet[r].add(k)
                        colSet[c].add(k)

                        if c < col - 1:
                            if backtrack(r, c + 1):
                                return True
                        else:
                            if backtrack(r + 1, 0):
                                return True

                        board[r][c] = ''
                        matrixSet[(mr, mc)].remove(k)
                        rowSet[r].remove(k)
                        colSet[c].remove(k)
            else:
                if c < col - 1:
                    if backtrack(r, c + 1):
                        return True
                else:
                    if backtrack(r + 1, 0):
                        return True

            return False




        backtrack(0, 0)
                
        