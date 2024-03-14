class Solution:
    def findSum(self, nums, divisor):
        res = 0
        for num in nums:
            res += (ceil(num / divisor))

        return res

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        low = 1
        high = max(nums)

        while low <= high:
            mid = low + ( high - low) // 2

            curSum = self.findSum(nums, mid)

            if curSum > threshold:
                low = mid + 1
            else:
                high = mid - 1

        return low


