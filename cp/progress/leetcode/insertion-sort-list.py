# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-5001)

        prev_node = dummyHead
        itr = head
        while itr:
            next_node = itr.next
            pos_searching_node = itr
            pos_searching_node.next = None
            itr = next_node


            prev = dummyHead
            curr_node = prev

            while curr_node and pos_searching_node.val > curr_node.val:
                prev = curr_node
                curr_node = curr_node.next

            pos_searching_node.next = prev.next
            prev.next = pos_searching_node

        return dummyHead.next



        