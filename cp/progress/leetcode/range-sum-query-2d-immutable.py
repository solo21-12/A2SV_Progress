class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col = len(matrix),len(matrix[0])
        self.sumMtrix = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(row):
            prefixSum = 0
            for j in range(col):
                prefixSum += matrix[i][j]
                above = self.sumMtrix[i][j+1]
                self.sumMtrix[i+1][j+1] = prefixSum + above

        print(self.sumMtrix)

        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2 = row1+1,col1+1,row2+1,col2+1

        bottomRight = self.sumMtrix[r2][c2]
        above = self.sumMtrix[r1-1][c2]
        left = self.sumMtrix[r2][c1-1]
        topLeft = self.sumMtrix[r1-1][c1-1]

        return bottomRight +  topLeft - above - left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)