class Solution:
    UNOCCUPIED = 0
    GUARD = "G"
    WALL = "W"
    PROTECTED = "X"

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        cells = [[self.UNOCCUPIED for _ in range(n)] for _ in range(m)]

        for row, col in guards:
            cells[row][col] = self.GUARD

        for row, col in walls:
            cells[row][col] = self.WALL

        for row, col in guards:
            self.updateDirection(cells, row, col + 1, m, n, 0, 1)
            self.updateDirection(cells, row, col - 1, m, n, 0, -1)
            self.updateDirection(cells, row + 1, col, m, n, 1, 0)
            self.updateDirection(cells, row - 1, col, m, n, -1, 0)

        count = sum(row.count(self.UNOCCUPIED) for row in cells)
        return count

    def updateDirection(self, cells, row, col, m, n, row_dir, col_dir):

        while 0 <= row < m and 0 <= col < n and cells[row][col] != self.WALL and cells[row][col] != self.GUARD:
            cells[row][col] = self.PROTECTED

            row += row_dir
            col += col_dir
