# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head:
            return None

        lessPtr, greaterPtr = ListNode(), ListNode()
        lessTail, greaterTail = lessPtr, greaterPtr

        while head:
            if head.val < x:
                lessTail.next = head
                lessTail = head
            else:
                greaterTail.next = head
                greaterTail = head

            head = head.next

        if greaterTail.next:
            greaterTail.next = None

        lessTail.next = greaterPtr.next

        return lessPtr.next

        