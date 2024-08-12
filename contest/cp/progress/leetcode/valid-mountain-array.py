class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        maxx = 0 
        for i, num in enumerate(arr):
            if num > arr[maxx]:
                maxx = i

        if maxx == len(arr) - 1 or maxx == 0 :
            return False

        inc = True
        for i in range(len(arr) - 1):
            if arr[i] == arr[maxx]:
                inc = False
            
            if inc and arr[i + 1] <= arr[i]:
                return False
            elif not inc and arr[i+1] >= arr[i]:
                return False
            else:
                continue

        return True

            


        