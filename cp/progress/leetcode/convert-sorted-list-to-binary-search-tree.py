# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid  - 1)
        root.right = self.helper(nums, mid  + 1, right)

        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []

        itr = head
        while itr:
            nums.append(itr.val)
            itr = itr.next

        return self.helper(nums, 0, len(nums) - 1)
        