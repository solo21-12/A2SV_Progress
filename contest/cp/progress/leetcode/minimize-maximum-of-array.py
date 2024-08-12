class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        curSum = 0

        for i, num in enumerate(nums):
            curSum += num
            avg = curSum / (i +1 )
            ans = max(avg, ans)

        return ceil(ans)
        