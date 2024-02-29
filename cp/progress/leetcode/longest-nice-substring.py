class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        s_set = set(s)

        for i, ch in enumerate(s):
            if ch.swapcase() not in s_set:
                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i+1:len(s)])

                return s1 if len(s1) >= len(s2) else s2
                

        return s