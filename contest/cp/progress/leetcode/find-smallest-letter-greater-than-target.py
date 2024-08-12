class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)

        low, high = 0, N - 1

        while low <= high:
            mid = (low + high) // 2

            if letters[mid] > target:
                high = mid - 1
            else:
                low = mid  + 1

        return letters[low] if low < N else letters[0]
        