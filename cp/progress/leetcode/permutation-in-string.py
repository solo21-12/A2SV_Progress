class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1x = Counter(s1)
        s2x = Counter(s2[:len(s1)])
        
        if s1x == s2x:
            return True

        for r in range(len(s1),len(s2)):
            s2x[s2[r]] = s2x.get(s2[r],0) + 1
            s2x[s2[r-len(s1)]] -= 1

            if s1x == s2x:
                return True

        
        return False

                
