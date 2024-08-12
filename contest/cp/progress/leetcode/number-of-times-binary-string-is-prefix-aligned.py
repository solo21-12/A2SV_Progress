class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxx = 0
        count = 0
        
        for i, num in enumerate(flips):
            maxx = max(maxx, num)

            if maxx == i + 1:
                count += 1

        return count

        