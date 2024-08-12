# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def validate(node1, node2):
            if not node1 or not node2:
                return node1 is node2

            if node1.val != node2.val:
                    return False

            return validate(node1.left , node2.left) and validate(node1.right, node2.right)

        result = validate(p, q)

        return result
