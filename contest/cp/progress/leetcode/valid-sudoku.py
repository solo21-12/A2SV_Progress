class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        matrixSet = defaultdict(set)

        row = len(board)
        col = len(board[0])

        for r in range(row):
            for c in range(col):
                mr = r // 3
                mc = c // 3
                
                if board[r][c] in colSet[c] or board[r][c] in rowSet[r] or board[r][c] in matrixSet[(mr, mc)]:
                    return False
                
                if board[r][c].isdigit():
                    rowSet[r].add(board[r][c])
                    colSet[c].add(board[r][c])
                    matrixSet[(mr, mc)].add(board[r][c])


        return True

        