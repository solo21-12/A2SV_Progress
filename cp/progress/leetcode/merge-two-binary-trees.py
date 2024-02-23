# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        def merge(left, right):
            if not left and not right:
                return None
            elif not left:
                return right
            elif not right:
                return left
            else:
                left.val = left.val + right.val
                left.left = merge(left.left, right.left)
                left.right = merge(left.right, right.right)

                return left

        

        return merge(root1, root2)
        