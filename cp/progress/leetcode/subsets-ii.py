class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def findSubSet(index, curr):
            N = len(nums)

            if index >= N:
                ans.append(curr[::])
                return

            curr.append(nums[index])
            findSubSet(index  + 1, curr)
            curr.pop()

            while index  + 1 < N and nums[index] == nums[index+1]:
                index += 1

            findSubSet(index  + 1, curr)

        findSubSet(0,[])

        return ans
        