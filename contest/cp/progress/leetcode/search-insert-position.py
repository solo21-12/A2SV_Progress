class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        res = N

        low, high = 0, N - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
