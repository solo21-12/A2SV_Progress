class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        count = 0
        hashx = set()
        
        while l <= r and r < len(s):
            if s[r] not in hashx:
                hashx.add(s[r])
                count = max(r-l+1,count)
                r += 1
            else:
                hashx.remove(s[l])
                l += 1

        return count
        