class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combinations(i, arr):
            # This implmentation has a slower time due to a second recursion
            if i > n:
                return
            
            if len(arr) == k:
                ans.append(arr[:])
                return

            # This is picking the current index element
            arr.append(i + 1)
            combinations(i + 1, arr)

            # This is not picking the current element and move to the next index element
            arr.pop()
            combinations(i + 1, arr)


        def backtrack(i, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return

            for choice in range(i + 1, n + 1):
                arr.append(choice)
                backtrack(choice, arr)
                arr.pop()


        ans = []
        # combinations(0, [])
        backtrack(0, [])

        return ans


