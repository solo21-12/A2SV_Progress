class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minn = [nums[0]] * len(nums)
        stack = []

        for i in range(1, len(nums)):
            minn[i] = min(minn[i-1], nums[i])

        for i in range(len(nums) -1,-1,-1):
            if minn[i] > nums[i]:
                continue
            while stack and stack[-1] <= minn[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
                
            stack.append(nums[i])

        return False


            
        