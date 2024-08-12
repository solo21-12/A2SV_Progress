class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left,right = [0]*len(nums), [0]*len(nums)
        ls,rs = 1,1

        for i in range(len(nums)):
            ls *= nums[i]
            left[i] = ls

        for i in range(len(nums)-1,-1,-1):
            rs *= nums[i]
            right[i] = rs

        nums[0] = right[1]
        nums[-1] = left[-2]

        for i in range(1,len(nums)-1):
            nums[i] = (right[i+1] * left[i-1])
           

        return nums

        
        