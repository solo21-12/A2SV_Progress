# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0

        itr = head

        while itr:
            count += 1
            itr = itr.next
        

        count = (count // 2)

        itr = head
        while count:
            itr = itr.next
            count -= 1

        return itr
        