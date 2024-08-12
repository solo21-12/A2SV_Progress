class Solution:
    def maxScore(self, s: str) -> int:
        ones,zeros = s.count('1'),0
        ans = -1

        for i in range(len(s)-1):
            ch = s[i]
            ones -= 1 if ch == '1' else 0
            zeros += 1 if ch == '0' else 0

            currSum = ones + zeros

            ans = max(ans,currSum)

        return ans
        