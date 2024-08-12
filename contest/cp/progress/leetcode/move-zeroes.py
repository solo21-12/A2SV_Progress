class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]

            if nums[l] != 0:
                l += 1
            r += 1
        