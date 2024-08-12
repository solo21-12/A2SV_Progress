class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r = 0, k - 1 
        max_ave = float("-inf")
        cur_sum =  sum(nums[l:r])

        while r < len(nums):
            cur_sum += nums[r]
            cur_avr = cur_sum / k
            max_ave = max(cur_avr,max_ave)
            cur_sum -= nums[l]
            l += 1
            r += 1

        return max_ave

        