class Solution:
    def isValid(self, window, t):
        for key in t.keys():
            if window[key] < t[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)

        t = Counter(t)
        l = 0
        res = (inf, "")

        for r in range(len(s)):
            count[s[r]] += 1

            while self.isValid(count, t):
                if r - l + 1 < res[0]:
                    res = (r - l + 1, s[l : r + 1])

                if s[l] in count:
                    count[s[l]] -= 1

                if not count[s[l]]:
                    count.pop(s[l])

                l += 1

        return res[1]
