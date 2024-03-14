class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = -inf

        def findHeater(house):
            low, high = 0, len(heaters) - 1
            radius = inf

            while low <= high:
                mid = (low + high) // 2
                radius = min(abs(heaters[mid] - house), radius)

                if heaters[mid] == house:
                    return 0
                elif  heaters[mid] < house:
                    low = mid + 1
                else:
                    high = mid - 1

            return radius


        for house in houses:
            r = findHeater(house)
            res = max(r, res)

        return res



        