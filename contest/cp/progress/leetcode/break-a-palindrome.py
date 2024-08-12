class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = []

        if len(palindrome) <= 1:
            return ""

        count = 0
        for i in range(len(palindrome)):
            ch = palindrome[i]
            
            if ord(ch) - ord('a') > 0 and count == 0 and i != len(palindrome) // 2:
                ans.append("a")
                count += 1
            else:
                ans.append(ch)

        if count == 0:
            ans[-1] = 'b'

        return "".join(ans)

            


        