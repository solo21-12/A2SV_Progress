class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = {num: i for i,num in enumerate(nums1) }
        stack = []
        res = [-1] * len(nums1)

        for num in nums2:

            while stack and stack[-1] < num:
                cur = stack.pop()

                if cur in index:
                    res[index[cur]] = num

            stack.append(num)

        return res

                

        