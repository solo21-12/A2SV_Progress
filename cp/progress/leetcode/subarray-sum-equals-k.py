class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = { 0:1 }
        res,currSum = 0,0

        for num in nums:
            currSum += num
            diff = currSum - k

            res += prefixSums.get(diff,0)
            prefixSums[currSum] = prefixSums.get(currSum,0) + 1

        return res