class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = bisect.bisect_right(arr, x)
        l = r - 1
        res = []

        while k and l >= 0 and r < len(arr):
            distL = x - arr[l]
            distR = arr[r] - x

            if distL <= distR:
                bisect.insort(res, arr[l])
                l -= 1
            else:
                bisect.insort(res, arr[r])
                r += 1

            k -= 1

        while k and l >= 0:
            bisect.insort(res, arr[l])
            l -= 1
            k -= 1

        while k and r < len(arr):
            bisect.insort(res, arr[r])
            r += 1
            k -= 1

        return res



         
        