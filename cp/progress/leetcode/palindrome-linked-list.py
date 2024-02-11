# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        itr = head
        while itr:
            nums.append(itr.val)
            itr = itr.next

        left,right = 0,len(nums) - 1

        while left < right:
            if nums[left] != nums[right]:
                return False

            left += 1
            right -= 1

        return True
                

        