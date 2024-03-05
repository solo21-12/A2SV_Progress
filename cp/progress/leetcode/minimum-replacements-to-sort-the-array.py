class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        mx = nums[-1]

        for i in range(len(nums) - 2, -1,-1):
            d = ceil(nums[i] / mx)
            res += d - 1
            mx = nums[i] // d
        
        return res