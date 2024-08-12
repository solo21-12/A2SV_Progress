class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        lp = len(piles)
        res = 0
        for i in range(1, lp - lp//3, 2):
            res += piles[i]
        return res