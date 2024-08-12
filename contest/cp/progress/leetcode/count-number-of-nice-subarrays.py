class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i,num in enumerate(nums):
            if num % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        prefixSum = {0:1}
        currSum,ans=0,0

        for num in nums:
            currSum += num

            if currSum - k in prefixSum:
                ans += prefixSum[currSum - k]

            prefixSum[currSum]= prefixSum.get(currSum,0) + 1


        return ans



