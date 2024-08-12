# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            if list1.val <= list2.val:
               tail.next = list1
               list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # moving to the last element added to the tail node
            tail = tail.next
        # if we have a remininig elements
        if list1:
            tail.next = list1
            
        
        if list2:
            tail.next = list2

        return dummy.next


        
