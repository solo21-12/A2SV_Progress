class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        longestPalindrome = 0
        odds = 0

        for ch, count in letters.items():
            if count % 2:
                if odds:
                    longestPalindrome += count - 1
                else:
                    longestPalindrome += count
                    odds += 1
            else:
                longestPalindrome += count

        return longestPalindrome
