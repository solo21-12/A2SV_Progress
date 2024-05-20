class Solution:
    def prevSmaller(self,nums):
        ans = [-1] * len(nums)
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[i] < nums[stack[-1]]:
                index = stack.pop()
                ans[index] = nums[i]
            
            stack.append(i)
            
        return ans

    def nextSmaller(self,nums):
        ans = [-1] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                index = stack.pop()
                ans[index] = nums[i]
            
            stack.append(i)
        
        return ans
    
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # stack = []
        # ans = 0
        # MOD = 10**9 + 7
        
        # for i, num in enumerate(arr):

        #     while stack and num < arr[stack[-1]]:
        #         index = stack.pop()
        #         left = index - stack[-1] if stack else index + 1
        #         right = i - index
        #         ans += (arr[index] * left * right) % MOD

        #     stack.append(i)

        # for i in range(len(stack)):
        #     index = stack[i]
        #     left = index - stack[i - 1] if i > 0 else index + 1
        #     right = len(arr) - index

        #     ans += (arr[index] * left * right) % MOD

        # return ans
        ans = 0
        MOD = 10**9 + 7
        leftSmaller = self.prevSmaller(arr)
        rightSmaller = self.nextSmaller(arr)

        for i in range(len(arr)):
            left = leftSmaller[i] - i if leftSmaller[i] > -1 else  i + 1
            right = rightSmaller[i] - i
            ans += (arr[i] * left * right) % MOD

        return ans

        
