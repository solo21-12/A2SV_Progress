class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        i,j = 0, 0
        row = len(mat) - 1
        col = len(mat[0]) - 1
        for i in range(len(mat)):
            ans += mat[i][j]
            ans += mat[i][row - i]
            i += 1
            j += 1
        
        if len(mat) % 2:
            dec = len(mat) // 2
            ans -= mat[dec][dec]


        

        return ans

        