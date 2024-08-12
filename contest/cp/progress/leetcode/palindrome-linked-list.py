# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''I'm using floyd's alog to find the middle of the linked list
        so when the fast pointer reach to the last node the slow one will reach the half of the linked list'''
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        '''
        I'm reversing the last half of the linked list to see if's equal to the first half of the linked 
        list
        '''
        prev_node, next_node = None, None
        while slow:
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        slow = prev_node

        '''
        I'm iterating through the 2 halfs to  see if they are palindrom
        '''
        itr = head
        while slow:
            if itr.val != slow.val:
                return False

            itr = itr.next
            slow = slow.next

        return True
