class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans = []

        for num in arr2:
            if count[num]:
                for _ in range(count[num]):
                    ans.append(num)

                count[num] = 0
            else:
                ans.append(num)

        for key in sorted(list(count.keys())):
            if count[key] > 0:
                for _ in range(count[key]):
                    ans.append(key)

        return ans
            
            
            
        