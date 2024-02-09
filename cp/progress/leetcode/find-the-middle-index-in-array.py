class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1,n):
            nums[i] += nums[i - 1]

        for i in range(n):
            leftSum,rightSum =0,0

            if i > 0:
                leftSum = nums[i-1]
            if i < n-1:
                rightSum = nums[-1] - nums[i]

            if leftSum == rightSum:
                return i

        return -1
        
        