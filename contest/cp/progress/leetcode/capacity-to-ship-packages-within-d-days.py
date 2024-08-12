class Solution:
    def possible(self, weights, curWeight):
        count = 1
        temp = 0

        for weight in weights:
            if temp + weight <= curWeight:
                temp += weight
            else:
                count += 1
                temp = weight

        return count

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = low + (high - low) // 2

            curDays = self.possible(weights, mid)

            if curDays <= days:
                high = mid
            else:
                low = mid + 1

        return low
