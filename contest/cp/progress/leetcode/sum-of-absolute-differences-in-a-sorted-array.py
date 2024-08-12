class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        prefix,ans = [],[]
        leftSum,rightSum = 0,0
        suffix =[0]*len(nums)

        for num in nums:
            leftSum += num
            prefix.append(leftSum)
        
        for i in range(len(nums)-1,-1,-1):
            rightSum += nums[i]
            suffix[i] = rightSum

        for i in range(len(nums)):
            leftSum,rightSum = 0, 0
            if i > 0:
                leftSum = prefix[i-1]

            if i < len(nums) - 1:
                rightSum = suffix[i+1]
            
            ls = (nums[i] * i) - leftSum
            rs = rightSum - (nums[i] * (len(nums) - i - 1))  

            ans.append(ls + rs)

        return ans


