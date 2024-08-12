# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            nonlocal maxSum
            if not root:
                return (0, inf, -inf, True)

            curSumLeft, minRight_left, maxLeft_left, isBst_left = dfs(root.left)
            curSumRight, minRight_right, maxLeft_right, isBst_right = dfs(root.right)

            if isBst_left and isBst_right:
                isBst = maxLeft_left < root.val < minRight_right
                minn = min(root.val, minRight_right, minRight_left)
                maxx = max(root.val,maxLeft_left,maxLeft_right)
                curSum = 0

                if isBst:
                    curSum = curSumLeft + curSumRight + root.val
                    maxSum = max(maxSum, curSum, 0)
                    

                return (curSum, minn, maxx, isBst)

            return (0, 0, 0, False)
        
        maxSum = -inf
        dfs(root)

        return maxSum        
