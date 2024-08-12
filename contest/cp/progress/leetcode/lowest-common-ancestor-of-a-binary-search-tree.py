# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def Findlowest(root, minVal, maxVal):
            if not root:
                return None
            if minVal <= root.val <= maxVal:
                return root
            elif minVal > root.val:
                return Findlowest(root.right, minVal, maxVal)
            elif maxVal < root.val:
                return Findlowest(root.left, minVal, maxVal)

        return Findlowest(root, min(p.val, q.val), max(p.val, q.val))

        