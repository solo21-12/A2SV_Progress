class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = float('inf')
        sum_count = 0
        left,right=0,0
        
        while right < len(nums):
            sum_count += nums[right]

            while sum_count >= target and left <=right:
                count = min(count,(right - left + 1))
                sum_count -= nums[left]
                left+=1

            right += 1


        return count if count != float("inf") else 0

        