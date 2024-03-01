class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        count = 0
        l = 0
        while l < len(costs) and coins > 0 and coins >= costs[l]:
            coins -= costs[l]
            count += 1
            l += 1

        return count