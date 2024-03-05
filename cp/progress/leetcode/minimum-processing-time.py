class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        processorTime.sort()
        tasks.sort(reverse=True)
        n = len(tasks) // len(processorTime)
        l = 0

        minTime = -inf
        for pro in processorTime:
            minTime = max(minTime, pro + tasks[l])
            l += n 

        return minTime
