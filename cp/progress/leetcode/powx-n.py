class Solution:
    def myPow(self, x: float, n: int) -> float:

        def findPow(x, n):
            if n == 0:
                return 1

            result = findPow(x * x, n // 2)

            if n % 2:
                return result * x

            return result

        return findPow(x, n) if n > 0 else 1 / findPow(x, -n)
