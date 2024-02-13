# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddNode,evenNode = ListNode(),ListNode()
        tailOdd,tailEven = oddNode,evenNode

        itr = head
        count = 1
        while itr:
            if count % 2:
                tailOdd.next = itr
                tailOdd = itr
            else:
                tailEven.next = itr
                tailEven = itr

            itr = itr.next
            count += 1
            
        if tailEven.next:
            tailEven.next = None

        tailOdd.next = evenNode.next

        return oddNode.next
        