class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        N = len(s)
        l = 0

        res = N
        for r in range(N):
            count[s[r]] -= 1

            while l < N and max( count["Q"],count["W"] ,count["R"],count["E"]) <= N // 4:
                res = min(res, r - l + 1)
                count[s[l]] += 1
                l += 1

        return res
