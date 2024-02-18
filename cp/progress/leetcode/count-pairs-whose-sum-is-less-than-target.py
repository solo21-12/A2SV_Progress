class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0

        for l in range(len(nums)):
            r = l + 1

            while r < len(nums) and nums[r] + nums[l] < target:
                r += 1
                count += 1

        return count
