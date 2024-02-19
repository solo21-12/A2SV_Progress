class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = "0"
        for i, ch in enumerate(number):
            if ch == digit:
                cur = number[:i] + number[i + 1 :]
                ans = max(cur, ans)

        return ans
