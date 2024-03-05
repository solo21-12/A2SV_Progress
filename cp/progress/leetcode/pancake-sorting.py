class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        def swap(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        r = len(arr)
        res = []

        while r > 0:

            curMax = (-inf, 0)

            for i in range(r):
                if arr[i] > curMax[0]:
                    curMax = (arr[i], i)

            res.append(curMax[1] + 1)
            res.append(r)

            swap(0, curMax[1])
            swap(0, r - 1)

            r -= 1

        return res
