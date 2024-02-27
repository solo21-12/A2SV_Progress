# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal ans
            if not root:
                return (float("inf"), float("-inf"))

            if not root.left and not root.right:
                return (root.val, root.val)

            left = dfs(root.left)
            right = dfs(root.right)

            minn = min(left[0], right[0])
            maxx = max(left[1], right[1])

            ans = max(ans, abs(root.val - minn), abs(root.val - maxx))

            return (min(root.val, minn), max(maxx, root.val))

        ans = 0
        dfs(root)
        return ans
