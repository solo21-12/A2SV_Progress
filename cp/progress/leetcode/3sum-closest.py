class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = float('inf')
        ans = 0

        for i, num in enumerate(nums):

            l, r = i + 1, len(nums) - 1


            while l < r:
                curSum = nums[l] + nums[r]
                if abs(target - (num + curSum)) <= close:
                    close = abs(target - (num + curSum))
                    ans = num + curSum

                if curSum + num > target:
                    r -= 1
                elif curSum + num < target:
                    l += 1
                else:
                    r -= 1
                    l += 1

        return ans

        