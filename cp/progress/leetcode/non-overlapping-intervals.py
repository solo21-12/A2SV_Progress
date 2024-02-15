class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        
        lastEnd = intervals[0][1]
        count = 1

        for start, end in intervals[1:]:
            if start < lastEnd:
                lastEnd = min(lastEnd, end)
            else:
                count += 1
                lastEnd = end

        return len(intervals) - count



        