class Solution:
    def minimumSteps(self, s: str) -> int:
        s = [ch for ch in s]
        left,right = 0,len(s) - 1
        count  = 0

        while left < right:

            if s[left] == "1":
                while right > left and s[right] == "1":
                    right -= 1
                
                s[left],s[right] = s[right],s[left]
                count += right - left
            else:
                left += 1

        return count


