class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        low, high = 0, len(nums) - 1
        # find the first occurenec

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                res[0] = mid
                high = mid - 1

        low, high = 0, len(nums) - 1
        # Find the last occurence
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                res[1] = mid
                low = mid + 1

        return res
