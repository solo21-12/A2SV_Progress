class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        count = {}
        sorted_nums = sorted(nums)

        for index,num in enumerate(sorted_nums):
            if num not in count:
                count[num] = index

        ans = [count[num] for num in nums]

        return  ans

        