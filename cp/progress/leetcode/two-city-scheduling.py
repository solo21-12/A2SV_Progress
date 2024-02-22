class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:(x[0] - x[1]))
        N = len(costs)

        first = sum(cost[0] for cost in costs[:N//2])
        second = sum(cost[1] for cost in costs[N//2:])

        return first + second

        