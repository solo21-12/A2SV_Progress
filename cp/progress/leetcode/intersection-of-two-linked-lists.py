# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        countA,countB = 0,0
        tailA,tailB = headA,headB

        while tailA and tailA.next:
            tailA = tailA.next
            countA += 1

        while tailB and tailB.next:
            tailB = tailB.next
            countB += 1

        if tailA != tailB:
            return None

        diff = abs(countA-countB)

        
        if countA >= countB:
            while diff:
                headA = headA.next
                diff -= 1
        else:
            while diff:
                headB = headB.next
                diff -= 1


        while headA:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next


        return None


        



        