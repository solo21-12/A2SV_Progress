class Solution:
    def numberOfWays(self, s: str) -> int:
        prefixSum = [[0] for _ in range(len(s))]
        sufixSum = [[0] for _ in range(len(s))]

        ones, zeros = 0, 0
        for i, ch in enumerate(s):
            prefixSum[i] = (zeros, ones)

            if ch == "1":
                ones += 1
            else:
                zeros += 1

        ones, zeros = 0, 0
        for i in range(len(s) - 1, -1, -1):
            sufixSum[i] = (zeros, ones)
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1

        ans = 0
        for i, ch in enumerate(s):
            z, o = prefixSum[i]
            ze, on = sufixSum[i]
            if ch == "1":
                ans += z * ze
            else:
                ans += on * o

        return ans
