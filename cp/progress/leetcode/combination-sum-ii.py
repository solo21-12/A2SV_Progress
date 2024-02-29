class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def findCombinations(i, target, arr):

            N = len(candidates)

            if i >= N:
                if not target:
                    ans.append(arr[:])

                return

            if not target:
                ans.append(arr[:])
                return


            if candidates[i] <= target:
                arr.append(candidates[i])
                findCombinations(i + 1, target - candidates[i], arr)
                arr.pop()

            while i + 1 < N and candidates[i] == candidates[i + 1]:
                i += 1

            findCombinations(i + 1, target, arr)


        findCombinations(0, target, [])


        return ans