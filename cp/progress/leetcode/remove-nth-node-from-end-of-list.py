# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        aheadPtr, behindPtr = dummy, dummy

        while n > 0:
            aheadPtr = aheadPtr.next
            n -= 1
            
        while aheadPtr and aheadPtr.next:
            aheadPtr = aheadPtr.next
            behindPtr = behindPtr.next

        if behindPtr.next:
            behindPtr.next = behindPtr.next.next

        return dummy.next
