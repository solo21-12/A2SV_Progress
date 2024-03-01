class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e', 'i','o','u',}

        result = 0
        l = 0
        curCount = 0

        for r in range(len(s)):
            if s[r] in vowels:
                curCount += 1 
            
            if r - l  + 1 == k:
                result = max(curCount, result)

                if s[l] in vowels:
                    curCount  -= 1

                l += 1

        return result

