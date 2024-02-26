class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def findSubSequence(i, target, arr):
            N = len(candidates)

            if i >= N:
                if not target:
                    ans.append(arr[:])
                return

            if not target:
                ans.append(arr[:])
                return

            # This is when picking
            if target >= candidates[i]:
                arr.append(candidates[i])
                findSubSequence(i, target - candidates[i], arr)
                arr.pop()

                

            # This is when not picking
            findSubSequence(i + 1, target, arr)
           

        
        findSubSequence(0, target, [])

        return ans
            

