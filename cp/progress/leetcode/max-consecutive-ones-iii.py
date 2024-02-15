class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        l,r=0,0
        ans = 0
        while r < len(nums):
            window[nums[r]] += 1

            while (r-l+1) - window[1] > k:
                window[nums[l]] -= 1
                l += 1

            ans = max(r-l+1,ans)
            r += 1
        return ans