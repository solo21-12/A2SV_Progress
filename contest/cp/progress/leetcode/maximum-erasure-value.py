class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = set()

        l = 0
        N = len(nums)
        curSum = 0
        maxSum = float("-inf")
        for r in range(N):

            while l < r and nums[r] in count:
                count.remove(nums[l])
                curSum -= nums[l]
                l += 1

            count.add(nums[r])
            curSum += nums[r]
            maxSum = max(maxSum, curSum)

        return maxSum
