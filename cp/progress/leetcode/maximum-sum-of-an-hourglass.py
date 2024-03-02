class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row - 2):
            for j in range(col - 2):
                firstRow = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                thirdRow = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                secondRow = grid[i+1][j+1]

                ans = max(ans, firstRow + secondRow +thirdRow)

        return ans


        