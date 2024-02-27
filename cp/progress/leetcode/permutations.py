class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(selected, path):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if selected[i] == 0:
                    path.append(nums[i])
                    selected[i] = 1
                    backtrack(selected, path)
                    selected[i] = 0
                    path.pop()

        ans = []
        backtrack([0] * len(nums), [])

        return ans
