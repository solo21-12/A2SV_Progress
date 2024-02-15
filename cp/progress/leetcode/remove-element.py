class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start,end = 0 , len(nums) - 1

        if len(nums) == 1 and nums[0] == val:
            nums.clear()
            return 0

        while start <= end:
            if nums[start] == val:
                nums[start],nums[end] = nums[end],nums[start]
                end -= 1
            else:
                start += 1


        return end + 1
            
            
        