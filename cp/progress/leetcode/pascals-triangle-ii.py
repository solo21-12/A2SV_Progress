class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascals = [[1], [1, 1]]

        for i in range(2, rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = pascals[i - 1][j - 1] + pascals[i - 1][j]

            pascals.append(row)

        return pascals[rowIndex]
