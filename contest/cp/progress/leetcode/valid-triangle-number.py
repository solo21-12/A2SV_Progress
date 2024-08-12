class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        ans = 0
        for i in range(len(nums) - 2):
            left = i + 1

            right = i + 2
            while left < len(nums) - 1:


                while right < len(nums) and nums[i] + nums[left] > nums[right]:
                    right += 1

                ans += right - left - 1 

                left += 1
                if left == right:
                    right += 1

        return ans
