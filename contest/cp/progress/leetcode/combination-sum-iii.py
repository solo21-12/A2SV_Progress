class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        ans = []

        def findCombinations(i, k, n, arr):

            N = len(nums)
            if i >= N:
                if not k and not n:
                    ans.append(arr[:])

                return

            if not k:
                if not n:
                    ans.append(arr[:])

                return

            if nums[i] <= n:
                arr.append(nums[i])
                findCombinations(i + 1, k - 1, n - nums[i], arr)
                arr.pop()

            findCombinations(i + 1, k, n, arr)


        findCombinations(0, k, n, [])

        return ans

        