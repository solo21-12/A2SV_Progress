class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        expected.sort()
        cnt = 0

        for e, h in zip(expected, heights):
            if e != h:
                cnt += 1

        return cnt

        