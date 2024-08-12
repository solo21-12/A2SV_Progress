class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        left,right = N - 2, N - 1

        while left >= 0:
            if nums[left] >= right - left:
                right -= 1
                left = right

            left -= 1

        return right == 0