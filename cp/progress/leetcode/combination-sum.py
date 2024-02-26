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

            # if at any stage we reach to the target 
            if not target:
                ans.append(arr[:])
                return

            # This is when picking
            if target >= candidates[i]:
                arr.append(candidates[i])
                findSubSequence(i, target - candidates[i], arr)
                # This is removing the picked element
                arr.pop()

            # This is when not picking
            findSubSequence(i + 1, target, arr)

        findSubSequence(0, target, [])

        return ans


'''
the idea is as follows if the current element is less than the target we keep picking the element 
else we remove it and go to the next index

'''