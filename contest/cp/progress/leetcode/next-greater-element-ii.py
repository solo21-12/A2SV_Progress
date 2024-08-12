class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []
        ans = [-1] * N

        for i in range(2*N - 1,-1, -1):
            curr = nums[i % N]

            while stack and curr >= nums[stack[-1]]:
                stack.pop()

            if stack:
                ans[i % N] = nums[stack[-1]]

            stack.append(i % N)

        return ans
        