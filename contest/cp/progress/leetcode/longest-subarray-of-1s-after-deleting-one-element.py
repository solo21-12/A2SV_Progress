class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window = defaultdict(int)
        l,r=0,0
        ans = 0

        while r < len(nums):
            window[nums[r]] += 1

            while window[0] > 1:
                window[nums[l]] -= 1
                l += 1

            ans = max(r-l,ans)

            r += 1

        return ans
        