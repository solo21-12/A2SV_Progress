class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        res,curSum = 0,0

        for num in nums:
            curSum += num
            rem = curSum % k

            res += prefix.get(rem,0)
            prefix[rem] = prefix.get(rem,0) + 1


        return res
           

        