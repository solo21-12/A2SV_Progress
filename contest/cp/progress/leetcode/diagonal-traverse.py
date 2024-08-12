class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        ans = []
        row = len(mat)
        col = len(mat[0])

        r,c = 0, 0
        up = True

        while r < row and c < col:
            if up:
                while r > 0 and c < col - 1:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
                
                ans.append(mat[r][c])

                if c == col - 1:
                    r += 1
                else:
                    c += 1

            else:
                while r < row - 1 and c > 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1

                ans.append(mat[r][c])
                if r == row - 1:
                    c += 1
                else:
                    r += 1

            up = not up

        return ans
                


        