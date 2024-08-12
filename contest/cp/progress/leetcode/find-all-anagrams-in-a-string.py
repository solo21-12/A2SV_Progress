class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdict = Counter(p)
        sdict = Counter([])
        l,r= 0,0
        ans = []
        
        while r < len(s):
            sdict[s[r]] = sdict.get(s[r],0) + 1

            if r - l + 1 > len(p):
                sdict[s[l]] -= 1
                l += 1

            if r - l + 1 == len(p) and sdict == pdict:
                ans.append(l)

            r += 1

        return ans

