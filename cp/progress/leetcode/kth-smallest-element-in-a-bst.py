# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        def traverse(root, result):
            if not root:
                return

            traverse(root.left, result)
            result.append(root.val)
            traverse(root.right, result)


        result = []
        traverse(root, result)

        return result[k - 1]