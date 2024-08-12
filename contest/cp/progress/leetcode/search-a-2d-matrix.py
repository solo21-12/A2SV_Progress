class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)

        while low < high:
            mid = low + (high - low)//2

            if matrix[mid][0] <= target:
                i = bisect.bisect_left(matrix[mid] , target)
                

                if 0 <= i < len(matrix[0]) and matrix[mid][i] == target:
                    return True

                low = mid + 1
            else:
                high = mid

        return False
        