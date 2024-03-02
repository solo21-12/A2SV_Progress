# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            path.append(root.val)
            inorder(root.right)

        path = []
        inorder(root)

        def build(left, right):
            if left > right:
                return

            mid = (left + right) // 2
            root = TreeNode(path[mid])
            root.left = build(left, mid  - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(path) - 1)
        