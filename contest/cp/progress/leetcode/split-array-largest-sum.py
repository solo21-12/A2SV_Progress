class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def possible(summ):
            cnt = 1
            curSum = 0

            for num in nums:
                if num + curSum <= summ:
                    curSum += num
                else:
                    curSum = num
                    cnt += 1
            
            return cnt


        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2

            c = possible(mid)
            if c <= k:
                high = mid - 1
            else:
                low = mid + 1

        return low
        