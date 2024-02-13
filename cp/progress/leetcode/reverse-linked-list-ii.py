# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,startNode, endNode, nextEndNode):
        prevNode, nextNode = nextEndNode, None

        

        while startNode != nextEndNode:
            nextNode = startNode.next
            startNode.next = prevNode
            prevNode = startNode
            startNode = nextNode

        return prevNode


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prevStart,nextEnd = None, None
        startNode, endNode = None, None

        if left == right:
            return head

        itr = head
        count = 1

        while itr:
            if count == left - 1:
                prevStart = itr

            if count == right + 1:
                nextEnd = itr

            if count ==  left:
                startNode = itr

            if count == right:
                endNode = itr

            itr = itr.next
            count += 1



        newConnection = self.reverse(startNode, endNode, nextEnd)

        if prevStart:
            prevStart.next = newConnection
        else:
            head = newConnection
        

        return head



        