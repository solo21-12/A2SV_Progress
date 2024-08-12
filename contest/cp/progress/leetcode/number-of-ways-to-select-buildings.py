class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        oneZero, zeroOne = 0, 0
        ones, zeros = 0, 0

        for ch in s:
            if ch == '1':
                ones += 1
                zeroOne += zeros
                ways += oneZero
            else:
                zeros += 1
                oneZero += ones
                ways += zeroOne

        return ways

        