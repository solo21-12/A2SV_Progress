class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans,currSum = 0,0
        s = { 0:1 }
        
        for num in nums:
            currSum += num
            diff = currSum - goal
            ans += s.get(diff,0)

            s[currSum] = s.get(currSum,0) + 1

        return ans