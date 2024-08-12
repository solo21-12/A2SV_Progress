class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted((start, end, i) for i, (start, end) in enumerate(intervals))
        print(intervals)

        def getInterval(end):
            low, high = 0, len(intervals) - 1

            while low <= high:
                mid = (low + high) // 2

                if intervals[mid][0] < end:
                    low = mid + 1
                elif intervals[mid][0] > end:
                    high = mid - 1
                else:
                    return intervals[mid][2]

            return intervals[low][2] if -1 < low < len(intervals) else -1

        res = [-1] * len(intervals)
        for i,(start, end, original_index) in enumerate(intervals):
            res[original_index] = getInterval(end)

        return res
