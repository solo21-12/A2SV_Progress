# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, head: Optional[ListNode]):
        count = 0
        itr = head

        while itr:
            count += 1
            itr = itr.next

        return count // 2

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = self.get_length(head)

        itr = head
        while count:
            itr = itr.next
            count -= 1

        return itr
