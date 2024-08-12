class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l,r=0,0
        ans = 0

        while r < len(s):
            window[s[r]] += 1

            while (r-l+1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1

            ans = max(ans,r-l+1)
            r += 1

        return ans

        