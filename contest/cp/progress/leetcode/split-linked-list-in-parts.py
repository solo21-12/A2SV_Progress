# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        itr = head 

        while itr:
            count += 1
            itr = itr.next 

        ans = []
        rem = count % k
        each = count // k

        itr = head
        while itr:
            ans.append(itr)
            if rem:
                for _ in range(each):
                    itr = itr.next

                rem -= 1
            else:
                for _ in range(each - 1):
                    itr = itr.next

            temp = itr
            itr = itr.next
            temp.next = None
    
              
        
        
        for _ in range(k - len(ans)):
            ans.append(ListNode(""))

        return ans

        
        