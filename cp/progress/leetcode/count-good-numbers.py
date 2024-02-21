class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        evens = pow(5,math.ceil(n / 2),MOD)
        odds = pow(4, n // 2, MOD)

        return (evens * odds) % MOD
        