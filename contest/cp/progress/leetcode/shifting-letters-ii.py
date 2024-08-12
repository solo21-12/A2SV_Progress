class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        modification = [0] * (len(s) + 1)

        for left,right,dirx in shifts:
            if dirx:
                modification[left] += 1
                modification[right + 1] -= 1
            else:
                modification[left] -= 1
                modification[right + 1] += 1

        for i in range(1,len(modification)):
           modification[i] += modification[i-1]
           
        
        for i in range(len(s)):
            order = ord(s[i])  - ord('a')
            modification[i] = chr(((order + modification[i])  % 26) + ord('a'))

        modification.pop()
            


        return "".join(modification)