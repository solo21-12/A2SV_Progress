class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        low, high = 0, len(citations)

        while low < high:
            mid = (low + high) // 2
            size = N - mid
            
            if size <= citations[mid]:
                high = mid
            else:
                low = mid + 1

        return  len(citations) - low
        