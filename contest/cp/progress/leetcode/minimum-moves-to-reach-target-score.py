class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0

        while maxDoubles and target > 1:
            if target % 2:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1

            res += 1


        res += target - 1

        return res
        