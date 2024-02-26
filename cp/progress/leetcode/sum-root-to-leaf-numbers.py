# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def preOrder(root, nums):
            nonlocal ans
            if not root:
                return

            if not root.left and not root.right:
                num = "".join(nums)
                num += str(root.val)
                ans += int(num)

            nums.append(str(root.val))
            preOrder(root.left, nums)
            preOrder(root.right, nums)
            nums.pop()

        preOrder(root, [])

        return ans
